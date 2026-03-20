import os
import sys
import pathlib
import fitz
import json
from groq import Groq
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import tempfile
import uvicorn
from gtts import gTTS
from fastapi.responses import FileResponse
import tempfile
import uuid

# Load .env
env_path = pathlib.Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend files
frontend_path = pathlib.Path(__file__).parent.parent / "frontend"

if frontend_path.exists():
    app.mount("/static", StaticFiles(directory=str(frontend_path)), name="static")

@app.get("/")
def serve_frontend():
    return FileResponse(str(frontend_path / "index.html"))

def extract_text_from_pdf(pdf_bytes):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    doc.close()
    return full_text

def analyze_loan_document(text, language="Hindi"):
    prompt = f"""
You are a financial literacy assistant helping rural Indians understand loan documents.

Analyze this loan document and find all important clauses.
For each clause return:
- "original": short original clause text
- "simple_english": explain in simple English (Class 6 level)
- "translation": explain in simple {language} (Class 6 level)
- "risk": "high", "medium", or "low"
- "warning": one-line warning for high/medium risk, empty string for low

Return ONLY a valid JSON array. No extra text.

Loan document:
{text[:3000]}
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    content = response.choices[0].message.content
    content = content.strip()
    if content.startswith("```"):
        content = content.split("```")[1]
        if content.startswith("json"):
            content = content[4:]
    content = content.strip()
    return json.loads(content)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...), language: str = "Hindi"):
    pdf_bytes = await file.read()
    text = extract_text_from_pdf(pdf_bytes)
    clauses = analyze_loan_document(text, language)
    return {"clauses": clauses, "filename": file.filename, "language": language}
class QuestionRequest(BaseModel):
    question: str
    language: str = "Hindi"
    context: str = ""

@app.post("/ask")
async def ask_question(req: QuestionRequest):
    prompt = f"""
You are a financial literacy assistant helping rural Indians understand loan documents.

The user has a question about their loan document. Answer in simple {req.language}
at a Class 6 reading level. Keep the answer short — 2 to 3 sentences maximum.

Loan document context:
{req.context[:1500]}

User question: {req.question}

Answer only in {req.language}. Be simple, clear and helpful.
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    answer = response.choices[0].message.content.strip()
    return {"answer": answer}
class SpeakRequest(BaseModel):
    text: str
    language: str = "Hindi"

@app.post("/speak")
async def speak_text(req: SpeakRequest):
    lang_code_map = {
        "Hindi":          "hi",
        "Tamil":          "ta",
        "Telugu":         "te",
        "Marathi":        "mr",
        "Bengali":        "bn",
        "Kannada":        "kn",
        "Simple English": "en"
    }
    lang_code = lang_code_map.get(req.language, "hi")

    # Generate audio file
    tts = gTTS(text=req.text, lang=lang_code, slow=False)
    filename = f"speech_{uuid.uuid4().hex}.mp3"
    filepath = os.path.join(tempfile.gettempdir(), filename)
    tts.save(filepath)

    return FileResponse(
        filepath,
        media_type="audio/mpeg",
        filename=filename
    )

@app.get("/ping")
def ping():
    return {"status": "awake"}
if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
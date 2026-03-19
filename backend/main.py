import os
import sys
import pathlib
import fitz
from groq import Groq
from dotenv import load_dotenv

# Load .env
env_path = pathlib.Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("❌ ERROR: GROQ_API_KEY not found!")
    sys.exit(1)

print("✅ API key loaded successfully!")
client = Groq(api_key=api_key)

# ── Sample text (used when no PDF is given) ──────────────────────────────────
SAMPLE_TEXT = """
The borrower's property shall serve as collateral and the lender may invoke 
rights under SARFAESI Act 2002 in case of 3 consecutive EMI defaults.
The rate of interest shall be subject to revision at the sole discretion of 
the lending institution without prior notice to the borrower.
In the event of prepayment, the borrower shall be liable to pay a prepayment 
penalty of 2% on the outstanding principal amount.
"""

# ── Function 1: Extract text from PDF ────────────────────────────────────────
def extract_text_from_pdf(pdf_path):
    print(f"📄 Reading PDF: {pdf_path}")
    doc = fitz.open(pdf_path)
    full_text = ""
    page_count = len(doc)  # save page count BEFORE closing
    for page_num, page in enumerate(doc):
        text = page.get_text()
        full_text += f"\n--- Page {page_num + 1} ---\n{text}"
    doc.close()
    print(f"✅ Extracted {len(full_text)} characters from {page_count} pages")
    return full_text

# ── Function 2: Analyze with AI ──────────────────────────────────────────────
def analyze_loan_document(text):
    prompt = f"""
You are a financial literacy assistant helping rural Indians understand loan documents.

Analyze this loan document text and do the following:
1. Find all important clauses
2. For each clause give:
   - "original": the original clause text (keep it short)
   - "simple_english": Explain in very simple English (Class 6 level)
   - "hindi": Explain in simple Hindi (Class 6 level)
   - "risk": Rate as "high", "medium", or "low"
   - "warning": A one-line warning if risk is high or medium, empty string if low

Return ONLY a valid JSON array. No extra text before or after.

Example format:
[
  {{
    "original": "clause text here",
    "simple_english": "simple explanation here",
    "hindi": "simple hindi explanation here",
    "risk": "high",
    "warning": "warning message here"
  }}
]

Loan document text:
{text[:3000]}
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return response.choices[0].message.content

# ── Main: Run everything ──────────────────────────────────────────────────────
print("\n🔍 Analyzing loan document...\n")

if len(sys.argv) > 1:
    pdf_path = sys.argv[1]
    text = extract_text_from_pdf(pdf_path)
else:
    print("No PDF provided — using sample text\n")
    text = SAMPLE_TEXT

result = analyze_loan_document(text)
print(result)
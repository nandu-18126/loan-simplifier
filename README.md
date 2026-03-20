# 🏦 Loan Document Simplifier **[🚀 Live Demo](https://loan-simplifier.onrender.com)**
> ⚠️ **Important:** Open in Google Chrome for full functionality. 

An AI-powered platform that reads loan documents, detects dangerous clauses, 
and explains them in 7 Indian languages — with full voice support.
Built for the 190 million Indians who sign documents they cannot understand.
---

## 💭 Why we Built This

> 📊 **190 million** Indians have no credit/loan literacy tools  
> 📊 **55%** of rural Indians want to understand loans but can't  
> 📊 **86%** sign documents without fully understanding them  
> *(Sources: World Bank 2023, NABARD Survey, RBI Annual Report)*

In many parts of India, especially rural areas, people are given long loan documents in English filled with legal terms. Most of them don’t fully understand what they’re signing.

Sometimes, important conditions are hidden deep inside — like losing property after missing a few payments.

For example:

> “The lender may invoke rights under SARFAESI Act 2002 in case of 3 consecutive EMI defaults.”

Which basically means:

👉 If you miss 3 EMIs, the bank can take your property — even without going to court.

That’s a serious thing, and many people don’t realize it.

So we thought — what if we could **simplify these documents using AI**?

---

## 💡 What This Project Does

This is a web app that helps users understand loan documents easily.

You can:

* Upload a loan PDF (even a scanned one)
* It reads and analyzes the document
* Highlights important clauses
* Shows risk levels (high / medium / low)
* Explains everything in simple language
* Translates into Indian languages
* Even reads it aloud

---

## ✨ Main Features

### 📄 Document Analysis

Upload a loan file → get important clauses extracted automatically.

### 🚨 Risk Highlighting

Each clause is marked as:

* 🔴 High risk → needs attention
* 🟡 Medium risk → be careful
* 🟢 Low risk → normal

### 🌐 Language Support

Supports multiple Indian languages like:

* Hindi
* Tamil
* Telugu
* Marathi
* Bengali
* Kannada
* Simple English

### 🔊 Voice Support

* Reads explanations aloud
* User can ask questions using voice
* Answers are also spoken

---

## 🛠 Tech Stack

We tried to keep things simple:

* **Frontend**: HTML, CSS, JavaScript
* **Backend**: Python + FastAPI
* **AI Model**: Groq API (Llama 3)
* **PDF Reading**: PyMuPDF
* **Text-to-Speech**: gTTS
* **Speech Input**: Web Speech API
* **Deployment**: Render

---

## 🚀 How to Run This Project

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/loan-simplifier.git
cd loan-simplifier
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add API key

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

### 4. Run backend

```bash
cd backend
python api.py
```

### 5. Open in browser

```
http://localhost:8000
```

---
### 6.Screenshot:
<img width="1920" height="1128" alt="Screenshot 2026-03-20 174917" src="https://github.com/user-attachments/assets/6ce7e51a-4042-4f44-b3e4-5ec4046e0fed" />
<img width="1920" height="1128" alt="Screenshot 2026-03-20 174935" src="https://github.com/user-attachments/assets/006181e2-8c42-472e-942e-400250b920c4" />
<img width="1920" height="1128" alt="Screenshot 2026-03-20 174952" src="https://github.com/user-attachments/assets/59cf3d1c-2fa8-493f-8612-52ef73b45566" />
<img width="1920" height="1128" alt="Screenshot 2026-03-20 175009" src="https://github.com/user-attachments/assets/6ceca23d-8413-4056-b1f8-8dbb836415b3" />
<img width="1920" height="1128" alt="Screenshot 2026-03-20 175047" src="https://github.com/user-attachments/assets/7a72ad2b-f581-42d7-8a22-4b95c2e3d669" />


## 📁 Project Structure

```
loan-simplifier/
│
├── backend/
│   ├── api.py
│   └── main.py
│
├── frontend/
│   └── index.html
│
├── sample_docs/
│   └── sample_loan_agreement.pdf
│
├── requirements.txt
└── README.md
```

---

## 🔌 API Endpoints

* `GET /` → Loads the web app
* `POST /analyze` → Upload PDF and get analysis
* `POST /ask` → Ask questions about document
* `POST /speak` → Convert text to speech

---

## 🌍 Why This Matters

This is not just a project — it can actually help people.

* Helps users understand risky clauses
* Prevents financial mistakes
* Makes legal language simpler
* Useful for people who can’t read English
* Works with just a browser (no app needed)

---

⚠️ Note

This is only for learning and awareness.

It is **not a replacement for legal advice**.
Users should still consult professionals before making financial decisions.

---
## 🏆 Hackathon Submission

**Event:** HACK HUSTLE
CODE KNIGHT  
**Track:** FinTech / Financial Inclusion  
**Team:**  Zenith  
**Members:** Nandini, Lakshana  
**College:** Panimalar Engineering college  

### 📚 References
- NABARD Financial Inclusion Survey 2023
- RBI Annual Report 2024
- World Bank Global Findex Database 2023
- SARFAESI Act 2002 — Government of India
- Bhashini Initiative — MeitY

## 🏁 Final Thought

We built this with a simple idea:

> People should understand what they are signing — especially when it involves their money or property.



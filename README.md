🎯 AI Resume — Job Description Matcher
Upload a resume. Paste a job description. Get an instant match score and see exactly which skills you're missing — in seconds.


🎯 The Problem It Solves
Recruiters receive hundreds of resumes per job posting. Manually reviewing them is slow, inconsistent, and error-prone. Candidates also apply without knowing how well they actually fit a role.

This tool solves both sides:

For recruiters — rank candidates by fit score instantly
For candidates — see exactly which skills to add before applying


✨ Features
📄 PDF Resume Parsing — extracts text automatically from any PDF resume
📋 Job Description Analysis — processes raw JD text, no formatting required
📊 Match Score — cosine similarity between resume and JD vectors
❌ Missing Skills Detection — highlights skills in the JD not found in the resume
⚡ Instant Results — processes in under 2 seconds
🖥️ Interactive Dashboard — clean Streamlit UI with visual match breakdown


🛠️ Tech Stack
Component
Technology
PDF Parsing
pdfplumber
NLP Vectorization
TF-IDF (Scikit-learn)
Similarity Scoring
Cosine Similarity
Skills Extraction
Custom NLP pipeline (skills.txt)
Frontend
Streamlit
Language
Python 3.x



⚙️ How to Run
1. Clone the repo
git clone https://github.com/Riyaguptacse/resume_job_matcher.git

cd resume_job_matcher
2. Create virtual environment
python -m venv venv

source venv/bin/activate  # Mac/Linux

venv\Scripts\activate     # Windows
3. Install dependencies
pip install -r requirements.txt
4. Run the app
streamlit run app.py
5. Upload your resume PDF + paste a job description → get your score!

🧠 How It Works

User uploads PDF resume + pastes job description
↓
pdfplumber extracts text from PDF
↓
Both texts cleaned and preprocessed
↓
TF-IDF vectorization applied to both documents
↓
Cosine similarity computed → match percentage
 ↓
Skills extracted from JD vs resume using skills.txt
↓
Missing skills identified
↓
Streamlit dashboard renders: score + matched skills + gaps

Why TF-IDF + Cosine Similarity? TF-IDF weights domain-specific terms (e.g. "PyTorch", "RAG", "SageMaker") by importance. Cosine similarity then measures how aligned the two documents are — fast, interpretable, and no black-box decisions.


📁 Project Structure
resume_job_matcher/

├── app.py              # Streamlit frontend + main logic

├── utils.py            # PDF parsing, vectorization, similarity scoring

├── skills.txt          # Curated skills dictionary for extraction

├── requirements.txt    # Python dependencies

└── README.md


📊 Results
Reduces manual resume screening effort by ~70%
Processes resume + JD match in under 2 seconds
Fully interpretable — every score is explainable


🔮 Future Improvements
Upgrade to BERT/sentence-transformer embeddings for deeper semantic matching
Add ATS keyword optimization suggestions
Support DOCX resume uploads
Deploy on Streamlit Cloud for public access
Add batch processing for multiple resumes


📬 Contact
Riya Gupta — AI/ML Engineer | Montreal, Canada 📧 riyagupta9906@gmail.com 🔗 LinkedIn 🐙 GitHub


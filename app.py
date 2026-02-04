import streamlit as st
from utils import extract_text_from_pdf, clean_text, extract_skills, calculate_similarity
import pandas as pd

# Page configuration
st.set_page_config(page_title="Resume Job Matcher", layout="centered")

st.title("📄 Resume Parser & Job Matcher")

# Upload resume
uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

# Paste job description
jd_text = st.text_area("Paste Job Description")

# Load skills from file
with open("skills.txt", "r") as f:
    skills_list = [line.strip().lower() for line in f if line.strip()]


# Process resume
if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)
    resume_text_clean = clean_text(resume_text)
    st.subheader("📝 Resume Preview (first 500 characters)")
    st.write(resume_text[:500] + ("..." if len(resume_text) > 500 else ""))

# Process job description
if jd_text:
    jd_text_clean = clean_text(jd_text)
    st.subheader("📄 Job Description Preview (first 500 characters)")
    st.write(jd_text[:500] + ("..." if len(jd_text) > 500 else ""))

# Perform matching if both are provided
if uploaded_file and jd_text:
    # Extract skills
    resume_skills = extract_skills(resume_text_clean.lower(), skills_list)
    jd_skills = extract_skills(jd_text_clean.lower(), skills_list)

    # Calculate similarity based on skills
    match_percentage = calculate_similarity(" ".join(resume_skills), " ".join(jd_skills))

    # Display results
    st.subheader("📊 Match Results")
    st.metric("Match Percentage", f"{match_percentage}%")

    st.subheader("🔹 Matched Skills")
    matched_skills = sorted(list(set(resume_skills) & set(jd_skills)))
    st.write(matched_skills if matched_skills else "No matched skills found.")

    st.subheader("✅ Skills Found in Resume")
    st.write(sorted(resume_skills))

    st.subheader("❌ Missing Skills")
    missing_skills = sorted(list(set(jd_skills) - set(resume_skills)))
    st.write(missing_skills if missing_skills else "All required skills are present ✅")

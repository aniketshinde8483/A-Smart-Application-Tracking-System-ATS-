import streamlit as st
import google.generativeai as genai
import os
import fitz  # PyMuPDF
from dotenv import load_dotenv
import re
import json  # Import json for safer parsing

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

def clean_and_preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s\.\,\;\:\-]", "", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[\*\•]", "-", text)
    return text

def create_prompt(template, resume_text, jd_text):
    return template.format(resume=resume_text, jd=jd_text)

def calculate_jd_score(resume_text, jd_text):
    prompt = create_prompt(ATS_PROMPT_TEMPLATE, resume_text, jd_text)
    response = get_gemini_response(prompt)
    
    
    st.text_area("API Response", response)
    
    jd_match = 0
    try:
        
        response_dict = json.loads(response)
        jd_match = float(response_dict["JD Match"].strip('%'))
    except json.JSONDecodeError as e:
        st.error(f"Error decoding JSON response: {e}")
    except KeyError as e:
        st.error(f"Missing expected key in response: {e}")
    except Exception as e:
        st.error(f"Unexpected error: {e}")
    return jd_match


ATS_PROMPT_TEMPLATE = """
Hey Act Like a skilled or very experienced ATS (Application Tracking System)
with a deep understanding of the tech field, software engineering, data science, data analysis,
and big data engineering. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving the resumes. Assign the percentage matching based 
on JD and the missing keywords with high accuracy.
resume:{resume}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%",
"MissingKeywords":[],
"Profile Summary":""}}
"""

HR_PROMPT_TEMPLATE = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
resume:{resume}
description:{jd}
"""

PERCENTAGE_MATCH_PROMPT_TEMPLATE = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
the job description. First, the output should come as percentage, then keywords missing, and last final thoughts.
resume:{resume}
description:{jd}
"""

# Streamlit App
st.set_page_config(page_title="Smart Applicant Tracking System for Resume")
st.title("Smart ATS")
st.text("Improve Your Resume ATS")

jd = st.text_area("Paste the Job Description")
uploaded_files = st.file_uploader("Upload Your Resume", type="pdf", accept_multiple_files=True, help="Please upload the PDF")

jd_scores = {}  # Dictionary to store JD scores for each resume

if uploaded_files:
    st.sidebar.subheader("Controls")
    top_n = st.sidebar.slider("Number of Top Resumes to Display", min_value=1, max_value=len(uploaded_files), value=5)

if st.sidebar.button("Rank Candidates"):
    for uploaded_file in uploaded_files:
        raw_text = extract_text_from_pdf(uploaded_file)
        resume_text = clean_and_preprocess_text(raw_text)
        jd_score = calculate_jd_score(resume_text, jd)
        filename = uploaded_file.name if uploaded_file.name else "Unnamed"
        jd_scores[filename] = jd_score

    # Sort resumes based on JD scores
    sorted_resumes = sorted(jd_scores.items(), key=lambda x: x[1], reverse=True)

    # Display ranked resumes
    st.subheader("Ranked Candidates based on JD Score:")
    for idx, (filename, score) in enumerate(sorted_resumes[:top_n], start=1):
        st.write(f"{idx}. {filename}: {score}% JD Match")

if st.button("Submit"):
    for uploaded_file in uploaded_files:
        raw_text = extract_text_from_pdf(uploaded_file)
        resume_text = clean_and_preprocess_text(raw_text)
        prompt = create_prompt(ATS_PROMPT_TEMPLATE, resume_text, jd)
        response = get_gemini_response(prompt)
        st.subheader("ATS Evaluation Result")
        st.write(response)

if st.sidebar.button("Tell Me About the Resume"):
    for uploaded_file in uploaded_files:
        raw_text = extract_text_from_pdf(uploaded_file)
        resume_text = clean_and_preprocess_text(raw_text)
        prompt = create_prompt(HR_PROMPT_TEMPLATE, resume_text, jd)
        response = get_gemini_response(prompt)
        st.subheader("HR Evaluation")
        st.write(response)

if st.sidebar.button("Percentage Match"):
    for uploaded_file in uploaded_files:
        raw_text = extract_text_from_pdf(uploaded_file)
        resume_text = clean_and_preprocess_text(raw_text)
        prompt = create_prompt(PERCENTAGE_MATCH_PROMPT_TEMPLATE, resume_text, jd)
        response = get_gemini_response(prompt)
        st.subheader("ATS Percentage Match")
        st.write(response)

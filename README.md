# A-Smart-Application-Tracking-System-ATS-
smart applicant tracking system (ats) for resume improvement optimize your resume with our smart ats! leveraging google generative ai, it evaluates resumes against job descriptions, calculates match percentages, ranks multiple resumes, and provides hr feedback.  setup install dependencies. set google api key in .env file. run the streamlit app.
Smart Applicant Tracking System (ATS) for Resume Improvement
Welcome to the Smart Applicant Tracking System (ATS) for Resume Improvement! This project is designed to help job seekers enhance their resumes by providing insightful feedback and scoring them against job descriptions using advanced AI models. Our system leverages Google Generative AI to simulate the behavior of an experienced ATS and a technical Human Resource Manager to provide detailed evaluations of your resume.

Features
1. Resume Evaluation Against Job Description
Upload your resume and paste a job description to receive a comprehensive evaluation. The AI will analyze your resume based on the job requirements, highlighting strengths, weaknesses, and missing keywords.

2. JD Score Calculation
Our AI calculates a percentage match score between your resume and the job description, giving you a clear idea of how well your resume fits the job. It also lists missing keywords that are crucial for the job, helping you to improve your resume effectively.

3. Ranked Candidates
If you upload multiple resumes, the system can rank them based on their JD scores, allowing you to see which resume is the most competitive for the given job description.

4. HR Evaluation
Get professional evaluation feedback from an AI that acts like a technical Human Resource Manager. This feature provides a detailed review of your resume’s strengths and areas for improvement.

How It Works
Input Job Description and Upload Resume
Paste the Job Description: Provide the job description in the designated text area.
Upload Resume: Upload your resume in PDF format. You can upload multiple resumes to compare their scores.
AI Analysis
The AI processes the uploaded resumes and evaluates them against the provided job description. It cleans and preprocesses the text for accurate analysis.

Generate Prompt
A prompt is created using the job description and the resume text. This prompt is sent to the Google Generative AI, which generates a response detailing the JD match percentage, missing keywords, and a profile summary.

Display Results
JD Scores: The system calculates and displays the JD match percentage for each uploaded resume.
Ranked Candidates: Resumes are ranked based on their JD scores, and the top resumes are displayed.
HR Evaluation: Detailed feedback is provided from the AI HR perspective.
ATS Percentage Match: A straightforward percentage match score is given for quick evaluation.
Setup and Usage
Prerequisites
Python environment with required libraries (streamlit, google.generativeai, fitz, dotenv, re, json)
Google API key for Generative AI
Installation
Clone this repository.
Install the necessary dependencies using pip install -r requirements.txt.
Set up your environment variables by creating a .env file and adding your Google API key:
makefile
Copy code
GOOGLE_API_KEY=your_api_key_here
Running the Application
Run the Streamlit app:
arduino
Copy code
streamlit run app.py
Open your browser and go to http://localhost:8501 to use the application.
Controls
Use the sidebar controls to select the number of top resumes to display and to initiate various actions like ranking candidates, getting HR evaluation, and percentage match.
Example Usage
Paste the job description in the provided text area.
Upload one or multiple resumes in PDF format.
Use the sidebar to rank candidates based on JD scores, get detailed HR feedback, or get a quick percentage match.
Contributions
We welcome contributions from the community! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

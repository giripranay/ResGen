

Project description: The project resgen is a short form for resume generation. The main idea behind project is to generate tailored resume based on job description and your current resume. We leverage the power LLMs to accomplish this task.

Main features includes:  Identify main Keywords and include it,  Generate dynamic relationed work experiences, Generate dynamic projects related to job description, Modify work experience, Update latest work experience to align job description.


Workflow:

Analyize job description, your resume and identify important keywords, suggestions to tailor resume using LLM.
Give suggestion, keywords, job description, your resume to generate final resume in json format.
Generate PDF of resume from JSON.

File descriptions:

score.py : Geneartes "score", "missing_skills", "keywords","suggestions" using LLM OPENAI Chatgpt-40
generateResume.py :  Generates tailored resume in json format given Job description, keywords, suggestions, missing skills.
prompts : A folder contains prompts used in this project.
JDs: folder contains text files of job description with company name as file name.
PDFs: folder  contains pdf files of final tailored resume with company name as file name.
resume.txt : A text file contains your current resume.

userInterface.py : Python script uses Streamlit to create an interactive web application for generating AI-powered resumes.  It takes a job description as input, compares it to a pre-existing resume (loaded from "resume.txt"), and generates a tailored resume in PDF format.  Key features include:

Resume Loading: Loads a resume from a local text file ("resume.txt").
Job Description Input: Allows users to paste a job description.
AI-Powered Generation: Uses OpenAI's API to generate a resume tailored to the job description, leveraging functions for prompt creation, resume generation, and JSON extraction.
Resume Matching and Analysis: Calculates a resume match score and provides analysis of keywords, missing skills, and suggestions for improvement.
PDF Generation: Generates an ATS-friendly PDF resume using the generated JSON data. Saves the PDF to the "PDFs" folder.
Saving Job Description and JSON: Saves the input job description to a text file in the "JDs" folder and the generated resume JSON to the "JSONs" folder.
Error Handling: Includes error handling for file loading, OpenAI API errors, and other exceptions, displaying informative messages to the user.
Streamlit Interface: Provides a user-friendly web interface with input fields, buttons, and output displays.


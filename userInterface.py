import streamlit as st
import os,json
import traceback
from typing import Dict, Any

# Import your existing functions
import openai
from score import get_resume_match_score
from utils import create_prompt, extract_json_from_text
from generateResume import generate_resume
from generatePDF import generate_ats_friendly_pdf
# from generateLatexPDF import generate_pdf_resume

def load_resume_from_file(file_path: str) -> str:
    """Load resume content from a text file."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        st.error(f"Error loading resume file: {str(e)}")
        return None

def validate_filename(filename: str) -> str:
    """Validate and format the filename."""
    # Remove any directory traversal attempts
    filename = os.path.basename(filename)
    
    # Add .pdf extension if not present
    if not filename.lower().endswith('.pdf'):
        filename += '.pdf'
    
    return filename

def main():
    st.title("AI Resume Generator")
    st.write("Upload a job description to generate a tailored resume")

    # Load resume content
    resume_path = "resume.txt"  # Update this with your resume file path
    resume_content = load_resume_from_file(resume_path)
    
    if resume_content is None:
        st.error("Failed to load resume file. Please check if 'resume.txt' exists.")
        return

    # Job description input
    job_description = st.text_area(
        "Enter Job Description",
        height=200,
        placeholder="Paste the job description here..."
    )

    # PDF filename input
    pdf_filename = st.text_input(
        "Enter PDF filename",
        value="resume",
        help="Enter the name for your generated PDF file (without .pdf extension)"
    )

    if st.button("Generate Resume"):
        if not job_description:
            st.warning("Please enter a job description")
            return

        if not pdf_filename:
            st.warning("Please enter a filename for the PDF")
            return

        try:
            with st.spinner("Analyzing job description and generating resume..."):
                # Create prompts
                system_prompt = create_prompt("prompts/generate_resume_prompt.txt")

                # Get resume match score and analysis
                result = get_resume_match_score(job_description, resume_content)
                
                # Generate new resume
                response = generate_resume(
                    system_prompt,
                    resume_content,
                    job_description,
                    "Expert",
                    'English',
                    result['keywords'],
                    result['suggestions'],
                    '.'.join(result['missing_skills'])
                )

                # Extract JSON from response
                resume_json = extract_json_from_text(response)

                # Validate and format the filename
                validated_filename = validate_filename(pdf_filename)
                pdf_path = os.path.join("PDFs", validated_filename)

                
                pdf_success = generate_ats_friendly_pdf(resume_json, pdf_path)

                if pdf_success:
                    st.success(f"Resume generated successfully! File saved as: {validated_filename}")
                    

                    # Save job description to "JDs" folder
                    jd_filename = validated_filename.replace(".pdf", ".txt")
                    jd_folder = "JDs"
                    os.makedirs(jd_folder, exist_ok=True)  # Create folder if it doesn't exist
                    jd_filepath = os.path.join(jd_folder, jd_filename)
                    
                    os.makedirs("JSONs", exist_ok=True)
                    json_filepath = os.path.join("JSONs", validated_filename.replace(".pdf", ".json"))

                    with open(jd_filepath, "w") as jd_file:
                        jd_file.write(job_description)
                    
                    with open(json_filepath, "w") as json_file:
                        json.dump(resume_json, json_file, indent=4)

                    # Display match analysis
                    st.subheader("Job Match Analysis")
                    st.write(f"Keywords found: {result['keywords']}")
                    st.write("Missing Skills:")
                    for skill in result['missing_skills']:
                        st.write(f"- {skill}")
                    st.write("Suggestions:")
                    st.write(result['suggestions'])
                else:
                    st.error("Failed to generate PDF. Please check the logs.")

        except openai.APIError as e:
            st.error(f"OpenAI API Error: {str(e)}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.code(traceback.format_exc())

if __name__ == "__main__":
    main()
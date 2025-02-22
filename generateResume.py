import openai
from resumePDF import create_pdf
# from generatePDF import generate_pdf
from score import get_resume_match_score
from utils import create_prompt, extract_json_from_text 


def generate_resume(prompt: str, resume_content: str, job_description,tone: str, language: str,
                        key_words: str = "", additional_info: str = None, missing_skills: str=None) -> str:
        """
        Generates a resume using OpenAI API.

        Parameters:
        ----------
        - prompt (str): Instruction for the AI model.
        - resume_content (str): The current resume content.
        - tone (str): Tone of the resume (e.g., professional, conversational).
        - language (str): Language of the resume.
        - key_words (str): Keywords extracted from the job description.
        - additional_info (str): Any additional information provided by the user.

        Returns:
        -------
        - str: The generated resume content.
        """
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"""
            User's Resume:
            {resume_content}
            Job Description:
            {job_description}
            Job Description Keywords:
            {key_words}
            Tone to be applied:
            {tone}
            Language of the new resume:
            {language}
            User's Additional Information:
            {additional_info}
            Missing skills:
            {missing_skills}
            """}
        ]

        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            max_tokens=4000
        )
        return response.choices[0].message.content
    

def extract_keywords_ai(prompt: str, job_description) -> str:
        """
        Extracts keywords from the job description using OpenAI API.

        Parameters:
        ----------
        - prompt (str): The prompt to extract keywords.

        Returns:
        -------
        - str: The extracted keywords as a string.
        """
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": job_description}
        ]

        response = openai.chat.completions.create(
            model='gpt-4o',
            messages=messages,
            max_tokens=600
        )

        # Return the response content directly or extract keywords from it
        return response.choices[0].message.content.strip()


# system_prompt = create_prompt("generate_resume_prompt.txt")
# keywords_prompt = create_prompt("keywords_prompt.txt")


# response = generate_resume(system_prompt,resume,"Expert", 'English', result['keywords'], result['suggestions'], '.'.join(result['missing_skills']))


# resume = extract_json_from_text(response)


# print(create_pdf(resume, "PDFs/weasy_resume.pdf", ['Experiences', 'Education', 'Skills', 'Projects'] , color_code="#000000"))
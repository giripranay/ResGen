import requests
from bs4 import BeautifulSoup
import openai, json
from utils import create_prompt, extract_json_from_text
import streamlit as st

# OpenAI API Key (replace with your key)
OPENAI_API_KEY = "your-api-key"


system_prompt = create_prompt("system_prompt.txt")


def extract_job_description(url):
    """Fetch full webpage text content"""
    headers = {"User-Agent": "Mozilla/5.0"}
    
    # Fetch page content
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return f"Failed to fetch page: {response.status_code}"

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract all visible text from the page
    full_text = soup.get_text(separator=" ", strip=True)
    
    return full_text



def extract_job_details(job_description):
    
    
    prompt = f"""
    Extract the following details from the job description below:
    1. Required skills (list of technologies & tools). Any technical term is considered as skill.
    2. Years of experience required
    3. **Is sponsorship available?** (Yes/No/Not mentioned).  
            - If the job description **implies** that only U.S. citizens or permanent residents are eligible (e.g., requires government clearance, mentions work authorization restrictions, or states permanent work eligibility), return **No** (not for F1/OPT EAD holders).  
            - If the job description **suggests openness** to candidates on a visa (e.g., mentions F1, OPT, EAD holders, or states willingness to sponsor), return **Yes**.  
            - If there’s no clear indication, return **Not mentioned**.
    4.Categorize the job into one of the following fields: Data Science, Cyber Security, Networking, Full Stack Development, Mobile App Development, Python Developer, Flutter Developer, or any other relevant field based on the job description.

    Job Description:
    {job_description}

    Output must be in **valid JSON format** with these exact keys:
    {{
    "required_skills": ["list of technologies & tools"],
    "years_of_experience_required": integer,
    "sponsorship_available": "Yes/No/Not mentioned",
    "category": String
    }}
    """

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content":system_prompt},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()



# # Example Usage:
# job_url = "https://algojobs.io/jobs/2977420"
# job_details = extract_job_details_from_url(job_url)
# print(job_details)

# 🚀 Streamlit UI
st.title("🔎 Job Description Analyzer")
st.write("Enter a **Job URL** or **Paste a Job Description** to extract details.")

# User Input
job_url = st.text_input("Enter Job Posting URL")
job_desc = st.text_area("Or Paste Job Description")

# Ensure at least one input is provided
if st.button("Analyze Job Details"):
    if not job_url and not job_desc:
        st.error("❌ Please enter either a Job URL or a Job Description!")
    else:
        with st.spinner("Extracting job details... ⏳"):
            if job_url:
                job_desc = extract_job_description(job_url)
            
            job_details = extract_json_from_text(extract_job_details(job_desc))
            print(job_details.keys())

            if "error" in job_details:
                st.error("❌ Error processing job details.")
            else:
                st.subheader("📌 Extracted Job Details")



                # Years of Experience
                st.markdown(f"**⏳ Years of Experience Required:** `{job_details['years_of_experience_required']}`")

                # Sponsorship
                sponsorship = job_details["sponsorship_available"]
                if sponsorship == "Yes":
                    st.markdown(f"**✅ Sponsorship Available:** ✔ Yes")
                elif sponsorship == "No":
                    st.markdown(f"**❌ Sponsorship Available:** ❌ No")
                else:
                    st.markdown(f"**❔ Sponsorship Available:** ℹ {sponsorship}")

                # Category
                st.markdown(f"**📂 Job Category:** `{job_details['category']}`")


                # Skills
                st.markdown("**🛠 Required Skills:**")
                for skill in job_details["required_skills"]:
                    st.markdown(f"- {skill}")

                
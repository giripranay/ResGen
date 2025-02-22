import streamlit as st
import json
from utils import extract_json_from_text, create_prompt
import openai

# OpenAI API Key
# OPENAI_API_KEY = "your-api-key"

def get_resume_match_score(job_description, resume):
    """Compares job description & resume using LLM and returns a match score."""
    
    score_prompt = create_prompt("prompts/score_prompt.txt")
    prompt = f"""
    Job Description:
    {job_description}

    Resume:
    {resume}
    """

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": score_prompt},
                  {"role": "user", "content": prompt}]
    )

    try:
        return extract_json_from_text(response.choices[0].message.content)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response from LLM"}


# # 🚀 Streamlit UI
# st.title("📄 Resume Match Score Analyzer")
# st.write("Paste a **Job Description** and **Resume**, then get an AI-powered **match score**!")

# # Input Fields
# job_description = st.text_area("📌 Paste Job Description Here")
# resume = st.text_area("📝 Paste Resume Here")

# # Ensure both fields are filled before proceeding
# if st.button("Analyze Match Score"):
#     if not job_description or not resume:
#         st.error("❌ Please enter both the Job Description and Resume!")
#     else:
#         with st.spinner("Processing... ⏳"):
#             result = get_resume_match_score(job_description, resume)
            
#             if "error" in result:
#                 st.error("❌ Error processing the match score.")
#             else:
#                 st.subheader("✅ Match Score Results")

#                 # Display Score
#                 st.markdown(f"**📊 Match Score:** `{result['score']}%`")

#                 # Display Suggestions
#                 st.markdown(f"**💡 Suggestions:** {result['suggestions']}")

#                 # Display Missing Skills
#                 if result["missing_skills"]:
#                     st.markdown("**🛠 Missing Skills:**")
#                     for skill in result["missing_skills"]:
#                         st.markdown(f"- {skill}")

#                 # Display Missing Skills
#                 if result["keywords"]:
#                     st.markdown("**🛠 Keywords:**")
#                     for keyword in result["keywords"]:
#                         st.markdown(f"- {keywords}")
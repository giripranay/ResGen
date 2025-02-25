# ResGen: AI-Powered Resume Generation 🚀

ResGen (Resume Generation) is a project that helps you create and customize your resumes. It uses AI to look at job descriptions and your current resume, then makes a new resume that focuses on the most important skills and experience.  This new resume is designed to be easily read by computer systems used by companies to manage job applications. This project was inspired by and gives credit to MyResumo by AnalyticAce.

## Project Description

The main idea behind project is to generate tailored resume based on job description and your current resume. We leverage the power LLMs to accomplish this task.

## Key Features

*   **Intelligent Keyword Identification:**  ResGen analyzes the job description to pinpoint crucial keywords and seamlessly integrates them into your resume.
*   **Dynamic Work Experience Generation:**  Creates work experience entries that are specifically tailored to the target job, highlighting relevant accomplishments and responsibilities.
*   **Dynamic Project Generation:**  Generates project descriptions that align with the job requirements, showcasing your skills and experience in a compelling way.
*   **Work Experience Modification:**  Adapts your existing work experience descriptions to better match the language and requirements of the job posting.
*   **Latest Work Experience Alignment:**  Ensures your most recent experience is presented in a way that directly addresses the needs of the potential employer.
*   **ATS-Friendly PDF Generation:**  Generates a polished, ATS-compliant PDF resume that is optimized for Applicant Tracking Systems.

## Workflow

1.  **Analysis:** ResGen analyzes the job description and your resume, identifying important keywords, and providing suggestions for tailoring your resume using LLMs (specifically OpenAI's ChatGPT-4).
2.  **Resume Generation:** The identified keywords, suggestions, job description, and your resume are used as input to generate a final resume in JSON format.
3.  **PDF Generation:** A professional PDF resume is generated from the JSON output.

## File Descriptions

*   `score.py`: Generates the "score," "missing\_skills," "keywords," and "suggestions" using the LLM.
*   `generateResume.py`: Generates the tailored resume in JSON format.
*   `prompts/`: Contains the prompts used for LLM interaction.
*   `JDs/`: Stores job descriptions as text files (filename: company name).
*   `PDFs/`: Stores the generated PDF resumes (filename: company name).
*   `resume.txt`: Your current resume in plain text format.
*   `requirements.txt`: Lists the project dependencies for setting up the virtual environment.
*   `userInterface.py`: The Streamlit application for the interactive resume generation process.

## Getting Started

1.  **Clone the Repository:**

    ```bash
    git clone [https://github.com/giripranay/YOUR_REPO_NAME.git](https://www.google.com/search?q=https://github.com/giripranay/YOUR_REPO_NAME.git)  # Replace with your repo URL
    ```

2.  **Create a Virtual Environment:**

    ```bash
    python3 -m venv .venv  # Create the virtual environment
    source .venv/bin/activate  # Activate the virtual environment (Linux/macOS)
    .venv\Scripts\activate  # Activate the virtual environment (Windows)
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit App:**

    ```bash
    streamlit run userInterface.py
    ```

5.  **Configure OpenAI API Key:**

    Set your OpenAI API key as an environment variable named `OPENAI_API_KEY`.

## Usage

1.  Prepare your current resume and save it as `resume.txt` in the project directory.
2.  Run the Streamlit app (`streamlit run userInterface.py`).
3.  Paste the job description into the input area.
4.  Enter the desired filename for the PDF.
5.  Click "Generate Resume."

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

[Choose a License - e.g., MIT License]

## Acknowledgements

*   Inspired by and gives credit to [MyResumo](https://github.com/AnalyticAce/MyResumo) by AnalyticAce.
*   Powered by OpenAI.

## Hashtags

#AIResume #ResumeGenerator #JobSearch #LLM #ChatGPT #OpenAI #Career #JobHunt #ATS #ResumeTips #ArtificialIntelligence #Innovation #Tech #Hiring #JobApplication #ResGen

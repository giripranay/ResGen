# utils.py
import re, json

def read_file(file_path: str) -> str:
    """Reads a file and returns its content."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def create_prompt(filename: str) -> str:
    """Creates a prompt from a file.
    
    Parameters:
    ----------
        filename (str): The path to the file.
        
    Returns:
    -------
        str: The prompt.
    """
    prompt = read_file(filename)
    template = f"""
    {prompt}
    """
    return template


def extract_json_from_text(text):
    """Extracts valid JSON from a mixed LLM response using regex."""
    match = re.search(r"\{.*\}", text, re.DOTALL)  # Find JSON in response
    if match:
        try:
            return json.loads(match.group(0))  # Convert to Python dict
        except json.JSONDecodeError:
            return {"error": "Extracted JSON is invalid"}
    return {"error": "No valid JSON found"}
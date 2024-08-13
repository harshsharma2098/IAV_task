## Welcome to my project.

### The project consists of two parts:
1. First part where a page displays my CV.
2. Second part where I have integerated a LLM API (Llama-3.1-70b-versatile)

### To use the API follow the mentioned instructions:
1. Create an account on "groq.com".
2. Go to "Developer Playground" under "Start building" and create an API key.

### Run the following command to install necessary dependencies:
pip install -r requirements.txt

### Run the following command to setup groq environment using API key:
export GROQ_API_KEY=" YOUR UNIQUE API KEY " (In case of windows system use "set" instead of "export")

### Run the following command to run script:
streamlit run app.py
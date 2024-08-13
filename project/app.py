import streamlit as st
import base64
from groq import Groq

# Groq client initialization
client = Groq()

# Page 1: Welcome Page
def welcome_page():
    st.title('Welcome to My Project')
    st.write("""
        Welcome to my project! This application includes three sections:
        1. A welcome page.
        2. My CV displayed as a PDF.
        3. A joke generator powered by a language model.
        Use the sidebar to navigate between these sections.
    """)

# Page 2: Display CV as PDF
def show_cv():
    st.title('My CV')

    def show_pdf(file_path):
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

    show_pdf('project/data/Harsh_CV_Latest_de.pdf')

# Page 3: Generate a Joke
def generate_joke():
    st.title('Joke Generator')

    prompt = st.text_input("Ask for joke here")
    completion = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
    )
    joke_lis = list()
    for chunk in completion:
        word = chunk.choices[0].delta.content
        if word == None:
            pass
        else:
            joke_lis.append(word)
    
    joke = ' '.join(joke_lis)
    st.write(joke)





# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Welcome", "Show CV", "Generate Joke"])

# Page navigation
if page == "Welcome":
    welcome_page()
elif page == "Show CV":
    show_cv()
elif page == "Generate Joke":
    generate_joke()



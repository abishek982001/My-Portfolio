import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Set page configuration
st.set_page_config(page_title="Portfolio", page_icon=":briefcase:", layout="wide")

# Function to load Lottie animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load CSS for styling (if any)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Optional CSS file for custom styles
# Uncomment the next line if you have a "style.css" file
local_css("style/style.css")

# Load assets
lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/private_files/lf30_m075yjya.json")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Abishek R :wave:")
    st.title("A Machine Learning Enthusiast")
    st.write(
        "Welcome to my portfolio! Here, you'll find details about my projects, skills, and contact information."
    )
    st.write("[Learn More on GitHub >](https://github.com/abishek982001)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write(
        """
           I am a passionate and dedicated tech professional, currently working as an SAP BODS Developer at Ford, where I focus on optimizing data integration and ETL processes.\n
           Previously, as a Software Developer, I specialized in upgrading Spring Boot 2.x to 3.x, writing robust test cases, and ensuring top-notch code quality using tools like Checkmarx, FOSSA, and SonarQube. This experience honed my skills in software development, code standardization, and process improvement.\n
           In my current role, I leverage this foundation to streamline data workflows, automate processes, and drive business outcomes. My journey reflects a commitment to continuous learning, innovation, and making meaningful contributions to projects.\n
           Let's connect to collaborate, share ideas, and explore new opportunities in the tech landscape!
        """
        )

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS SECTION ----
with st.container():
    st.header("My Projects")
    # Updated project list with Streamlit-friendly emojis
    project_list = [
        {
            "title": "Smart Attendance System",
            "description": "Face Recognition project with a time-stamp intended for attendance purposes.",
            "tools": "Python, OpenCV, Numpy, OS",
            "github_link": "https://github.com/abishek982001/Face-Recognition",
            "emoji": ":bust_in_silhouette:",  # Face-related emoji
        },
        {
            "title": "Real-Time Object Measurement Tool",
            "description": "Python project to measure the perimeter of objects fitting within a given frame.",
            "tools": "Python, OpenCV, Numpy, OS",
            "github_link": "https://github.com/abishek982001/Real-Time-Object-Measurement",
            "emoji": ":straight_ruler:",  # Measurement-related emoji
        },
        {
            "title": "Image-to-Text Speech Converter",
            "description": "Detect texts from images by letters or words and convert them to speech.",
            "tools": "Python, OpenCV, IO, Tesseract, Pygame",
            "github_link": "https://github.com/abishek982001/Image-Text-Detector",
            "emoji": ":page_facing_up:",  # Text-related emoji
        },
        {
            "title": "Predictive Analysis with Linear Regression",
            "description": "Predict sales, housing prices, and per capita income using Kaggle datasets.",
            "tools": "Python, Numpy, sklearn",
            "github_link": "https://github.com/abishek982001/Banglore-House-Price-Prediction",
            "emoji": ":bar_chart:",  # Prediction/data-related emoji
        },
    ]

     # Display projects in a 2-column layout
    for i in range(0, len(project_list), 2):
        cols = st.columns(2)  # Create two columns for each row
        
        # First project in the row
        with cols[0]:
            project = project_list[i]
            st.subheader(f"{project['emoji']} {project['title']}")
            st.write(project["description"])
            st.write(f"**Technologies Used:** {project['tools']}")
            st.write(f"[GitHub Link]({project['github_link']})")
        
        # Second project in the row, if it exists
        if i + 1 < len(project_list):
            with cols[1]:
                project = project_list[i + 1]
                st.subheader(f"{project['emoji']} {project['title']}")
                st.write(project["description"])
                st.write(f"**Technologies Used:** {project['tools']}")
                st.write(f"[GitHub Link]({project['github_link']})")



# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/903f019b6041adfa3d2a4eda644facd4" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

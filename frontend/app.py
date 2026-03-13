import streamlit as st
import requests


# CONFIG


BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Slide Tutor",
    page_icon="📚",
    layout="wide"
)


# CUSTOM CSS


st.markdown("""
<style>

.main-title{
font-size:45px;
font-weight:700;
text-align:center;
color:#4CAF50;
}

.subtitle{
text-align:center;
font-size:18px;
color:gray;
margin-bottom:20px;
}

.slide-card{
background:white;
padding:30px;
border-radius:12px;
box-shadow:0px 6px 20px rgba(0,0,0,0.08);
margin-top:20px;
}

.slide-title{
font-size:30px;
font-weight:700;
color:#2c3e50;
}

.slide-content{
font-size:18px;
margin-top:15px;
color:#333;
}

.example-box{
background:#eef6ff;
padding:15px;
border-radius:10px;
margin-top:15px;
font-size:16px;
}

.ai-box{
background:#e8f5e9;
padding:18px;
border-radius:10px;
margin-top:15px;
font-size:16px;
}

</style>
""", unsafe_allow_html=True)


# TITLE


st.markdown('<p class="main-title">📚 AI Slide Tutor</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Learn Science & Mathematics concepts with AI-generated slides</p>', unsafe_allow_html=True)


# SESSION STATE


if "slides" not in st.session_state:
    st.session_state.slides = []

if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

if "topic" not in st.session_state:
    st.session_state.topic = ""


# SIDEBAR


st.sidebar.title("📘 Generate Lesson")

topic = st.sidebar.text_input("Topic")

grade = st.sidebar.selectbox(
    "Grade",
    ["Not specified",1,2,3,4,5,6,7,8,9,10,11,12]
)

generate = st.sidebar.button("Generate Lesson")


# GENERATE LESSON


if generate:

    if topic == "":
        st.warning("Please enter a topic.")

    else:

        with st.spinner("Generating lesson..."):

            payload = {
                "topic": topic,
                "grade": None if grade == "Not specified" else grade
            }

            try:

                response = requests.post(
                    f"{BACKEND_URL}/generate-lesson",
                    json=payload
                )

                data = response.json()

                if "slides" in data:

                    st.session_state.slides = data["slides"]
                    st.session_state.slide_index = 0
                    st.session_state.topic = topic

                else:

                    st.error("Backend Error")
                    st.write(data)

            except Exception as e:

                st.error("Backend connection failed")
                st.write(e)


# DISPLAY SLIDES


if st.session_state.slides:

    slides = st.session_state.slides
    index = st.session_state.slide_index

    slide = slides[index]

    # progress bar
    progress = (index + 1) / len(slides)
    st.progress(progress)

    st.markdown(
        f"""
        <div class="slide-card">

        <div class="slide-title">{slide['title']}</div>

        <div class="slide-content">
        {slide['content']}
        </div>

        <div class="example-box">
        <b>Example:</b> {slide['example']}
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    
    # NAVIGATION
    

    col1, col2, col3 = st.columns([1,2,1])

    with col1:

        if st.button("⬅ Previous"):

            if index > 0:
                st.session_state.slide_index -= 1

    with col3:

        if st.button("Next ➡"):

            if index < len(slides) - 1:
                st.session_state.slide_index += 1

    st.markdown(
        f"<center><b>Slide {index+1} of {len(slides)}</b></center>",
        unsafe_allow_html=True
    )

    
    # DOUBT SECTION
    

    st.divider()

    st.subheader("❓ Ask the AI Tutor")

    question = st.text_input("Type your question")

    ask = st.button("Ask AI Tutor")

    if ask:

        if question == "":

            st.warning("Please enter a question.")

        else:

            with st.spinner("Thinking..."):

                payload = {
                    "topic": st.session_state.topic,
                    "context": slide["content"],
                    "question": question
                }

                try:

                    response = requests.post(
                        f"{BACKEND_URL}/solve-doubt",
                        json=payload
                    )

                    data = response.json()

                    st.markdown(
                        f"""
                        <div class="ai-box">
                        🤖 <b>AI Tutor</b><br><br>
                        {data["answer"]}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                except Exception as e:

                    st.error("Error contacting backend")
                    st.write(e)
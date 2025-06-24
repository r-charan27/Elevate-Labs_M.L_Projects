# AI Career Counsellor Chatbot with Voice Input, TTS, and Multilingual Support

import streamlit as st
from textblob import TextBlob
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os
import base64
import speech_recognition as sr
import tempfile

st.set_page_config(page_title="AI Career Counsellor")
st.title("🎓 AI Virtual Career Counsellor")
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
# ✅ Background
def set_background(local_img_path):
    with open(local_img_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
        }}
        </style>
    """, unsafe_allow_html=True)
set_background("C:/Users/RAMCHARAN/Downloads/Get more value from your favorite tools with Chatbot.jpg")
# Text-to-speech function using gTTS
def speak(text):
    tts = gTTS(text)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        temp_filename = fp.name
    tts.save(temp_filename)
    playsound(temp_filename)
    os.remove(temp_filename)

# Voice input function
def record_voice_input():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        st.info("🎤 Listening... Please speak your career interests.")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        st.success(f"✅ You said: {text}")
        return text
    except sr.UnknownValueError:
        st.error("❌ Sorry, could not understand your voice.")
    except sr.RequestError:
        st.error("❌ Speech recognition service is unavailable.")
    return ""

# Career learning paths and recommendations
career_advice = {
    "technology": {
        "advice": "You can explore careers in software development, AI/ML, data science, or cybersecurity.",
        "skills": ["Python", "Machine Learning", "Problem Solving"],
        "resources": [
            "YouTube: Python for Beginners",
            "Course: Google's Machine Learning Crash Course",
            "Platform: HackerRank"
        ]
    },
    "arts": {
        "advice": "You can explore careers in fine arts, animation, graphic design, or content creation.",
        "skills": ["Creativity", "Design Tools", "Color Theory"],
        "resources": ["YouTube: Art for Beginners", "Course: Canva Design School"]
    },
    "commerce": {
        "advice": "You can explore careers in finance, accounting, marketing, or business analysis.",
        "skills": ["Excel", "Accounting", "Presentation Skills"],
        "resources": ["Course: Google Data Analytics", "YouTube: Learn Excel"]
    },
    "medical": {
        "advice": "You can explore careers in medicine, doctor, physiotherapy, or medical research.",
        "skills": ["Biology", "Empathy", "Teamwork"],
        "resources": ["Course: Anatomy 101", "YouTube: NEET Prep"]
    },
    "law": {
        "advice": "You can explore careers as a lawyer, legal advisor, or in corporate law.",
        "skills": ["Logical Reasoning", "Debate", "Reading"],
        "resources": ["YouTube: Law School 101", "Course: Legal Studies on edX"]
    }
}

# Personality quiz scoring
st.subheader("Personality Quiz")
personality_score = 0
q1 = st.radio("Do you enjoy solving logical problems?", ["Yes", "No"])
q2 = st.radio("Do you prefer working with people over machines?", ["Yes", "No"])
q3 = st.radio("Are you more creative or analytical?", ["Creative", "Analytical"])

if q1 == "Yes": personality_score += 2
if q2 == "Yes": personality_score += 1
if q3 == "Creative": personality_score += 1

# Determine personality direction
if personality_score >= 4:
    default_path = "technology"
elif personality_score == 3:
    default_path = "commerce"
elif personality_score == 2:
    default_path = "arts"
else:
    default_path = "law"

st.markdown(f"Based on your quiz, you might be suited for: **{default_path.title()}**")

# Choose input method
type_choice = st.selectbox("Choose input method:", ["Type", "Speak"])
translator = Translator()

if type_choice == "Type":
    text_input = st.text_input("Type in any language:")
    if text_input:
        try:
            st.session_state["user_input"] = translator.translate(text_input, dest='en').text
            st.session_state["speak_now"] = True
        except:
            st.error("Translation failed.")
            st.session_state["user_input"] = ""
            st.session_state["speak_now"] = False
elif type_choice == "Speak":
    if st.button("🎙️ Start Voice Input"):
        voice_input = record_voice_input()
        if voice_input:
            st.session_state["user_input"] = voice_input
            st.session_state["speak_now"] = True

# Sentiment analysis
def analyze_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity < -0.3:
        return "I sense some confusion. Let's take it step-by-step."
    elif polarity > 0.3:
        return "You sound enthusiastic! That's great."
    else:
        return "Got it. Let's explore your options."

# Career suggestion engine
def get_career_advice(text):
    text = text.lower()
    if any(keyword in text for keyword in ["tech", "coding", "computers", "software"]):
        return "technology"
    elif any(keyword in text for keyword in ["drawing", "painting", "design", "art"]):
        return "arts"
    elif any(keyword in text for keyword in ["business", "commerce", "finance", "accounts"]):
        return "commerce"
    elif any(keyword in text for keyword in ["biology", "doctor", "medicine", "health"]):
        return "medical"
    elif any(keyword in text for keyword in ["law", "justice", "court"]):
        return "law"
    else:
        return default_path

# Process user input from session state
if "user_input" in st.session_state and st.session_state["user_input"]:
    user_input = st.session_state["user_input"]
    sentiment = analyze_sentiment(user_input)
    st.markdown(f"🧠 **Sentiment Insight:** {sentiment}")

    suggestion = get_career_advice(user_input)
    advice = career_advice[suggestion]

    st.markdown(f"**🤖 Counsellor:** {advice['advice']}")
    st.markdown("**📚 Recommended Skills:**")
    st.write(", ".join(advice['skills']))
    st.markdown("**🎓 Learning Resources:**")
    for res in advice['resources']:
        st.write(f"- {res}")

    if st.session_state.get("speak_now", False):
        speak(advice['advice'])
        st.session_state["speak_now"] = False

import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="AI-powered Text Analyzer", page_icon=":rocket:", layout="centered")

st.title("🚀 AI-powered Text Analyzer")
st.markdown("""
Welcome to your own AI-powered Text Analyzer!  
Paste any text below and choose what you want to do with it:
- **Summarize** the text
- **Translate** to Spanish
- **Analyze Sentiment** (positive, negative, neutral)
""")

st.write("---")

# Text input
user_input = st.text_area("Paste your text here 👇", height=200)

# Option select
option = st.selectbox(
    "Choose an analysis type:",
    ("Summarize", "Translate to Spanish", "Analyze Sentiment")
)

st.write("---")

def summarize(text):
    # Simple extractive summary: show 2 longest sentences
    import re
    sentences = re.split(r'(?<=[.!?]) +', text)
    sentences = sorted(sentences, key=len, reverse=True)
    return " ".join(sentences[:2]) if sentences else ""

def translate_to_spanish(text):
    blob = TextBlob(text)
    try:
        return str(blob.translate(to='es'))
    except Exception as e:
        return f"Error translating: {e}"

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        sentiment = "Positive 😀"
    elif polarity < -0.2:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"
    return f"Sentiment Score: {polarity:.2f} ({sentiment})"

# Analyze button
if st.button("Analyze!"):
    if not user_input.strip():
        st.warning("Please paste some text to analyze!")
    else:
        if option == "Summarize":
            st.subheader("📝 Summary")
            st.success(summarize(user_input))
        elif option == "Translate to Spanish":
            st.subheader("🌐 Translation")
            st.info(translate_to_spanish(user_input))
        elif option == "Analyze Sentiment":
            st.subheader("💡 Sentiment Analysis")
            st.code(analyze_sentiment(user_input))

st.write("---")
st.caption("Made with Streamlit and 💙 by Sergio Man")

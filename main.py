import streamlit as st
import pandas as pd

# Page Configurations
st.set_page_config(page_title="🤖 AI Assistant & Conversions", layout="wide")

# Custom CSS for Modern UI
st.markdown("""
    <style>
        .stApp {
            background-color: #0e1117;
            color: white;
        }
        .title {
            font-size: 28px;
            font-weight: bold;
            text-align: center;
            color: #00c3ff;
        }
        .subtitle {
            font-size: 20px;
            text-align: center;
            color: #FFD700;
        }
        .container {
            padding: 20px;
            border-radius: 10px;
            background-color: #1e2127;
            box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.1);
            margin-bottom: 20px;
        }
        .button {
            background-color: #00c3ff;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title & Description
st.markdown("<h1 class='title'>🤖 AI Assistant & Units Converter</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>📚 Ask anything to AI or explore unit conversions</p>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar for Navigation
mode = st.sidebar.radio("🔍 Select Mode:", ["AI Assistant", "Units & Conversions Table"])

# AI Assistant Section
if mode == "AI Assistant":
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.subheader("💬 Chat with AI")
    user_query = st.text_area("Ask your question:", placeholder="Type your question here...", height=100)

    if st.button("🚀 Get Answer"):
        if user_query:
            # Placeholder function (Replace with actual AI API like OpenAI or Gemini)
            def ask_gemini(query):
                return f"🤖 AI says: '{query}' is an interesting question! Implement API for real responses."

            ai_response = ask_gemini(user_query)
            st.success(ai_response)
        else:
            st.error("⚠️ Please enter a question.")

# Units & Conversions Table
elif mode == "Units & Conversions Table":
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.subheader("📏 Common Units & Conversions")

    # DataFrame for better UI
    conversion_data = {
        "Category": ["Length", "Length", "Weight", "Weight", "Temperature", "Temperature", "Volume", "Volume"],
        "Conversion": ["1 meter = 3.281 feet", "1 kilometer = 0.621 miles", 
                       "1 kilogram = 2.205 pounds", "1 gram = 0.035 ounces",
                       "0°C = 32°F", "100°C = 212°F",
                       "1 liter = 4.227 cups", "1 gallon = 3.785 liters"]
    }
    
    df = pd.DataFrame(conversion_data)
    st.table(df)

# Footer
st.markdown("---")
st.markdown("🚀 Developed by *Zaryab Irfan* | Powered by *Gemini AI & Streamlit*", unsafe_allow_html=True)


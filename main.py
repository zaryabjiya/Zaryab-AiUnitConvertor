import streamlit as st
import random
import pint
import google.generativeai as genai
from dotenv import load_dotenv
import os

# **🔑 Load API Key**
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# **📏 Initialize Unit Converter**
ureg = pint.UnitRegistry()

# **🎨 Custom CSS – Futuristic Neon UI**
st.markdown("""
    <style>
        @keyframes glow {0% {box-shadow: 0px 0px 15px #00fff2;} 50% {box-shadow: 0px 0px 30px #ff00ff;} 100% {box-shadow: 0px 0px 15px #00fff2;}}
        .stApp {background: linear-gradient(45deg, #001f3f, #6600cc, #002f6c); padding: 30px; border-radius: 20px; animation: glow 2s infinite alternate;}
        h1 {text-align: center; font-size: 42px; color: #ffcc00; font-weight: bold; text-shadow: 0px 0px 10px #fff;}
        .stButton>button {background: linear-gradient(45deg, #00ffff, #ff00ff); color: white; font-size: 22px; padding: 15px 30px; border-radius: 15px; transition: 0.3s; animation: glow 2s infinite alternate;}
        .stButton>button:hover {transform: scale(1.15); background: linear-gradient(45deg, #ff0066, #00ff99);}
        .result-box {font-size: 26px; font-weight: bold; text-align: center; background: rgba(255, 255, 255, 0.15); padding: 20px; border-radius: 14px; box-shadow: 0px 6px 20px rgba(255, 255, 255, 0.3);}
        .ai-msg {text-align: center; font-size: 20px; font-weight: bold; color: #ffcc00; margin-top: 15px;}
    </style>
""", unsafe_allow_html=True)

# **🎙️ AI Predictions + Funny Messages**
ai_suggestions = [
    "Last time tumne Meters to Feet convert kiya tha! 🤓",
    "AI Tip: Ounces se Grams convert karna bohot useful hota hai! 💡",
    "Celsius to Fahrenheit? 🥵 Ya cold kaafi lag rahi hai? 🥶",
    "AI Suggestion: Tumhe kg se pounds convert karna pasand hai! 😂",
    "Kya tum ek scientist ho? Kelvin se Celsius kar rahe ho! 🧪"
]

funny_responses = [
    "Conversion complete! Ab to tum genius lag rahe ho! 🤓",
    "Converted! Ab NASA ka job apply kar lo! 🚀",
    "Tumne itni conversions kar li, ab mujhe bhi convert kar lo! 🤖",
    "Bas karo yaar! Ab AI bhi thak gaya! 😂",
    "Conversion done! Ab mujhe bhi chutti do! 😆"
]

# **🟢 App Heading**
st.markdown("<h1> 🤖 AI-Powered Unit Converter 🎙️🚀 </h1>", unsafe_allow_html=True)
st.markdown(f"<div class='ai-msg'>{random.choice(ai_suggestions)}</div>", unsafe_allow_html=True)

# **🔄 Choose Mode**
mode = st.sidebar.radio("Choose Mode:", ["Unit Converter", "AI Assistant", "Units & Conversion Table"])

# **📏 Unit Converter**
if mode == "Unit Converter":
    st.subheader("📏 Unit Converter")
    
    conversion_type = st.sidebar.selectbox("🔄 Choose Conversion Type", ["📏 Length", "⚖️ Weight", "🌡 Temperature"])
    value = st.number_input("🔢 Enter Value", value=0.0, min_value=0.0, step=0.1)

    col1, col2 = st.columns(2)

    # **Dropdown Selection**
    if conversion_type == "📏 Length":
        with col1:
            from_unit = st.selectbox("🎯 From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
        with col2:
            to_unit = st.selectbox("🎯 To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    elif conversion_type == "⚖️ Weight":
        with col1:
            from_unit = st.selectbox("💪 From", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])
        with col2:
            to_unit = st.selectbox("💪 To", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])
    elif conversion_type == "🌡 Temperature":
        with col1:
            from_unit = st.selectbox("🔥 From", ["Celsius", "Fahrenheit", "Kelvin"])
        with col2:
            to_unit = st.selectbox("🔥 To", ["Celsius", "Fahrenheit", "Kelvin"])

    # **🚀 Convert Button**
    if st.button("🎯 Convert Now 🚀"):
        try:
            if conversion_type == "🌡 Temperature":
                # **Temperature Conversion Logic**
                if from_unit == "Celsius" and to_unit == "Fahrenheit":
                    result = (value * 9/5) + 32
                elif from_unit == "Celsius" and to_unit == "Kelvin":
                    result = value + 273.15
                elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                    result = (value - 32) * 5/9
                elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                    result = (value - 32) * 5/9 + 273.15
                elif from_unit == "Kelvin" and to_unit == "Celsius":
                    result = value - 273.15
                elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                    result = (value - 273.15) * 9/5 + 32
                else:
                    result = value  # Same unit conversion
                
            else:
                # **General Unit Conversion Using Pint**
                result = (value * ureg(from_unit.lower())).to(to_unit.lower()).magnitude

            st.markdown(f"<div class='result-box'>✅ {value} {from_unit} = {result:.4f} {to_unit} 🎉</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='ai-msg'>{random.choice(funny_responses)}</div>", unsafe_allow_html=True)
        except Exception:
            st.error("Invalid conversion. Please check unit names.")

# **🤖 AI Assistant**
elif mode == "AI Assistant":
    st.subheader("🤖 AI Chat Assistant")
    user_query = st.text_area("Ask anything:", placeholder="Type your question here...")

    if st.button("Get Answer"):
        if user_query:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(user_query)
            st.success(response.text if response else "Error fetching response")
        else:
            st.error("Please enter a question.")

# **📌 Units & Conversion Table**
elif mode == "Units & Conversion Table":
    st.subheader("📌 Common Units & Conversions")
    conversion_data = {
        "📏 Length": ["1 meter = 3.281 feet", "1 kilometer = 0.621 miles"],
        "⚖️ Weight": ["1 kilogram = 2.205 pounds", "1 gram = 0.035 ounces"],
        "🌡 Temperature": ["0°C = 32°F", "100°C = 212°F"],
        "🛢 Volume": ["1 liter = 4.227 cups", "1 gallon = 3.785 liters"],
    }

    for category, conversions in conversion_data.items():
        with st.expander(category):
            for conversion in conversions:
                st.write(conversion)

# **⚡ Footer**
st.markdown("---")
st.markdown("🚀 Developed by Your Name | Powered by Gemini AI & Streamlit")
    

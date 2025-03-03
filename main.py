import streamlit as st
import pint
import google.generativeai as genai
import os
from dotenv import load_dotenv

# 🔹 Load API key for Gemini AI
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)

# 🔹 Initialize Pint for unit conversion
ureg = pint.UnitRegistry()

# 🚀 Function: Convert Units
def convert_units(value, from_unit, to_unit):
    try:
        result = (value * ureg(from_unit)).to(to_unit)
        return f"🎯 {value} {from_unit} = {result}"
    except pint.DimensionalityError:
        return "❌ Invalid unit conversion! Please check units."
    except Exception:
        return "⚠️ Error: Enter a valid number and correct unit names."

# 🤖 Function: AI Assistant Response
def get_ai_response(prompt):
    try:
        if api_key:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            return response.text if response else "⚠️ No response from AI!"
        else:
            return "❌ API Key not found! Set it up in .env file."
    except Exception as e:
        return f"🚨 AI Error: {str(e)}"

# 🌟 Streamlit App Configuration
st.set_page_config(
    page_title="🧮 Smart Unit Converter & AI Assistant", 
    page_icon="🔢", 
    layout="wide"
)

# 🎨 Sidebar Design
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3074/3074350.png", width=100)
st.sidebar.title("🔧 **Options Panel**")
mode = st.sidebar.radio("📌 Select a Feature:", ["📏 Unit Conversion", "💡 AI Assistant", "📚 Quick Conversion Guide"])

# 🎯 Title
st.markdown("<h1 style='text-align:center;'>🧮 Smart Unit Converter & AI Bot 🤖</h1>", unsafe_allow_html=True)
st.write("🚀 *Easily convert units & get instant AI assistance!*")

# 📏 **UNIT CONVERSION SECTION**
if mode == "📏 Unit Conversion":
    st.subheader("📐 **Unit Converter** 🔄")

    col1, col2, col3 = st.columns(3)

    with col1:
        value = st.text_input("🔢 Enter Value:", placeholder="e.g., 25")

    with col2:
        from_unit = st.text_input("📏 Convert From:", placeholder="e.g., inches")

    with col3:
        to_unit = st.text_input("🔄 Convert To:", placeholder="e.g., centimeters")

    if st.button("🚀 Convert Now", use_container_width=True):
        if value and from_unit and to_unit:
            try:
                value = float(value)
                result = convert_units(value, from_unit, to_unit)
                st.success(result)
            except ValueError:
                st.error("❌ Invalid number format!")
        else:
            st.warning("⚠️ Fill all fields before converting.")

# 💡 **AI ASSISTANT SECTION**
elif mode == "💡 AI Assistant":
    st.subheader("🤖 **Ask AI Anything!** 🧠")

    user_question = st.text_area("💬 Type your query below:", placeholder="E.g., How does AI work?")

    if st.button("🚀 Get Answer", use_container_width=True):
        if user_question:
            ai_answer = get_ai_response(user_question)
            st.success(f"🤖 AI Response: {ai_answer}")
        else:
            st.error("⚠️ Please enter a question.")

# 📚 **CONVERSION REFERENCE TABLE**
elif mode == "📚 Quick Conversion Guide":
    st.subheader("📘 **Quick Unit Conversion Guide**")

    conversions = {
        "📏 Length": ["1 meter = 3.281 feet", "1 mile = 1.609 km"],
        "⚖️ Weight": ["1 kg = 2.205 pounds", "1 gram = 0.035 ounces"],
        "🌡️ Temperature": ["0°C = 32°F", "100°C = 212°F"],
        "🧪 Volume": ["1 liter = 4.227 cups", "1 gallon = 3.785 liters"],
    }

    for category, values in conversions.items():
        with st.expander(f"{category}"):
            for conversion in values:
                st.write(f"✅ {conversion}")

# 🔻 Footer
st.markdown("---")
st.markdown("<h4 style='text-align:center;'>🚀 Created by *Zaryab Irfan* | Powered by AI & Streamlit</h4>", unsafe_allow_html=True)
            

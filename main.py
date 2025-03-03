import streamlit as st
import pint
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Environment variables load karna
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Gemini AI ko configure karna
if api_key:
    genai.configure(api_key=api_key)

# Pint library ka setup unit conversion ke liye
ureg = pint.UnitRegistry()

# Function: Unit Conversion
def convert_units(value, from_unit, to_unit):
    try:
        result = (value * ureg(from_unit)).to(to_unit)
        return f"{value} {from_unit} = {result}"
    except pint.DimensionalityError:
        return "❌ Invalid unit conversion!"
    except Exception:
        return "⚠️ Please enter valid numbers and unit names."

# Function: AI Assistant (Gemini AI)
def ask_gemini(prompt):
    try:
        if api_key:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            return response.text if response else "⚠️ No response from AI!"
        else:
            return "❌ API Key not found! Please configure it."
    except Exception as e:
        return f"🚨 AI Error: {str(e)}"

# Streamlit App Configuration
st.set_page_config(page_title="🔄 Universal Unit Converter", page_icon="♾️", layout="wide")

# Sidebar Options
st.sidebar.title("⚙️ Options")
mode = st.sidebar.radio("Choose a Mode:", ["📏 Unit Converter", "🤖 AI Assistant", "📚 Conversion Table"])

st.title("♾️ Universal Unit Converter & AI Assistant")
st.write("Easily convert units and get AI-powered responses!")

# 1️⃣ Unit Converter Section
if mode == "📏 Unit Converter":
    st.subheader("📐 Unit Converter")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        value = st.text_input("🔢 Enter value:", placeholder="e.g., 10")
    
    with col2:
        from_unit = st.text_input("📏 From unit:", placeholder="e.g., meters")
    
    with col3:
        to_unit = st.text_input("🔄 To unit:", placeholder="e.g., feet")
    
    if st.button("🚀 Convert Now", use_container_width=True):
        if value and from_unit and to_unit:
            try:
                value = float(value)
                result = convert_units(value, from_unit, to_unit)
                st.success(f"✅ {result}")
            except ValueError:
                st.error("❌ Please enter a valid numeric value.")
        else:
            st.warning("⚠️ Please fill all fields correctly.")

# 2️⃣ AI Assistant Section
elif mode == "🤖 AI Assistant":
    st.subheader("🤖 AI Assistant")
    
    user_query = st.text_area("💬 Ask anything:", placeholder="Type your question here...")
    
    if st.button("🚀 Get Answer", use_container_width=True):
        if user_query:
            ai_response = ask_gemini(user_query)
            st.success(f"🤖 {ai_response}")
        else:
            st.error("⚠️ Please enter a question.")

# 3️⃣ Conversion Table Section
elif mode == "📚 Conversion Table":
    st.subheader("📚 Common Unit Conversions")
    
    conversion_data = {
        "Length": ["1 meter = 3.281 feet", "1 kilometer = 0.621 miles"],
        "Weight": ["1 kilogram = 2.205 pounds", "1 gram = 0.035 ounces"],
        "Temperature": ["0°C = 32°F", "100°C = 212°F"],
        "Volume": ["1 liter = 4.227 cups", "1 gallon = 3.785 liters"],
    }
    
    for category, conversions in conversion_data.items():
        with st.expander(f"📌 {category}"):
            for conversion in conversions:
                st.write(f"🔹 {conversion}")

# Footer
st.markdown("---")
st.markdown("🚀 Developed by *Your Name* | Powered by *Gemini AI & Streamlit*")
                         

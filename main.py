import streamlit as st
import pint
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("⚠️ Gemini API key not found. Please check your .env file.")

# Unit conversion setup
ureg = pint.UnitRegistry()

def convert_units(value, from_unit, to_unit):
    try:
        result = (value * ureg(from_unit.lower())).to(to_unit.lower())
        return f"{value} {from_unit} = {result}"
    except pint.DimensionalityError:
        return "❌ Invalid conversion"
    except Exception:
        return "⚠️ Please enter a valid numeric value and unit names."

def ask_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        if response and hasattr(response, 'text'):
            return response.text
        return "⚠️ No valid response received from Gemini AI."
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Streamlit UI setup
st.set_page_config(page_title="Gemini Unit Converter", page_icon="♾️", layout="wide")
st.sidebar.title("🛠️ Settings")
mode = st.sidebar.radio("Select Options:", ["Unit Converter", "AI Assistant", "Units & Conversions Table"])
st.sidebar.markdown("Effortlessly transform your *UNITS🔮*")

st.title("♾️ Gemini-Powered Unit Converter")
st.write("Easily convert units and ask AI-powered questions!")

# Unit Converter Mode
if mode == "Unit Converter":
    st.subheader("🔮 Unit Converter")
    
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
            st.warning("⚠️ Please fill in all fields correctly.


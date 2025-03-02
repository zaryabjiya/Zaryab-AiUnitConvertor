import streamlit as st
import pint
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Check API Key
if not api_key:
    st.error("❌ API Key not found! Set GEMINI_API_KEY in .env file.")
else:
    genai.configure(api_key=api_key)

# Initialize Pint for unit conversion
ureg = pint.UnitRegistry()

# Function to convert units
def convert_units(value, from_unit, to_unit):
    try:
        result = (value * ureg(from_unit.lower())).to(to_unit.lower())
        return f"{value} {from_unit} = {result}"
    except pint.DimensionalityError:
        return "❌ Invalid conversion"
    except Exception:
        return "⚠️ Please enter a valid numeric value and unit names."

# Function to interact with Gemini AI
def ask_gemini(prompt):
    if not api_key:
        return "❌ API Key not found! Set GEMINI_API_KEY in .env file."
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text if response and response.text else "⚠️ No response received from AI. Please try again."
    except Exception as e:
        return f"❌ AI Error: {str(e)}"

# Streamlit Page Configuration
st.set_page_config(page_title="Gemini Unit Converter", page_icon="♾️", layout="wide")
st.sidebar.title("🛠️ Settings")
mode = st.sidebar.radio("Select Options:", ["Unit Converter", "AI Assistant", "Units & Conversions Table"])

st.title("♾️ Gemini-Powered Unit Converter")

# Unit Converter Section
if mode == "Unit Converter":
    st.subheader("🔮 Unit Converter")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        value = st.text_input("🔢 Enter value:", placeholder="e.g., 10")
    with col2:
        from_unit = st.text_input("📏 From unit:", placeholder="e.g., meters")
    with col3:
        to_unit = st.text_input("🔄 To unit:", placeholder="e.g., feet")
    if st.button("🚀 Convert Now"):
        if value and from_unit and to_unit:
            try:
                value = float(value)
                result = convert_units(value, from_unit, to_unit)
                st.success(f"✅ {result}")
            except ValueError:
                st.error("❌ Please enter a valid numeric value.")
        else:
            st.warning("⚠️ Please fill in all fields correctly.")

# AI Assistant Section
elif mode == "AI Assistant":
    st.subheader("🧠 AI Assistant")
    user_query = st.text_area("💬 Ask anything:", placeholder="Type your question here...")
    if st.button("🚀 Get Answer"):
        if user_query:
            ai_response = ask_gemini(user_query)
            st.success(f"🤖 {ai_response}")
        else:
            st.error("⚠️ Please enter a question.")

# Units & Conversions Table Section
elif mode == "Units & Conversions Table":
    st.subheader("📏 Common Units & Conversions")
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
st.markdown("🚀 Developed by *Zaryab Irfan* | Powered by *Gemini AI & Streamlit*")


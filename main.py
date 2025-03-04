import streamlit as st
import pint
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini AI
genai.configure(api_key=api_key)

# Initialize Pint for unit conversion
ureg = pint.UnitRegistry()

# Function to convert units
def convert_units(value, from_unit, to_unit):
    try:
        result = (value * ureg(from_unit.lower())).to(to_unit.lower())
        return f"{value} {from_unit} = {result}"
    except pint.DimensionalityError:
        return "Invalid conversion"
    except Exception:
        return "Please enter a valid numeric value and unit names."

# Function to interact with Gemini AI
def ask_gemini(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text if response else "Error fetching response"

# Streamlit Page Configuration
st.set_page_config(page_title="Unit Converter & AI Assistant", page_icon="🔢", layout="wide")

# Sidebar for settings
st.sidebar.title("Settings")
mode = st.sidebar.radio("Choose Mode:", ["Unit Converter", "AI Assistant", "Units & Conversion Table"])

# Dark/Light Mode Toggle
theme = st.sidebar.radio("Select Theme:", ["Light Mode", "Dark Mode"])

if theme == "Dark Mode":
    st.markdown(
        """
        <style>
        body { background-color: #121212; color: white; }
        .stTextInput, .stNumberInput { background-color: #1E1E1E !important; color: white !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )

st.title("Unit Converter & AI Assistant")
st.write("Easily convert units and get AI-powered answers!")

# Unit Converter Section
if mode == "Unit Converter":
    st.subheader("Unit Converter")
    st.markdown("Enter details below to convert units.")

    col1, col2, col3 = st.columns(3)

    with col1:
        value = st.text_input("Enter Value:", placeholder="e.g., 10")

    with col2:
        from_unit = st.text_input("From Unit:", placeholder="e.g., meters")

    with col3:
        to_unit = st.text_input("To Unit:", placeholder="e.g., feet")

    if st.button("Convert Now"):
        if value and from_unit and to_unit:
            try:
                value = float(value)
                result = convert_units(value, from_unit, to_unit)
                st.success(result)
            except ValueError:
                st.error("Please enter a valid numeric value.")
        else:
            st.warning("Please fill in all fields correctly.")

# AI Assistant Section
elif mode == "AI Assistant":
    st.subheader("AI Chat Assistant")
    user_query = st.text_area("Ask anything:", placeholder="Type your question here...")

    if st.button("Get Answer"):
        if user_query:
            ai_response = ask_gemini(user_query)
            st.success(ai_response)
        else:
            st.error("Please enter a question.")

# Units & Conversion Table
elif mode == "Units & Conversion Table":
    st.subheader("Common Units & Conversions")
    conversion_data = {
        "Length": ["1 meter = 3.281 feet", "1 kilometer = 0.621 miles"],
        "Weight": ["1 kilogram = 2.205 pounds", "1 gram = 0.035 ounces"],
        "Temperature": ["0°C = 32°F", "100°C = 212°F"],
        "Volume": ["1 liter = 4.227 cups", "1 gallon = 3.785 liters"],
    }

    for category, conversions in conversion_data.items():
        with st.expander(category):
            for conversion in conversions:
                st.write(conversion)

# Footer
st.markdown("---")
st.markdown("Developed by Your Name | Powered by Gemini AI & Streamlit")

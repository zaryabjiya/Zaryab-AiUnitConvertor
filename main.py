import streamlit as st
import pint
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Unit conversion setup
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

# Streamlit UI Setup
st.set_page_config(page_title="Elegant Unit Converter", page_icon="♾️", layout="centered")

# Custom Styling
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
        }
        .title {
            font-size: 2.2em;
            font-weight: bold;
            color: #2c3e50;
            text-align: center;
        }
        .stTextInput, .stNumberInput {
            border-radius: 10px !important;
            padding: 10px !important;
            background-color: #f5f5f5 !important;
        }
        .convert-btn {
            background-color: #3498db !important;
            color: white !important;
            font-size: 1.1em;
            font-weight: bold;
            border-radius: 10px !important;
            width: 100%;
        }
        .success-message {
            font-size: 1.2em;
            color: #2ecc71;
            font-weight: bold;
        }
        .warning-message {
            font-size: 1.1em;
            color: #e74c3c;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">♾️ Elegant Unit Converter</p>', unsafe_allow_html=True)
st.write("Convert units quickly and accurately with a sleek interface!")

# Sidebar Navigation
st.sidebar.title("🔄 Unit Converter Menu")
mode = st.sidebar.radio("Choose an option:", ["Unit Converter", "Units & Conversions Table"])
st.sidebar.markdown("---")

# Unit Converter Section
if mode == "Unit Converter":
    st.subheader("📏 Convert Units Instantly")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        value = st.text_input("🔢 Enter value:", placeholder="e.g., 10")
    
    with col2:
        from_unit = st.text_input("📏 From unit:", placeholder="e.g., meters")
    
    with col3:
        to_unit = st.text_input("🔄 To unit:", placeholder="e.g., feet")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("🚀 Convert Now", use_container_width=True):
        if value and from_unit and to_unit:
            try:
                value = float(value)
                result = convert_units(value, from_unit, to_unit)
                st.markdown(f'<p class="success-message">✅ {result}</p>', unsafe_allow_html=True)
            except ValueError:
                st.markdown('<p class="warning-message">❌ Please enter a valid numeric value.</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="warning-message">⚠️ Please fill in all fields correctly.</p>', unsafe_allow_html=True)

# Units & Conversions Table
elif mode == "Units & Conversions Table":
    st.subheader("📌 Common Units & Conversions")
    st.write("A handy reference guide for everyday conversions.")
    
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
st.markdown("Developed by *Zaryab Irfan* | Powered by *Streamlit*")


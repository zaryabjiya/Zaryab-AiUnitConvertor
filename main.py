import streamlit as st
import pint
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Unit conversion setup
ureg = pint.UnitRegistry()

# List of common units for dropdown
unit_options = [
    "meters", "feet", "kilometers", "miles", "centimeters", "inches",
    "kilograms", "pounds", "grams", "ounces", "liters", "gallons",
    "celsius", "fahrenheit", "kelvin", "joules", "calories"
]

# Function to convert units
def convert_units(value, from_unit, to_unit):
    try:
        result = (value * ureg(from_unit)).to(to_unit)
        return f"{value} {from_unit} = {result}"
    except pint.DimensionalityError:
        return "❌ Invalid conversion"
    except Exception:
        return "⚠️ Please enter a valid numeric value and unit names."

# Streamlit UI Setup
st.set_page_config(page_title="Vibrant Unit Converter", page_icon="♾️", layout="centered")

# Custom Styling
st.markdown("""
    <style>
        body {
            background-color: #1f1f1f;
        }
        .title {
            font-size: 2.5em;
            font-weight: bold;
            color: #ffcc00;
            text-align: center;
            text-shadow: 2px 2px 5px rgba(255, 204, 0, 0.8);
        }
        .stTextInput, .stSelectbox, .stNumberInput {
            border-radius: 10px !important;
            padding: 10px !important;
            background-color: #fffcf5 !important;
            color: #333 !important;
        }
        .convert-btn {
            background-color: #ff5733 !important;
            color: white !important;
            font-size: 1.2em;
            font-weight: bold;
            border-radius: 10px !important;
            width: 100%;
            transition: 0.3s;
        }
        .convert-btn:hover {
            background-color: #ff2e00 !important;
        }
        .success-message {
            font-size: 1.3em;
            color: #27ae60;
            font-weight: bold;
            text-align: center;
        }
        .warning-message {
            font-size: 1.2em;
            color: #e74c3c;
            font-weight: bold;
            text-align: center;
        }
        .unit-box {
            background: linear-gradient(135deg, #ff7e5f, #feb47b);
            padding: 15px;
            border-radius: 10px;
            color: white;
            font-weight: bold;
            text-align: center;
            font-size: 1.2em;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">♾️ Vibrant Unit Converter</p>', unsafe_allow_html=True)
st.write("Convert units instantly with an interactive, colorful experience! 🚀")

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
        from_unit = st.selectbox("📏 From unit:", options=unit_options, index=0)

    with col3:
        to_unit = st.selectbox("🔄 To unit:", options=unit_options, index=1)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🚀 Convert Now", use_container_width=True, key="convert"):
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
        "Length": ["1 meter = 3.281 feet", "1 kilometer = 0.621 miles", "1 inch = 2.54 cm"],
        "Weight": ["1 kilogram = 2.205 pounds", "1 gram = 0.035 ounces"],
        "Temperature": ["0°C = 32°F", "100°C = 212°F"],
        "Volume": ["1 liter = 4.227 cups", "1 gallon = 3.785 liters"],
        "Energy": ["1 joule = 0.239 calories", "1 calorie = 4.184 joules"]
    }

    for category, conversions in conversion_data.items():
        with st.expander(f"📌 {category}"):
            for conversion in conversions:
                st.markdown(f'<div class="unit-box">🔹 {conversion}</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Developed by *Zaryab Irfan* | Powered by *Streamlit*")


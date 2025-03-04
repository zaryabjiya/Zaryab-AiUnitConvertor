import streamlit as st 

# Custom CSS for a new futuristic and glowing look
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.4);
        color: white;
    }
    h1 {
        text-align: center;
        font-size: 42px;
        color: #00d4ff;
        font-weight: bold;
        text-shadow: 3px 3px 8px rgba(0, 212, 255, 0.7);
    }
    .stButton>button {
        background: linear-gradient(45deg, #ff00ff, #ff6600);
        color: white;
        font-size: 22px;
        padding: 14px 28px;
        border-radius: 18px;
        transition: 0.3s ease-in-out;
        box-shadow: 0px 6px 18px rgba(255, 0, 255, 0.6);
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        transform: scale(1.15);
        background: linear-gradient(45deg, #00ffcc, #0099ff);
        color: black;
    }
    .result-box {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.15);
        padding: 24px;
        border-radius: 14px;
        margin-top: 20px;
        box-shadow: 0px 6px 18px rgba(255, 255, 255, 0.3);
        color: white;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 16px;
        color: #00d4ff;
        font-weight: bold;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Title and description with new emojis
st.markdown("<h1> 🚀 Ultimate Unit Converter 🌍 </h1>", unsafe_allow_html=True)
st.write("✨ Convert your units with style and speed! 🔥 Choose a category and enter your value to get started.")

# Sidebar menu with cool emojis
conversion_type = st.sidebar.selectbox("🔄 Choose Conversion Type", ["📏 Length", "⚖️ Weight", "🌡 Temperature"])
value = st.number_input("🔢 Enter Value", value=0.0, min_value=0.0, step=0.1)

col1, col2 = st.columns(2)

# Conversion options with more intuitive selection
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

# Conversion functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Millimeters': 1000,
        'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28084, 'Inches': 39.3701
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Kilogram': 1, 'Grams': 1000, 'Milligrams': 1000000, 'Pounds': 2.20462, 'Ounces': 35.274
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temp_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return ((value - 32) * 5/9) if to_unit == "Celsius" else ((value - 32) * 5/9 + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return (value - 273.15) if to_unit == "Celsius" else ((value - 273.15) * 9/5 + 32) if to_unit == "Fahrenheit" else value
    return value

# Button for conversion with animated effect
if st.button("🎯 Convert Now 🚀"):
    if conversion_type == "📏 Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "⚖️ Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "🌡 Temperature":
        result = temp_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>✅ {value} {from_unit} = {result:.4f} {to_unit} 🎉</div>", unsafe_allow_html=True)        

# Footer with a new exciting text
st.markdown("<div class='footer'>🔥 Powered by Innovation | Made with ❤️ by Zaryab 🔥</div>", unsafe_allow_html=True)    

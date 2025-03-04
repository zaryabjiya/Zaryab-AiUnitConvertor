import streamlit as st 

# Custom Styling
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0c39, #302b93, #52243e);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.4);
        color: white;
    }
    h1 {
        text-align: center;
        font-size: 42px;
        color: #ff00ff;
        font-weight: bold;
        text-shadow: 2px 2px 8px rgba(255, 0, 255, 0.6);
    }
    .stButton>button {
        background: linear-gradient(45deg, #ff0099, #ff6600);
        color: white;
        font-size: 20px;
        padding: 12px 24px;
        border-radius: 15px;
        transition: 0.3s ease-in-out;
        box-shadow: 0px 5px 20px rgba(255, 0, 153, 0.6);
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        transform: scale(1.1);
        background: linear-gradient(45deg, #00ffcc, #ff33cc);
        color: black;
    }
    .result-box {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        margin-top: 20px;
        box-shadow: 0px 5px 20px rgba(255, 255, 255, 0.3);
        color: white;
        backdrop-filter: blur(12px);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 16px;
        color: #ff00ff;
        font-weight: bold;
        text-shadow: 1px 1px 5px rgba(255, 0, 255, 0.5);
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Title and description
st.markdown("<h1>🚀 Advanced Unit Converter 🚀</h1>", unsafe_allow_html=True)
st.write("Convert units with a **futuristic look** and smooth animations!")

# Sidebar menu
conversion_type = st.sidebar.radio("⚡ Select Conversion Type:", ["Length", "Weight", "Temperature"])
value = st.number_input("🔢 Enter Value:", value=0.0, min_value=0.0, step=0.1)

col1, col2 = st.columns(2)

# Conversion options
if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("📏 From:", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("📐 To:", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("⚖️ From:", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("🛠 To:", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("🌡 From:", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("🔥 To:", ["Celsius", "Fahrenheit", "Kelvin"])

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

# Button for conversion
if st.button("✨ Convert Now ✨"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temp_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)        

# Footer
st.markdown("<div class='footer'>✨ Developed by Zaryab Irfan ✨</div>", unsafe_allow_html=True) 

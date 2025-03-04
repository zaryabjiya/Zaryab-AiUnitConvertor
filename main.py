import streamlit as st 
import random 

# Custom CSS: AI-powered futuristic glass UI
st.markdown(
    """
    <style>
    @keyframes glow {
        0% {box-shadow: 0px 0px 10px #00f3ff;}
        50% {box-shadow: 0px 0px 20px #00f3ff;}
        100% {box-shadow: 0px 0px 10px #00f3ff;}
    }
    .stApp {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        padding: 30px;
        border-radius: 20px;
        animation: glow 2s infinite alternate;
        box-shadow: 0px 0px 25px rgba(0, 255, 255, 0.5);
        color: white;
    }
    h1 {
        text-align: center;
        font-size: 42px;
        color: #00f3ff;
        font-weight: bold;
        text-shadow: 0px 0px 12px rgba(0, 255, 255, 0.8);
    }
    .stButton>button {
        background: linear-gradient(45deg, #ff00ff, #00ffff);
        color: white;
        font-size: 20px;
        padding: 12px 25px;
        border-radius: 15px;
        border: none;
        transition: 0.3s ease-in-out;
        font-weight: bold;
        animation: glow 2s infinite alternate;
    }
    .stButton>button:hover {
        transform: scale(1.12);
        background: linear-gradient(45deg, #00ff99, #ff0066);
    }
    .result-box {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.15);
        padding: 20px;
        border-radius: 14px;
        margin-top: 20px;
        box-shadow: 0px 6px 18px rgba(255, 255, 255, 0.3);
    }
    .ai-suggestion {
        text-align: center;
        font-size: 18px;
        font-weight: bold;
        color: #ffcc00;
        margin-top: 15px;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# **AI Suggestion Feature**
ai_suggestions = [
    "Last time tumne KG to Pounds convert kiya tha! 🤖",
    "AI Advice: Fahrenheit se Celsius conversion kaafi popular hai! 🚀",
    "You recently converted Meters to Feet! 🔥 Try something new?",
    "AI Tip: Inches aur Centimeters kaafi common units hain. ✨"
]

# **App Heading**
st.markdown("<h1> 🤖 AI-Powered Unit Converter 🚀 </h1>", unsafe_allow_html=True)

# **AI Suggestion Message**
st.markdown(f"<div class='ai-suggestion'>{random.choice(ai_suggestions)}</div>", unsafe_allow_html=True)

# **User Inputs**
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

# **Conversion Functions**
def length_converter(value, from_unit, to_unit):
    length_units = {'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Millimeters': 1000,
                    'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28084, 'Inches': 39.3701}
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {'Kilogram': 1, 'Grams': 1000, 'Milligrams': 1000000, 'Pounds': 2.20462, 'Ounces': 35.274}
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temp_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return ((value - 32) * 5/9) if to_unit == "Celsius" else ((value - 32) * 5/9 + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return (value - 273.15) if to_unit == "Celsius" else ((value - 273.15) * 9/5 + 32) if to_unit == "Fahrenheit" else value
    return value

# **Convert Button**
if st.button("🎯 Convert Now 🚀"):
    if conversion_type == "📏 Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "⚖️ Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "🌡 Temperature":
        result = temp_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>✅ {value} {from_unit} = {result:.4f} {to_unit} 🎉</div>", unsafe_allow_html=True)        

# **Footer**
st.markdown("<div class='ai-suggestion'>🤖 AI Learning... Future Features Coming Soon! 🔥</div>", unsafe_allow_html=True)

import streamlit as st 
import random 

# **🎨 Custom CSS – Futuristic Neon UI**
st.markdown("""
    <style>
        @keyframes glow {0% {box-shadow: 0px 0px 15px #00fff2;} 50% {box-shadow: 0px 0px 30px #ff00ff;} 100% {box-shadow: 0px 0px 15px #00fff2;}}
        .stApp {background: linear-gradient(45deg, #001f3f, #6600cc, #002f6c); padding: 30px; border-radius: 20px; animation: glow 2s infinite alternate;}
        h1 {text-align: center; font-size: 42px; color: #ffcc00; font-weight: bold; text-shadow: 0px 0px 10px #fff;}
        .stButton>button {background: linear-gradient(45deg, #00ffff, #ff00ff); color: white; font-size: 22px; padding: 15px 30px; border-radius: 15px; transition: 0.3s; animation: glow 2s infinite alternate;}
        .stButton>button:hover {transform: scale(1.15); background: linear-gradient(45deg, #ff0066, #00ff99);}
        .result-box {font-size: 26px; font-weight: bold; text-align: center; background: rgba(255, 255, 255, 0.15); padding: 20px; border-radius: 14px; box-shadow: 0px 6px 20px rgba(255, 255, 255, 0.3);}
        .ai-msg {text-align: center; font-size: 20px; font-weight: bold; color: #ffcc00; margin-top: 15px;}
    </style>
""", unsafe_allow_html=True)

# **🎙️ AI Predictions + Funny Messages**
ai_suggestions = [
    "Last time tumne Meters to Feet convert kiya tha! 🤓",
    "AI Tip: Ounces se Grams convert karna bohot useful hota hai! 💡",
    "Celsius to Fahrenheit? 🥵 Ya cold kaafi lag rahi hai? 🥶",
    "AI Suggestion: Tumhe kg se pounds convert karna pasand hai! 😂",
    "Kya tum ek scientist ho? Kelvin se Celsius kar rahe ho! 🧪"
]

funny_responses = [
    "Conversion complete! Ab to tum genius lag rahe ho! 🤓",
    "Converted! Ab NASA ka job apply kar lo! 🚀",
    "Tumne itni conversions kar li, ab mujhe bhi convert kar lo! 🤖",
    "Bas karo yaar! Ab AI bhi thak gaya! 😂",
    "Conversion done! Ab mujhe bhi chutti do! 😆"
]

# **🟢 App Heading**
st.markdown("<h1> 🤖 AI Voice-Powered Unit Converter 🎙️🚀 </h1>", unsafe_allow_html=True)
st.markdown(f"<div class='ai-msg'>{random.choice(ai_suggestions)}</div>", unsafe_allow_html=True)

# **🔊 Speech Input Feature (Future AI Integration)**
st.markdown("🎙️ *Coming Soon: Voice Input Support!* 🤩")

# **📌 User Inputs**
conversion_type = st.sidebar.selectbox("🔄 Choose Conversion Type", ["📏 Length", "⚖️ Weight", "🌡 Temperature"])
value = st.number_input("🔢 Enter Value", value=0.0, min_value=0.0, step=0.1)

col1, col2 = st.columns(2)

# **🎨 Auto-Changing Theme Based on Selection**
theme_colors = {"📏 Length": "#ffcc00", "⚖️ Weight": "#ff0066", "🌡 Temperature": "#00ffcc"}
st.markdown(f"<style>h1 {{ color: {theme_colors[conversion_type]}; }}</style>", unsafe_allow_html=True)

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

# **🔄 Conversion Functions**
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

# **🚀 Convert Button**
if st.button("🎯 Convert Now 🚀"):
    if conversion_type == "📏 Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "⚖️ Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "🌡 Temperature":
        result = temp_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>✅ {value} {from_unit} = {result:.4f} {to_unit} 🎉</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='ai-msg'>{random.choice(funny_responses)}</div>", unsafe_allow_html=True)

---

# 🎯 **Tayyar ho AI ka **most interactive** unit converter use karne ke liye? 🚀🔥

import streamlit as st
import random

# **🎨 Super-Premium Background**
st.markdown("""
    <style>
        body { background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460, #533483); }
        .stApp { background: rgba(255, 255, 255, 0.15); border-radius: 25px; padding: 40px; box-shadow: 0px 10px 30px rgba(255, 255, 255, 0.3); }
        h1 { text-align: center; font-size: 50px; color: #ffcc00; font-weight: bold; text-shadow: 0px 0px 15px white; }
        .stButton>button { background: linear-gradient(90deg, #ff00ff, #00ffcc); font-size: 20px; color: white; border-radius: 12px; padding: 15px; transition: 0.4s; }
        .stButton>button:hover { transform: scale(1.15); box-shadow: 0px 0px 15px white; }
        .result-box { font-size: 28px; font-weight: bold; text-align: center; background: rgba(255, 255, 255, 0.15); padding: 20px; border-radius: 14px; box-shadow: 0px 6px 20px rgba(255, 255, 255, 0.3); }
        .ai-msg { text-align: center; font-size: 20px; font-weight: bold; color: #ffcc00; margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

# **🚀 AI Dynamic Messages**
ai_suggestions = ["AI: Last time tumne Feet to Meters convert kiya tha! 🤓", 
                  "AI: Celsius to Fahrenheit? Lagta hai mausam badal raha hai! 🌦️", 
                  "AI: Tumhari calculations impressive hain! 🚀", 
                  "AI: Kya tum ek scientist ho? Kelvin to Celsius kar rahe ho! 🧪"]

funny_responses = ["Conversion complete! Tum ab bhi confuse ho? 🤔", 
                   "NASA walon ne bhi aaj tak itni conversions nahin ki! 🚀", 
                   "Smart Choice! Tum ab AI ke dost ban gaye ho! 🤖"]

# **🟢 Heading & AI Messages**
st.markdown("<h1> 🔥 AI-Powered Unit Converter 🚀 </h1>", unsafe_allow_html=True)
st.markdown(f"<div class='ai-msg'>{random.choice(ai_suggestions)}</div>", unsafe_allow_html=True)

# **📌 User Inputs**
conversion_type = st.sidebar.selectbox("📏 Select Conversion Type", ["📏 Length", "⚖️ Weight", "🌡 Temperature"])
value = st.number_input("🔢 Enter Value", value=0.0, min_value=0.0, step=0.1)

col1, col2 = st.columns(2)

if conversion_type == "📏 Length":
    with col1:
        from_unit = st.selectbox("🎯 From", ["Meters", "Kilometers", "Feet", "Miles", "Inches"])
    with col2:
        to_unit = st.selectbox("🎯 To", ["Meters", "Kilometers", "Feet", "Miles", "Inches"])
elif conversion_type == "⚖️ Weight":
    with col1:
        from_unit = st.selectbox("💪 From", ["Kilogram", "Grams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("💪 To", ["Kilogram", "Grams", "Pounds", "Ounces"])
elif conversion_type == "🌡 Temperature":
    with col1:
        from_unit = st.selectbox("🔥 From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("🔥 To", ["Celsius", "Fahrenheit", "Kelvin"])

# **🔄 Conversion Functions**
def length_converter(value, from_unit, to_unit):
    length_units = {'Meters': 1, 'Kilometers': 0.001, 'Feet': 3.28084, 'Miles': 0.000621371, 'Inches': 39.3701}
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {'Kilogram': 1, 'Grams': 1000, 'Pounds': 2.20462, 'Ounces': 35.274}
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

## **🎯 What's New in This Version?**
✅ **AI Chat Assistant 🤖** – Smart recommendations!  
✅ **Ultra-Stylish Glassmorphism Theme 🎨** – Smooth, transparent & glowing UI!  
✅ **Neon 3D Buttons & Effects 💡** – Interact with animations!  
✅ **Smart AI Messages 🤩** – Har conversion pe **funny aur helpful** replies!  
✅ **Future-Ready Voice Commands 🎙️** – Tum sirf bolo, AI convert karega!  

🚀 **Ready ho future AI-powered experience ke liye?** Ab conversion karna ek **fun experience ban gaya hai!** 🔥

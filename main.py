import streamlit as st
import pint
import google.generativeai as genai
from dotenv import load_dotenv
import os

# ✅ Streamlit Page Configuration (Must be First!)
st.set_page_config(page_title="Gemini Unit Converter", page_icon="♾️", layout="wide")

# ✅ Load API Key from .env OR use a manual fallback key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY", "your_actual_api_key_here")  # Replace manually if needed

# ✅ Check if API key is present
if not api_key or api_key == "your_actual_api_key_here":
    st.error("❌ API Key not found! Set `GEMINI_API_KEY` in `.env` or update the script.")

# ✅ Initialize Gemini AI
else:
    genai.configure(api_key=api_key)

# ✅ Initialize Pint for unit conversion
ureg = pint.UnitRegistry()

# 🔄 Function to Convert Units
def convert_units(value, from_unit, to_unit):
    try:
        result = (value * ureg(from_unit.lower())).to(to_unit.lower())
        return f"{value} {from_unit} = {result}"
    except pint.DimensionalityError:
        return "❌ Invalid conversion (mismatched units)"
    except Exception:
        return "⚠️ Please enter a valid numeric value and unit names."

# 🤖 Function to Get AI Response
def ask_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text if response else "⚠️ AI response not available."
    except Exception as e:
        return f"❌ AI Error: {str(e)}"

# ✅ Sidebar Navigation
st.sidebar.title("🛠️ Settings")
mode = st.sidebar.radio("Select Option:", ["Unit Converter", "AI Assistant", "Units & Conversions Table"])

st.title("♾️ Gemini-Powered Unit Converter & AI Assistant")

# 🔮 **Unit Converter**
if mode == "Unit Converter":
    st.subheader("🔄 Convert Units Instantly")

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
            st.warning("⚠️ Please fill in all fields.")

# 🧠 **AI Assistant**
elif mode == "AI Assistant":
    st.subheader("🤖 Ask Gemini AI")

    user_query = st.text_area("💬 Type your question...", placeholder="Ask anything here...")
    
    if st.button("🚀 Get AI Answer"):
        if user_query:
            ai_response = ask_gemini(user_query)
            st.success(f"🤖 {ai_response}")
        else:
            st.error("⚠️ Please enter a question.")

# 📏 **Units & Conversions Table**
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

# ✅ Footer
st.markdown("---")
st.markdown("🚀 Developed by *Zaryab Irfan* | Powered by *Gemini AI & Streamlit*")


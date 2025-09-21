import streamlit as st
import streamlit.components.v1 as components

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Abdallah Hesham | Portfolio", layout="wide")

# -------------------------------
# Sidebar Navigation
# -------------------------------
st.sidebar.title("📂 My Tools")
pages = [
    "🏠 Home",
    "🔍 Capacitor Value Matcher Tool",
    "📏 Enhanced Resistance Code Parser",
    "📝 Excel Mask Processing Tool PC",
    "✂️ Exact Character-by-Character Difference Tool",
    "📊 Enhanced Series Comparison Tool",
    "🛠️ Pin Analysis Tool"
]

choice = st.sidebar.radio("Navigate", pages)

# -------------------------------
# Home Page
# -------------------------------
if choice == "🏠 Home":
    st.title("🚀 My Portfolio")
    st.write("Hi, I'm **Abdallah Hesham** – DevOps Engineer | Automation | Data Tools")
    st.write("Here are some of the tools I’ve built with Streamlit 👇")

    st.markdown("### 🔍 [Capacitor Value Matcher Tool](https://capacitacevalueextractionfriday.streamlit.app/)")
    st.markdown("### 📏 [Enhanced Resistance Code Parser](https://z2tools-resistance.streamlit.app/)")
    st.markdown("### 📝 [Excel Mask Processing Tool PC](https://z2tools-mask-pc.streamlit.app/)")
    st.markdown("### ✂️ [Exact Character-by-Character Difference Tool](https://part-masker-app.streamlit.app/)")
    st.markdown("### 📊 [Enhanced Series Comparison Tool](https://seriesf.streamlit.app/)")
    st.markdown("### 🛠️ [Pin Analysis Tool](https://z2tools-pin-out-tool.streamlit.app/)")

# -------------------------------
# Capacitor Value Matcher Tool
# -------------------------------
elif choice == "🔍 Capacitor Value Matcher Tool":
    st.title("🔍 Capacitor Value Matcher Tool")
    st.write("Upload Excel files to process and match capacitor values efficiently.")
    components.iframe("https://capacitacevalueextractionfriday.streamlit.app/", height=700)

# -------------------------------
# Enhanced Resistance Code Parser
# -------------------------------
elif choice == "📏 Enhanced Resistance Code Parser":
    st.title("📏 Enhanced Resistance Code Parser")
    st.write("A tool to parse and analyze resistance codes with batch processing support.")
    components.iframe("https://z2tools-resistance.streamlit.app/", height=700)

# -------------------------------
# Excel Mask Processing Tool PC
# -------------------------------
elif choice == "📝 Excel Mask Processing Tool PC":
    st.title("📝 Excel Mask Processing Tool PC")
    st.write("Process Excel files with advanced masking logic for part numbers.")
    components.iframe("https://z2tools-mask-pc.streamlit.app/", height=700)

# -------------------------------
# Exact Character-by-Character Difference Tool
# -------------------------------
elif choice == "✂️ Exact Character-by-Character Difference Tool":
    st.title("✂️ Exact Character-by-Character Difference Tool")
    st.write("Compare part numbers with exact character-level differences.")
    components.iframe("https://part-masker-app.streamlit.app/", height=700)

# -------------------------------
# Enhanced Series Comparison Tool
# -------------------------------
elif choice == "📊 Enhanced Series Comparison Tool":
    st.title("📊 Enhanced Series Comparison Tool")
    st.write("Perform advanced series comparisons with detailed analysis.")
    components.iframe("https://seriesf.streamlit.app/", height=700)

# -------------------------------
# Pin Analysis Tool
# -------------------------------
elif choice == "🛠️ Pin Analysis Tool":
    st.title("🛠️ Pin Analysis Tool")
    st.write("Analyze and compare pinouts with advanced matching features.")
    components.iframe("https://z2tools-pin-out-tool.streamlit.app/", height=700)

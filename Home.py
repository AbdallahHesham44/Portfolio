import streamlit as st

st.set_page_config(page_title="Abdallah Hesham | Portfolio", layout="wide")

st.title("🚀 My Portfolio")
st.write("Hi, I'm **Abdallah Hesham** – DevOps Engineer | Automation | Data Tools")
st.write("Here are some of the tools I’ve built with Streamlit 👇")

projects = {
    "Capacitor Value Matcher Tool": "https://capacitacevalueextractionfriday.streamlit.app/",
    "Enhanced Resistance Code Parser": "https://z2tools-resistance.streamlit.app/",
    "Excel Mask Processing Tool PC": "https://z2tools-mask-pc.streamlit.app/",
    "Exact Character-by-Character Difference Tool": "https://part-masker-app.streamlit.app/",
    "Enhanced Series Comparison Tool": "https://seriesf.streamlit.app/",
    "Pin Analysis Tool": "https://z2tools-pin-out-tool.streamlit.app/"
}

for name, link in projects.items():
    st.markdown(f"### [{name}]({link})")

import streamlit as st
from pages.encrypt_page import show_encrypt_page
from pages.decrypt_page import show_decrypt_page

st.set_page_config(page_title="AudioCrypt", layout="centered")

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "main"

if st.session_state.page == "main":
    st.title("🔐 AudioCrypt : A Secure Web APP For Encrypt & Decrypt Your Audio Files ")
    st.markdown(" ### Secure Your Voice Seamlessly ### ")
    st.markdown(""" A Clean UI and Zero Complexity — Privacy Meets Simplicity 🎙️✨

- 🎧 Record audio directly in-browser  
- 🔒 Encrypt with any custom key—no restrictions  
- 🔓 Decrypt and playback instantly  
- 🧩 Streamlit-powered with smooth navigation and styling
""")

    if st.button("Go to Encrypt Page"):
        st.session_state.page = "encrypt"
        st.experimental_rerun()


elif st.session_state.page == "encrypt":
    show_encrypt_page()

elif st.session_state.page == "decrypt":
    show_decrypt_page()
    
st.markdown(
    """
    <div class="footer">
        © 2025 - All rights reserverd by, <br>
        Sanjevi Sree Vijayan <br>
        Sivasankari Balachandran
    </div>
    """,
    unsafe_allow_html=True
)

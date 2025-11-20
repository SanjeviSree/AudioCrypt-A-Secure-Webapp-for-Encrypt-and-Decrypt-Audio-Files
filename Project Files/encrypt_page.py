import streamlit as st
from streamlit_mic_recorder import mic_recorder
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import base64
import os

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def show_encrypt_page():
    st.title("🎙️ Encrypt And Secure")
    st.markdown("""

- 🛡️ Secure your voice with a custom key  
- 🎙️ Record audio and encrypt it instantly with zero complexity  
- 🔑 Your key, your control  
- 🚀 No restrictions, no limits—just high protection
""")
    
    audio = mic_recorder(start_prompt="START", stop_prompt="STOP", key="rec", use_container_width=True)

    if audio:
        with open("recorded.wav", "wb") as f:
            f.write(audio["bytes"])
        st.success("Audio saved.")

        key = st.text_input("Enter Your Key", type="password", key="enc_key")
        confirm = st.text_input("Confirm Your key", type="password", key="enc_confirm")

        if key and confirm:
            if key != confirm:
                st.error("Keys do not match.")
            else:
                try:
                    hashed_key = SHA256.new(key.encode()).digest()
                    cipher = AES.new(hashed_key, AES.MODE_EAX)

                    with open("recorded.wav", "rb") as f:
                        data = f.read()
                    ciphertext, tag = cipher.encrypt_and_digest(data)

                    encrypted_path = os.path.abspath("encrypted.bin")
                    with open("encrypted.bin", "wb") as f:
                        f.write(cipher.nonce + tag + ciphertext)

                    st.session_state["aes_key"] = key
                    st.success("Encrypted!")
                    st.text_area("Preview of Encoded File", base64.b64encode(ciphertext).decode()[:500] + "...")
                    st.text(f"Encrypted file saved at: {encrypted_path}")

                    if st.button("Go to Decrypt Page"):
                        st.session_state.page = "decrypt"
                        st.experimental_rerun()
                except Exception as e:
                    st.error(f"Encryption failed: {e}")
                    
    st.markdown(
        """
        <div class="footer">
            © 2025 - All rights reserverd by,<br>
            Sanjevi Sree Vijayan <br>
            Sivasankari Balachandran
        </div>
        """,
        unsafe_allow_html=True
    )

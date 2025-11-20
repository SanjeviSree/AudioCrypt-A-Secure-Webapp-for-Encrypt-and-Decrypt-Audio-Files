import streamlit as st
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
def show_decrypt_page():
    st.title("🔓 Decrypt & Playback")
    st.markdown("""

- 🔓 Unlock your encrypted audio and listen back with clarity 🎧.
- ✅ Confirm your key and decrypt with confidence.
- 🔁 Privacy meets playback🚀.
-  No restrictions, no limits—just high protection
""")

    key = st.text_input("Enter Your key", type="password", key="dec_key")
    confirm = st.text_input("Confirm Your key", type="password", key="dec_confirm")

    if key and confirm:
        if key != confirm:
            st.error("Keys do not match.")
        else:
            if st.button("DECRYPT"):
                try:
                    with open("encrypted.bin", "rb") as f:
                        nonce = f.read(16)
                        tag = f.read(16)
                        ciphertext = f.read()

                    hashed_key = SHA256.new(key.encode()).digest()
                    cipher = AES.new(hashed_key, AES.MODE_EAX, nonce=nonce)
                    decrypted = cipher.decrypt_and_verify(ciphertext, tag)

                    st.success("Decryption successful.")
                    st.audio(decrypted, format="audio/wav")
                except Exception as e:
                    st.error(f"Decryption failed: {e}")
                    
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

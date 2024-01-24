import streamlit as st
from deep_translator import GoogleTranslator
import os
import tempfile

# Set page title and favicon
st.set_page_config(
    page_title="Deep Translator App",
    page_icon="🌐",
    layout="wide"
)

# Sidebar with usage instructions
st.sidebar.title("How to Use")
st.sidebar.markdown(
    "1. Choose the translation playground from the dropdown menu.\n"
    "2. For 'Simple Translate', select the target language and enter text.\n"
    "3. For 'File Translate', upload a file and select the target language.\n"
    "4. Click the 'Translate' button to get the translation result.\n"
    "5. Enjoy exploring different translations!"
)

# Main content
st.title('Deep Translator App')
st.image("images/logo.png", width= 300)
st.subheader('Translate text from any language to any language')

# Selectbox for choosing the translation playground
filed = st.selectbox("Playground", ("Simple-Translate", "File-Translate"))

if filed == "Simple-Translate":
    st.subheader("Simple Translate")
    col1, col2 = st.columns(2)
    
    # Language selection
    with col1:
        languages = list(GoogleTranslator().get_supported_languages())
        choosen_lang = st.selectbox("Choose Target language", languages)

    # Text input
    with col2:
        text = st.text_input("Enter your text")

    if st.button("Translate"):
        # Translation
        translated = GoogleTranslator(source='auto', target=choosen_lang).translate(text=text)
        st.success(translated)

elif filed == "File-Translate":
    st.subheader("File Translate")
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        # Save the uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name

        # Language selection
        languages = list(GoogleTranslator().get_supported_languages())
        choosen_lang = st.selectbox("Choose Target language", languages)

        if st.button("Translate"):
            # Use the temporary file path for translation
            translate = GoogleTranslator(source='auto', target=choosen_lang).translate_file(temp_file_path)
            st.success(translate)

            # Remove the temporary file after translation
            os.remove(temp_file_path)

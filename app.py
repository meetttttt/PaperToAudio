import streamlit as st
import PyPDF2
import utils
import io
from utils import download_pdf_file, pdf_to_text, text_to_audio


def extract_text_from_pdf(pdf_bytes):
    text = ''
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_bytes))
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()
    return text


# Page title
st.title("PaperToAudio Converter")
st.caption('By Meet Nagadia')

# Sidebar with user input
st.sidebar.header("Download PDF")
pdf_url = st.sidebar.text_input("Enter PDF URL:")
convert_button = st.sidebar.button("Convert to PDF")

# Main content area
if convert_button:
    if pdf_url:
        st.info("Downloading PDF...")
        path = download_pdf_file(pdf_url)
        if path:
            st.success("PDF available for downloaded!")
            pdf_data = utils.download_pdf(path)
            st.download_button(
                label="Download Converted PDF",
                data=pdf_data,
                file_name="converted_pdf.pdf",
                mime="application/octet-stream"
            )
        else:
            st.error("Failed to download PDF. Please check the URL and try again.")

# Text to audio conversion
st.header("Text to Audio Conversion")

# Select PDF file for text extraction
pdf_file = st.file_uploader("Upload PDF file for text extraction:", type=["pdf"])

if pdf_file is not None:
    # Read PDF contents
    pdf_contents = pdf_file.read()

    # Use the function to extract text from PDF contents
    text_from_pdf = extract_text_from_pdf(pdf_contents)

    # # Text to audio conversion
    st.info("Converting text to audio...")
    if utils.text_to_audio(text_from_pdf, "output.mp3"):
        st.success("Text to audio conversion successful!")
        # st.audio(output_audio_file, format="audio/mp3", start_time=0)
    else:
        st.error("Failed to convert text to audio. Please try again.")

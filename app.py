import streamlit as st
import PyPDF2
import utils
import io
from utils import download_pdf_file, text_to_audio, download_audio, pdf_to_text


def extract_text_from_pdf(pdf_bytes):
    try:
        text = ''
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_bytes))
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
        return text
    except Exception as e:
        st.error(f"Error: {e}")


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
            st.info("Converting to Audio...")
            text = pdf_to_text(path)
            if text:
                audio_path = text_to_audio(text, "output.mp3")
                if audio_path:
                    st.success("Text to audio conversion successful!")
                    audio_data = download_audio(audio_path)
                    st.audio(audio_data, format="audio/mp3", start_time=0)
                else:
                    st.error("Failed to convert text to audio. Please try again.")
            else:
                st.error("Failed to Read PDF. Please check the URL and PDF and then try again.")
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
    if text_from_pdf:
        st.success("Extracted text from pdf")
        st.info("Converting text to audio...")
        audio_path = text_to_audio(text_from_pdf, "output.mp3")
        if audio_path:
            st.success("Text to audio conversion successful!")
            audio_data = download_audio(audio_path)
            st.audio(audio_data, format="audio/mp3", start_time=0)
        else:
            st.error("Failed to convert text to audio. Please try again.")
    else:
        st.error("Not Able to extract text from the pdf..!")

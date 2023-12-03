import utils
import logging

# Setting up Logging
logging.basicConfig(filename="Log/log.log",
                    format="%(asctime)s - %(message)s",
                    datefmt="%d-%b-%y %H:%M:%S",
                    level=logging.INFO)

try:
    logging.info(f"Starting with main.py...")

    # url to the pdf
    URL = 'https://raw.githubusercontent.com/seraph776/DevCommunity/main/PDFDownloader/assests/the_raven.pdf'
    utils.download_pdf_file(URL)  # download pdf in local
    pdf_path = "pdf_download/the_raven.pdf"  # path to store pdf in local

    audio_output_file = "audio_converted/output.mp3"  # path to store audio in local
    text_content = utils.pdf_to_text(pdf_path)  # extract text from pdf
    utils.text_to_audio(text_content, audio_output_file)  # convert the text to audio

    logging.info(f"Ending main.py...")

except Exception as e:
    logging.info(f"Error in main.py: {e}")

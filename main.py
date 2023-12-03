import utils
import logging

# Setting up Logging
logging.basicConfig(filename="Log/log.log",
                    format="%(asctime)s - %(message)s",
                    datefmt="%d-%b-%y %H:%M:%S",
                    level=logging.INFO)

logging.info(f"Starting with main.py...")
URL = 'https://raw.githubusercontent.com/seraph776/DevCommunity/main/PDFDownloader/assests/the_raven.pdf'
utils.download_pdf_file(URL)
pdf_path = "pdf_download/the_raven.pdf"
audio_output_file = "audio_converted/output.mp3"
text_content = utils.pdf_to_text(pdf_path)
utils.text_to_audio(text_content, audio_output_file)
logging.info(f"Ending main.py...")

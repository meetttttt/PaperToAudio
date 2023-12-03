"""
This is utils file:
- Here we will write all the functions that we need.
"""

import os
import PyPDF2
import logging
import requests

from gtts import gTTS

# Setting up Logging
logging.basicConfig(filename="Log/log.log",
                    format="%(asctime)s - %(message)s",
                    datefmt="%d-%b-%y %H:%M:%S",
                    level=logging.INFO)


def download_pdf_file(url: str):
    """Download PDF from given URL to local directory.

    :param url: The url of the PDF file to be downloaded
    :return: True if PDF file was successfully downloaded, otherwise False.
    """

    pdf_file_name = ""

    try:
        logging.info(f"Started with downloading..")

        # Request URL and get response object
        response = requests.get(url, stream=True)

        if response.status_code == 200:

            # isolate PDF filename from URL
            pdf_file_name += os.path.basename(url)

            # Save in current working directory
            filepath = os.path.join(os.getcwd() + "//pdf_download//", pdf_file_name)

            with open(filepath, 'wb') as pdf_object:
                pdf_object.write(response.content)
                logging.info(f'{pdf_file_name} was successfully saved!')
                return filepath
        else:
            logging.info(f'Uh oh! Could not download {pdf_file_name},')
            logging.info(f'HTTP response status code: {response.status_code}')
            return False

    except Exception as e:
        logging.info(f"Opps, we were not able to download the pdf: {pdf_file_name}")
        logging.info(f"Errr: {e}")


def pdf_to_text(pdf_path: str) -> str:
    """
    This will read the text present in the pdf and return that text
    :param pdf_path: path where pdf is stored
    :return: text extracted from the pdf
    """

    try:
        logging.info(f"Started with the text extraction from the pdf...")

        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            text = ''
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                text += page.extractText()
            logging.info(f"Done extraction the text from the pdf...")
            return text

    except Exception as e:
        logging.info(f"Error while extracting the text..")
        logging.info(f"Error: {e}")


def text_to_audio(text: str, output_file: str):
    """
    This function will convert the text to audio.
    The text will be the text that is extracted from the pdf.
    :param text: the text that needs to be converted into audio
    :param output_file: the audio file generated by the text conversion
    :return: status of the operation
    """
    try:
        logging.info(f"Started with the tex-to-audio")
        tts = gTTS(text=text, lang='en')
        # Save in current working directory
        filepath = os.path.join(os.getcwd() + "//audio_converted//", output_file)
        tts.save(filepath)
        logging.info(f"Done with text-to-audio")
        return filepath

    except Exception as e:
        logging.info(f"Error: {e}")
        return False


# Function to convert PDF
def download_pdf(file_path: str):
    logging.info(f"Staring with the downloading the pdf generating the link...")
    try:
        with open(file_path, 'rb') as file:
            pdf_data = file.read()
        return pdf_data

    except Exception as e:
        logging.info(f"Error while generating the link: {e}")


# Function to convert audio
def download_audio(file_path: str):
    logging.info(f"Staring with the downloading the audio generating the link...")
    try:
        with open(file_path, 'rb') as file:
            pdf_data = file.read()
        return pdf_data

    except Exception as e:
        logging.info(f"Error while generating the link for audio: {e}")


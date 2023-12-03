import utils

URL = 'https://raw.githubusercontent.com/seraph776/DevCommunity/main/PDFDownloader/assests/the_raven.pdf'
utils.download_pdf_file(URL)
pdf_path = "download/the_raven.pdf"
audio_output_file = "output.mp3"
text_content = utils.pdf_to_text(pdf_path)
utils.text_to_audio(text_content, audio_output_file)

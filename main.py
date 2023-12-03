import utils

URL = 'https://arxiv.org/pdf/2311.18000.pdf'
utils.download_pdf_file(URL)
pdf_path = "download/2311.18000.pdf"
audio_output_file = "output1.mp3"
text_content = utils.pdf_to_text(pdf_path)
utils.text_to_audio(text_content, audio_output_file)

import os
from PyPDF2 import PdfReader, PdfWriter

# add your file path
folder_path = 'path/to/your/pdf/files'  
output_folder = os.path.join(folder_path, 'modified_pdfs')
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(folder_path, filename)
        
        with open(pdf_path, 'rb') as file:
            pdf_reader = PdfReader(file)

            if len(pdf_reader.pages) > 1:
                pdf_writer = PdfWriter()

                
                pdf_writer.add_page(pdf_reader.pages[1])

                output_path = os.path.join(output_folder, f'modified_{filename}')
                with open(output_path, 'wb') as output_pdf:
                    pdf_writer.write(output_pdf)

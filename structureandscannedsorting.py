#Pratik
import os
import shutil
import fitz

# Prompt user to enter the input folder path
input_folder = input("Enter the path to the input folder: ")

# Prompt user to enter the path for the structured output folder
output_folder1 = input("Enter the path for the structured output folder: ")

# Prompt user to enter the path for the scanned output folder
output_folder2 = input("Enter the path for the scanned output folder: ")

for filename in os.listdir(input_folder):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(input_folder, filename)
        
        with fitz.open(pdf_path) as doc:
            text = ""
            for page in doc:
                text += page.get_text()
        
        if not text:
            shutil.move(pdf_path, output_folder1)
        else:
            shutil.move(pdf_path, output_folder2)

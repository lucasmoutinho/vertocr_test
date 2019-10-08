# Import libraries 
from PIL import Image 
import pytesseract as ocr
import sys 
import os 

# In windows it's necessary to set the path for pytesseract
ocr.pytesseract.tesseract_cmd = r'C:\Users\thiago.pinho\AppData\Local\Tesseract-OCR\tesseract.exe'
# Creating a text file to write the output 
outfile = "out_text.txt"

# Open the file in append mode so that 
# All contents of all images are added to the same file 
f = open(outfile, "w") 

# Set filename to recognize text from 
filename = "cnh-carteira-nacional-habilitacao" + ".jpg"
    
# Recognize the text as string in image using pytesserct 
text = str(((ocr.image_to_string(Image.open(filename), lang="por")))) 

# The recognized text is stored in variable text 
# Any string processing may be applied on text 
# Here, basic formatting has been done: 
# In many PDFs, at line ending, if a word can't 
# be written fully, a 'hyphen' is added. 
# The rest of the word is written in the next line 
# Eg: This is a sample text this word here GeeksF- 
# orGeeks is half on first line, remaining on next. 
# To remove this, we replace every '-\n' to ''. 
text = text.replace('-\n', '')	 

# Finally, write the processed text to the file. 
f.write(text) 

# Close the file after writing all the text. 
f.close() 

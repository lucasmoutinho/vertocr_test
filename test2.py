# To install tesserocr (https://github.com/sirfz/tesserocr): 
# $ apt-get install tesseract-ocr libtesseract-dev libleptonica-dev pkg-config
# $ pip install tesserocr
# This is a second test with another usage of the api

import tesserocr

print(tesserocr.tesseract_version())  # print tesseract-ocr version
print(tesserocr.get_languages())  # prints tessdata path and list of available languages

# or
print('------------------------------------------------------')
print()
print(tesserocr.file_to_text('sample3.jpg'))
print()
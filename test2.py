# To install tesserocr (https://github.com/sirfz/tesserocr): 
# $ apt-get install tesseract-ocr libtesseract-dev libleptonica-dev pkg-config
# $ pip install tesserocr
# This is a second test with another usage of the api

import tesserocr

print(tesserocr.tesseract_version())  # print tesseract-ocr version
print(tesserocr.get_languages())  # prints tessdata path and list of available languages

images = ['sample1.jpg', 'sample2.jpg', 'sample3.jpg', 'sample4.jpg', 'sample5.jpg', 'sample6.jpg']

for img in images:
    print('------------------------------------------------------')
    print(img.capitalize())
    print()
    print(tesserocr.file_to_text(img))
    print()

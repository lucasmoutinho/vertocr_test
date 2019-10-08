# To install tesserocr (https://github.com/sirfz/tesserocr): 
# $ apt-get install tesseract-ocr libtesseract-dev libleptonica-dev pkg-config
# $ pip install tesserocr

from api_examples import code_tests_ocr

images = ['sample1.jpg', 'sample2.jpg', 'sample3.jpg', 'sample4.jpg', 'sample5.jpg', 'sample6.jpg']

code_tests_ocr(images, 1)
code_tests_ocr(images, 2)
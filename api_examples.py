# To install tesserocr (https://github.com/sirfz/tesserocr): 
# $ apt-get install tesseract-ocr libtesseract-dev libleptonica-dev pkg-config
# $ pip install tesserocr
# Version 1 is the first example usage of the api
# Version 2 is a second test with another usage example of the api

import tesserocr
from tesserocr import PyTessBaseAPI

def code_tests_ocr(images, version):
    if version is 1:
        print("CODE EXAMPLE 1\n")
        with PyTessBaseAPI() as api:
            for img in images:
                api.SetImageFile(img)
                print('------------------------------------------------------')
                print(img.capitalize())
                print()
                print(api.GetUTF8Text())
                print(api.AllWordConfidences())
                print()
    elif version is 2:
        print("CODE EXAMPLE 2\n")
        for img in images:
            print('------------------------------------------------------')
            print(img.capitalize())
            print()
            print(tesserocr.file_to_text(img))
            print()
    else:
        print('WRONG CODE VERSION ERROR')
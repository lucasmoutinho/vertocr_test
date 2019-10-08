# To install tesserocr: 
# $ apt-get install tesseract-ocr libtesseract-dev libleptonica-dev pkg-config
# $ pip install tesserocr

from tesserocr import PyTessBaseAPI

images = ['sample1.jpg', 'sample2.jpg', 'sample3.jpg']

with PyTessBaseAPI() as api:
    for img in images:
        api.SetImageFile(img)
        print('------------------------------------------------------')
        print(img.capitalize())
        print()
        print(api.GetUTF8Text())
        print(api.AllWordConfidences())
        print()
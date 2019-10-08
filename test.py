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
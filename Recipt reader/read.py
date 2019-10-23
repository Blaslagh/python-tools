# -*- coding: utf-8 -*-

def read_recipt(img):
    from PIL import Image
    import pytesseract
    
    # Include tesseract executable in your path
    pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
     
    image = Image.open(img)
     
    image_to_text = pytesseract.image_to_string(image, lang="pol")
     
    # Print the text
    return(image_to_text)


print(read_recipt("C:/users/Adam/Desktop/image.jpg"))
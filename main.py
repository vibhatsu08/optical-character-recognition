import cv2
import pytesseract

number = int(input("enter a number between 1 and 3 :"))

# 
if (number >= 1 and number <= 3):
    if number == 1:
        image = cv2.imread('images/image-1.jpg')
    elif number == 2:
        image = cv2.imread('images/image-2.jpg')
    elif number == 3:
        image = cv2.imread('images/image-3.jpg')
        
# return the text from the image
def OCR(image):
    text = pytesseract.image_to_string(image)
    return text


# get grayscale image
def grayscaleImage(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# thresholding
def thresholdingImage(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

image = grayscaleImage(image)
image = thresholdingImage(image)
print(OCR(image))
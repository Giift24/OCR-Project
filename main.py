import pytesseract
from PIL import Image
import sys

# Prompt the user to enter the path to the image file
image_path = input('Enter the path to the image file: ')

try:
    # Open the image file
    image = Image.open(image_path)
except IOError:
    print("Error opening or loading image file")
    sys.exit()

try:
    # Extract text from image
    text = pytesseract.image_to_string(image)
    # Print the extracted text
    print(text)
except pytesseract.pytesseract.TesseractError as e:
    print("Error: ", e)

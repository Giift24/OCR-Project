import pytesseract
from PIL import Image

# Prompt the user to enter the path to the image file
image_path = input('Enter the path to the image file: ')

# Open the image file
image = Image.open(image_path)

# Extract the text from the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)

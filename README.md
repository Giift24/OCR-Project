# OCR-Project
This code uses the 'pytesseract' library to perform optical character recognition (OCR) on an image file. OCR is the process of extracting text from an image or a scanned document.
Requirements
This code requires the following libraries:
PIL (Python Imaging Library)
'pytesseract'
To install these libraries, you can use pip. Open a terminal and run the following command:
Copy code
pip install pillow 'pytesseract'
Usage
To use this code, follow these steps:
- Clone this repo or download the code file.
- Open a terminal and navigate to the directory where the code file is located.
- Run the code on your machine
- The code will prompt you to enter the path to the image file. Enter the path to the image file you want to process. The image file must be in a format that is supported by the PIL library, such as .png, .jpg, or .bmp.
- The code will extract the text from the image and print it to the terminal.
Additional notes


- This code has only been tested with Python 3. It may not work with older versions of Python.
- The accuracy of the OCR process depends on the quality of the input image and the complexity of the text. The 'pytesseract' library may have difficulty extracting text from images with low resolution or images with background noise.

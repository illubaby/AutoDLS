from PIL import Image
import pytesseract

# Specify the path to your Tesseract OCR executable
# Uncomment and update this if pytesseract is not in PATH
# pytesseract.pytesseract.tesseract_cmd = r'path_to_tesseract_executable'

# Load the image
image_path = 'cropped_center.png'
image = Image.open(image_path)

# Extract text from the image
extracted_text = pytesseract.image_to_string(image)

# Check if the word "continue" is in the extracted text
if "POINT" in extracted_text:
    print("The word 'continue' is present in the image.")
else:
    print("The word 'continue' is NOT present in the image.")
print(extracted_text)
from PIL import Image
import pytesseract
from library.capture import capture_screenshot
from global_variables import *
# Specify the path to your Tesseract OCR executable
# Uncomment and update this if pytesseract is not in PATH
# pytesseract.pytesseract.tesseract_cmd = r'path_to_tesseract_executable'
capture_screenshot(adb_device_id, screenshot_path)
# Load the image
image_path = 'screenshot.png'
# image_path = 'cropped_screenshot.png'
image = Image.open(image_path)

# Extract text from the image
extracted_text = pytesseract.image_to_string(image)

# Check if the word "continue" is in the extracted text
if "Failed to establish" in extracted_text:
    print("The word is present in the image.")
else:
    print("The word is NOT present in the image.")
print(extracted_text)
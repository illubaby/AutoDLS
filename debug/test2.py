import cv2
import numpy as np
import pytesseract
from PIL import Image

def preprocess_for_digits(input_image_path, output_path=None):
    """
    1) Loads the image via OpenCV
    2) Converts to grayscale
    3) Applies a threshold to separate digits from background
    4) (Optional) Applies morphological ops or other transformations
    5) Saves (optional) and returns the processed image (as a PIL Image for Tesseract)
    """
    # Load image using OpenCV
    img = cv2.imread(input_image_path, cv2.IMREAD_COLOR)
    if img is None:
        print(f"Failed to load {input_image_path}")
        return None

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply a threshold (Otsu’s or a fixed threshold)
    # Adjust '127' or use cv2.THRESH_OTSU to find an optimal value
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # (Optional) Erode or dilate if needed:
    # kernel = np.ones((1,1), np.uint8)
    # thresh = cv2.dilate(thresh, kernel, iterations=1)
    # thresh = cv2.erode(thresh, kernel, iterations=1)

    # (Optional) Save processed image for debugging
    if output_path:
        cv2.imwrite(output_path, thresh)

    # Convert back to PIL for pytesseract
    pil_img = Image.fromarray(thresh)
    return pil_img

def read_digits_from_image(input_image_path):
    # Preprocess image for digit recognition
    processed_pil_image = preprocess_for_digits(input_image_path, "debug_processed.png")
    if processed_pil_image is None:
        return None

    # Tesseract config for digits
    custom_config = r"--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789"
    # Explanation:
    # --oem 3 = default engine mode (newest + legacy)
    # --psm 7 = treat the image as a single text line
    # tessedit_char_whitelist=0123456789 = only recognize digits

    # Run Tesseract
    extracted_text = pytesseract.image_to_string(processed_pil_image, config=custom_config)
    extracted_text = extracted_text.strip()
    print("Raw OCR result:", repr(extracted_text))

    # Attempt to parse as number
    try:
        return float(extracted_text)
    except ValueError:
        return None

# Demo usage
if __name__ == "__main__":
    digit_value = read_digits_from_image("cropped_screenshot.png")
    if digit_value is not None:
        if digit_value < 10:
            print(f"Detected {digit_value}, which is less than 10.")
        else:
            print(f"Detected {digit_value}, which is >= 10.")
    else:
        print("Could not detect a numeric value.")

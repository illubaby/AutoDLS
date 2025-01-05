# fsm/tasks.py
from library.capture import crop_screenshot
from global_variables import adb_device_id, screenshot_path
import pytesseract
from PIL import Image, ImageEnhance
import os
import time

# For PreMatch
def down_tier():
    output_path = "cropped_screenshot.png"  # Path to save the cropped screenshot
    crop_box = (167, 693, 784, 811)  # Define the cropping region (left, top, right, bottom
    cropped_path = crop_screenshot(screenshot_path, output_path, crop_box)
    # if cropped_path:
    #     print("Cropping successful.")
    # else:
    #     print("Cropping failed.")
    try:
        image = Image.open(output_path)
        extracted_text = pytesseract.image_to_string(image).upper()

        if "CONCEDE" in extracted_text:
            print("The image contains the word CONCEDE.")
            # Example: tap screen
            adb_command = f"adb -s {adb_device_id} shell input tap 504 749"
            os.system(adb_command)
            time.sleep(2)
            adb_command = f"adb -s {adb_device_id} shell input tap 975 514"
            os.system(adb_command)
            return True
        else:
            return False
    except ValueError:
        print(f"Could not parse a numeric tier from OCR: '{extracted_text}'")
        return None

def check_tier(screenshot_path=None, adb_device_id=None):
    """
    1) If screenshot_path is not given, fallback to the global screenshot_path.
    2) Crop the screenshot to the region containing the tier number.
    3) Convert to grayscale & apply threshold to enhance OCR accuracy.
    4) Use Tesseract with digit-only whitelist to read the number.
    5) Print & return the numeric tier. If < 10 => "less than 10", else ">= 10".
    """
    if screenshot_path is None:
        screenshot_path = globals().get('screenshot_path', 'screenshot.png')
    if adb_device_id is None:
        adb_device_id = globals().get('adb_device_id', 'emulator-5554')

    # Define where to crop for the tier text (left, top, right, bottom)
    crop_box = (218, 270, 264, 302)  
    output_path = "cropped_screenshot.png"

    # 1) Crop the region
    cropped_path = crop_screenshot(screenshot_path, output_path, crop_box)
    if not cropped_path:
        print("Cropping failed or returned None.")
        return None

    # 2) Load cropped image with OpenCV
    img = cv2.imread(output_path, cv2.IMREAD_COLOR)
    if img is None:
        print(f"Could not load {output_path} with OpenCV.")
        return None

    # 3) Convert to grayscale & apply threshold (Otsu)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # (Optional) Save processed image for debugging:
    # cv2.imwrite("debug_processed.png", thresh)

    # 4) Convert thresholded image back to PIL for Tesseract
    pil_img = Image.fromarray(thresh)

    # Tesseract config for digits
    custom_config = r"--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789"
    extracted_text = pytesseract.image_to_string(pil_img, config=custom_config)
    extracted_text = extracted_text.strip()

    # 5) Parse as a float (or int) and compare
    try:
        tier_value = float(extracted_text)
    except ValueError:
        print(f"Could not parse a numeric tier from OCR: '{extracted_text}'")
        return None

    # Print the comparison
    if tier_value < 10:
        print(f"Tier is {tier_value}. It's less than 10.")
    else:
        print(f"Tier is {tier_value}. It's >= 10.")

    # Return the numeric tier value
    return tier_value
        
def is_advertisement(image_path=None):
    try:
        image = Image.open(screenshot_path)
        extracted_text = pytesseract.image_to_string(image).upper()

        if "LIMITED TIME OFFER!" in extracted_text:
            print("The image contains advertisement.")
            # Example: tap screen
            adb_command = f"adb -s {adb_device_id} shell input tap 1115 136"
            os.system(adb_command)
            return True
        else:
            return False
    except Exception as e:
        print(f"Error processing the image: {e}")
        return False
def is_advertisement_1(image_path=None):
    try:
        image = Image.open(screenshot_path)
        extracted_text = pytesseract.image_to_string(image).upper()

        if "DREAM POINT BOOSTS" in extracted_text:
            print("The image contains advertisement 1.")
            # Example: tap screen
            adb_command = f"adb -s {adb_device_id} shell input tap 1373 138"
            os.system(adb_command)
            time.sleep(2)
            adb_command = f"adb -s {adb_device_id} shell input tap 403 413"
            os.system(adb_command)
            return True
        else:
            return False
    except Exception as e:
        print(f"Error processing the image: {e}")
        return False
def is_new_tier(image_path=None):
    output_path = "cropped_screenshot.png"  # Path to save the cropped screenshot
    crop_box = (380, 332, 1212, 564)  # Define the cropping region (left, top, right, bottom
    cropped_path = crop_screenshot(screenshot_path, output_path, crop_box)
    try:
        image = Image.open(cropped_path)
        extracted_text = pytesseract.image_to_string(image)
        if "champion" in extracted_text or "relegated" in extracted_text:
            print("The image contains new tier")
            # Example: tap screen
            os.system(f"adb -s {adb_device_id} shell input tap 797 544")
            time.sleep(1)
            os.system(f"adb -s {adb_device_id} shell input tap 403 413")
            return True
        else:
            return False
    except Exception as e:
        print(f"Error processing the image: {e}")
        return False
# ======================For LiveMatch =========================

def is_continue(image_path=None):
    output_path = "cropped_screenshot.png"  # Path to save the cropped screenshot
    crop_box = (1287, 815, 1569, 880)  # Define the cropping region (left, top, right, bottom
    cropped_path = crop_screenshot(screenshot_path, output_path, crop_box)
    # if cropped_path:
    #     print("Cropping successful.")
    # else:
    #     print("Cropping failed.")
    try:
        image = Image.open(output_path)
        extracted_text = pytesseract.image_to_string(image).upper()

        if "CONTINUE" in extracted_text:
            print("The image contains the word CONTINUE.")
            # Example: tap screen
            adb_command = f"adb -s {adb_device_id} shell input tap 1464 846"
            os.system(adb_command)
            return True
        else:
            return False
    except Exception as e:
        print(f"Error processing the image: {e}")
        return False
def is_forfeits(image_path=None):
    try:
        image = Image.open(screenshot_path)
        extracted_text = pytesseract.image_to_string(image)
        if "forfeits" in extracted_text or "concedes" in extracted_text or "lost" in extracted_text:
            print("The image contains new forfeits")
            # Example: tap screen
            os.system(f"adb -s {adb_device_id} shell input tap 799 508")
            return True
        else:
            return False
    except Exception as e:
        print(f"Error processing the image: {e}")
        return False
def fix_state():
    output_path = "cropped_screenshot.png"  # Path to save the cropped screenshot
    crop_box = (1339, 0, 1511, 31)  # Define the cropping region (left, top, right, bottom
    cropped_path = crop_screenshot(screenshot_path, output_path, crop_box)
    # if cropped_path:
    #     print("Cropping successful.")
    # else:
    #     print("Cropping failed.")
    try:
        image = Image.open(output_path)
        extracted_text = pytesseract.image_to_string(image).upper()

        if "OUT DI THANG NGU" in extracted_text:
            print("The state is LiveEvents.")
            # Example: tap screen
            adb_command = f"adb -s {adb_device_id} shell input tap 1464 846"
            os.system(adb_command)
            return True
        else:
            return False
    except Exception as e:
        print(f"Error processing the image: {e}")
        return False

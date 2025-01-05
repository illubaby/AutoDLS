# fsm/model.py
from PIL import Image
import pytesseract
import os
from global_variables import adb_device_id, screenshot_path
from library.capture import crop_screenshot, capture_screenshot
import cv2
import time
class GameModel:
    """
    Holds condition methods and any other data relevant to the state machine.
    """
    def __init__(self):
        # Keep track of how many times we've seen "CONTINUE"
        self.continue_count = 0
        self.tier = 13
    def check_tier(self, screenshot_path=None, adb_device_id=None):
        """
        1) If screenshot_path is not given, fallback to the global screenshot_path.
        2) Crop the screenshot to the region containing the tier number.
        3) Convert to grayscale & apply threshold to enhance OCR accuracy.
        4) Use Tesseract with digit-only whitelist to read the number.
        5) Store and return the numeric tier in self.tier.
        """

        # Fallbacks if None provided
        if screenshot_path is None:
            screenshot_path = globals().get('screenshot_path', 'screenshot.png')
        if adb_device_id is None:
            adb_device_id = globals().get('adb_device_id', 'emulator-5554')

        # 1) Define where to crop for the tier text (left, top, right, bottom)
        crop_box = (218, 270, 264, 302)
        output_path = "cropped_screenshot.png"

        # Crop the region
        cropped_path = crop_screenshot(screenshot_path, output_path, crop_box)
        if not cropped_path:
            print("Cropping failed or returned None.")
            return None

        # 2) Load cropped image with OpenCV
        img = cv2.imread(output_path, cv2.IMREAD_COLOR)
        if img is None:
            print(f"Could not load {output_path} with OpenCV.")
            return None

        # 3) Convert to grayscale & apply Otsu threshold
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # 4) Convert thresholded image back to PIL for Tesseract
        pil_img = Image.fromarray(thresh)

        # Tesseract config for digits
        custom_config = r"--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789"
        extracted_text = pytesseract.image_to_string(pil_img, config=custom_config)
        extracted_text = extracted_text.strip()

        # 5) Parse as a float (or int), store in self.tier
        try:
            tier_value = float(extracted_text)
            self.tier = tier_value
            print(f"Detected tier: {tier_value}")
            return tier_value
        except ValueError:
            print(f"Could not parse a numeric tier from OCR: '{extracted_text}'")
            return None
    @staticmethod
    def is_LiveEvents_end_cond(image_path=None):
        """
        Checks if the given image contains the words 'SCORED' and 'CONCEDED'.

        Args:
            image_path (str): Path to the screenshot image (default is screenshot_path from global_variables).

        Returns:
            bool: True if 'SCORED' and 'CONCEDED' is found, False otherwise.
        """
        if image_path is None:
            # fallback to a default if not provided
            image_path = screenshot_path

        try:
            image = Image.open(image_path)
            extracted_text = pytesseract.image_to_string(image).upper()

            if "SCORED" in extracted_text and "CONCEDED" in extracted_text:
                print("The image contains the word 'SCORED' and 'CONCEDED'.")
                # Example: tap screen
                adb_command = f"adb -s {adb_device_id} shell input tap 403 413"
                os.system(adb_command)
                return True
            else:
                return False
        except Exception as e:
            print(f"Error processing the image: {e}")
            return False
    def is_LiveMatch_end_cond(self, image_path=None):
        """
        Checks if 'CONTINUE' appears in the cropped screenshot. If it does:
        1) Tap the 'CONTINUE' button
        2) Capture (or open) a new screenshot
        3) Check if 'MULTIPLIER' is present
            -> if yes, return True for the transition from LiveEvents_Match to LiveEvents_PreMatch
            -> otherwise, return False
        """
        output_path = "cropped_screenshot.png"    # Path to save the cropped screenshot
        crop_box = (1287, 815, 1569, 880)         # (left, top, right, bottom) region for "CONTINUE"
        
        # If no custom image path is provided, use the global screenshot_path
        if image_path is None:
            image_path = screenshot_path

        # 1) Crop the screenshot for "CONTINUE"
        cropped_path = crop_screenshot(image_path, output_path, crop_box)
        if not cropped_path:
            # Crop failed for some reason
            return False

        try:
            # Check if the cropped image has "CONTINUE"
            with Image.open(output_path) as image:
                extracted_text = pytesseract.image_to_string(image).upper()

            if "CONTINUE" in extracted_text:
                print("Detected 'CONTINUE' in the cropped region. Tapping on screen...")
                # Tap the "CONTINUE" button
                adb_command = f"adb -s {adb_device_id} shell input tap 1464 846"
                os.system(adb_command)

                # 2) After tapping, optionally capture a NEW screenshot 
                #    so we can check for "MULTIPLIER" in the updated screen.                
                time.sleep(5)
                capture_screenshot(adb_device_id, screenshot_path)
                cropped_path = crop_screenshot(image_path, output_path, crop_box)
                # 3) Check if the new screenshot has "MULTIPLIER"
                with Image.open(cropped_path) as new_image:
                    new_extracted_text = pytesseract.image_to_string(new_image).upper()
                if "CONTINUE" not in new_extracted_text:
                    print("Trigger FSM transition.")
                    return True
                else:
                    print("Transition not triggered.")
                    return False

            # "CONTINUE" wasn't found in the cropped region -> no tap, no transition
            return False

        except Exception as e:
            print(f"Error in is_LiveMatch_end_cond: {e}")
            return False

    def is_disconnected_cond(image_path=None):
        try:
            image = Image.open(screenshot_path)
            extracted_text = pytesseract.image_to_string(image).upper()

            if "DISCONNECTED" in extracted_text:
                print("The image contains the word DISCONNECTED.")
                # Example: tap screen
                adb_command = f"adb -s {adb_device_id} shell input tap 784 463"
                os.system(adb_command)
                time.sleep(1)
                adb_command = f"adb -s {adb_device_id} shell input tap 403 413"
                os.system(adb_command)
                return True
            else:
                return False
        except Exception as e:
            print(f"Error processing the image: {e}")
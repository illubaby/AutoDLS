# fsm/model.py
from PIL import Image
import pytesseract
import os
from global_variables import adb_device_id, screenshot_path
from library.capture import crop_screenshot, capture_screenshot
import cv2
import time
from fsm.tasks import is_continue, is_advertisement,is_advertisement_1, is_new_tier, is_quickly_end, down_tier, is_disconnected,is_disconnected_1,is_disconnected_2, enter_match, is_advertisement_2, is_advertisement_3, is_play, is_play_1, is_resume
class GameModel:
    """
    Holds condition methods and any other data relevant to the state machine.
    """
    def __init__(self):
        self.tier = 13
    def is_LiveMatch_cond(self, screenshot_path=None, adb_device_id=None):
        """
        Checks and updates the tier based on OCR results from a screenshot.
        Returns True if the tier was updated successfully, False otherwise.
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
            return False

        # 2) Load cropped image with OpenCV
        img = cv2.imread(output_path, cv2.IMREAD_COLOR)
        if img is None:
            return False

        # 3) Convert to grayscale & apply Otsu threshold
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # 4) Convert thresholded image back to PIL for Tesseract
        pil_img = Image.fromarray(thresh)

        # Tesseract config for digits
        custom_config = r"--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789"
        extracted_text = pytesseract.image_to_string(pil_img, config=custom_config).strip()

        # 5) Parse as a float (or int) and update the tier
        try:
            tier_value = float(extracted_text)
            if hasattr(self, 'tier') and self.tier == tier_value:
                return False  # No update needed
            self.tier = tier_value
            return False
        except ValueError:
            print("This is Live Match !")
            return True

    @staticmethod

    def is_LiveEvents_cond(image_path=None):
        output_path = "cropped_screenshot.png"  # Path to save the cropped screenshot
        crop_box = (1341, 5, 1502, 28)  # Define the cropping region (left, top, right, bottom
        cropped_path = crop_screenshot(screenshot_path, output_path, crop_box)
        # if cropped_path:
        #     print("Cropping successful.")
        # else:
        #     print("Cropping failed.")
        try:
            image = Image.open(output_path)
            extracted_text = pytesseract.image_to_string(image)

            if "OUT DI THANG NGU" in extracted_text:
                print("This is Live Events.")
                return True
            else:
                return False
        except Exception as e:
            print(f"Error processing the image: {e}")
            return False
    def is_CareerPreMatch_cond(self):
        output_path = "cropped_screenshot.png"  # Path to save the cropped screenshot
        crop_box = (1341, 5, 1502, 28)  # Define the cropping region (left, top, right, bottom
        cropped_path = crop_screenshot(screenshot_path, output_path, crop_box)
        # if cropped_path:
        #     print("Cropping successful.")
        # else:
        #     print("Cropping failed.")
        try:
            image = Image.open(output_path)
            extracted_text = pytesseract.image_to_string(image)

            if "OUT DI THANG NGU" in extracted_text:
                print("This is CareerPreMatch.")
                return True
            else:
                return False
        except Exception as e:
            print(f"Error processing the image: {e}")
            return False
    def on_enter_LiveEvents_PreMatch(self):
        print("Entered LiveEvents_PreMatch.")
        try:
            self.is_LiveMatch()
        except Exception as e:
            print(f"An error occurred: {e}")
        enter_match()
        is_advertisement()
        is_advertisement_1()
        is_advertisement_2()
        is_new_tier()
        is_disconnected()
        is_disconnected_2()
    def on_enter_LiveEvents_Match(self):
        """
        Called when entering the 'LiveEvents_Match' state.
        """
        print("Entered LiveEvents_Match.")
        try:
            self.is_LiveEvents()
        except Exception as e:
            print(f"An error occurred: {e}")
        # if model.tier < 11:
        #     down_tier()
        is_continue()
        is_quickly_end()
        is_disconnected_1()
    def on_enter_Career_CareerPreMatch(self):
        """
        Called when entering the 'Career_CareerPreMatch' state.
        """
        print("Entered CareerPreMatch.")
        if not self.is_CareerPreMatch_cond():
            print("This is not CareerPreMatch.")
            self.state = "Career_CareerMatch"
        is_advertisement_3()
        is_play()
        is_play_1()
        
    def on_enter_Career_CareerMatch(self):
        """
        Called when entering the 'Career_CareerMatch' state.
        """
        print("Entered CareerMatch.")
        try: 
            self.is_CareerPreMatch()
        except Exception as e:
            print(f"An error occurred: {e}")
        is_continue()
        is_resume()
        
        
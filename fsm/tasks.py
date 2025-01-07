# fsm/tasks.py
from library.capture import crop_screenshot, capture_screenshot
from global_variables import adb_device_id, screenshot_path
import pytesseract
from PIL import Image, ImageEnhance
import os
import time
import cv2
#                          _      _             _____            __  __       _       _                            
#                         | |    (_)           |  __ \          |  \/  |     | |     | |                           
#   ______ ______ ______  | |     ___   _____  | |__) | __ ___  | \  / | __ _| |_ ___| |__    ______ ______ ______ 
#  |______|______|______| | |    | \ \ / / _ \ |  ___/ '__/ _ \ | |\/| |/ _` | __/ __| '_ \  |______|______|______|
#                         | |____| |\ V /  __/ | |   | | |  __/ | |  | | (_| | || (__| | | |                       
#                         |______|_| \_/ \___| |_|   |_|  \___| |_|  |_|\__,_|\__\___|_| |_|                       
                                                                                                                 
                                                                                                                                                              
def enter_match():
    """
    Checks if the given image contains the words 'SCORED' and 'CONCEDED'.

    Args:
        image_path (str): Path to the screenshot image (default is screenshot_path from global_variables).

    Returns:
        bool: True if 'SCORED' and 'CONCEDED' is found, False otherwise.
    """
    try:
        image = Image.open(screenshot_path)
        extracted_text = pytesseract.image_to_string(image).upper()
        
        if "SCORED" in extracted_text and "CONCEDED" in extracted_text:
            print("The image contains the word 'SCORED' and 'CONCEDED'.")
            # Example: tap screen
            if adb_device_id is not None:
                adb_command = f"adb -s {adb_device_id} shell input tap 403 413"
                os.system(adb_command)
            else:
                print("adb_device_id is not set.")
            return True
        else:
            return False
    except Exception as e:
        print(f"Error processing the image: {e}")
        return False
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
            return True
        else:
            return False
    except Exception as e:
        print(f"Error processing the image: {e}")
        return False
def is_advertisement_2(image_path=None):
    try:
        image = Image.open(image_path if image_path else screenshot_path)
        extracted_text = pytesseract.image_to_string(image).upper()

        if "ACTIVATE" in extracted_text and "PASS!" in extracted_text:
            print("The image contains advertisement 2.")
            # Example: tap screen
            if adb_device_id is not None:
                adb_command = f"adb -s {adb_device_id} shell input tap 1522 97"
                os.system(adb_command)
            else:
                print("adb_device_id is not set.")
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
        if "champion" in extracted_text or "relegated" in extracted_text or "promotion" in extracted_text or "relegation" in extracted_text:
            print("The image contains new tier")
            # Example: tap screen
            os.system(f"adb -s {adb_device_id} shell input tap 797 544")
            return True
        else:
            return False
    except Exception as e:
        print(f"Error processing the image: {e}")
        return False
def is_disconnected(image_path=None):
    try:
        image = Image.open(screenshot_path)
        extracted_text = pytesseract.image_to_string(image).upper()

        if "DISCONNECTED" in extracted_text:
            print("The image contains the word DISCONNECTED.")
            # Example: tap screen
            adb_command = f"adb -s {adb_device_id} shell input tap 784 463"
            os.system(adb_command)
            return True
        elif "FAILED TO ESTABLISH" in extracted_text:
            print("The image contains the word FAILED TO ESTABLISH.")
            # Example: tap screen
            adb_command = f"adb -s {adb_device_id} shell input tap 782 538"
            os.system(adb_command)
            return True
        elif "NOT STABLE" in extracted_text:
            print("The image contains the word NOT STABLE.")
            # Example: tap screen
            adb_command = f"adb -s {adb_device_id} shell input tap 782 538"
            os.system(adb_command)
            return True
        else:   
            return False
    except Exception as e:
        print(f"Error processing the image: {e}")

#                          _      _           __  __       _       _                            
#                         | |    (_)         |  \/  |     | |     | |                           
#   ______ ______ ______  | |     ___   _____| \  / | __ _| |_ ___| |__    ______ ______ ______ 
#  |______|______|______| | |    | \ \ / / _ \ |\/| |/ _` | __/ __| '_ \  |______|______|______|
#                         | |____| |\ V /  __/ |  | | (_| | || (__| | | |                       
#                         |______|_| \_/ \___|_|  |_|\__,_|\__\___|_| |_|                       
                                                                                              
                                                                                                                                                                                             
                                                
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
            capture_screenshot(adb_device_id, screenshot_path)
            with Image.open(screenshot_path) as new_image:
                new_extracted_text = pytesseract.image_to_string(new_image)
        if "You" in new_extracted_text:
            print("Someone forfeit the match.")
            adb_command = f"adb -s {adb_device_id} shell input tap 793 501"
            os.system(adb_command)
            return True
        else:
            return False
    except Exception as e:
        print(f"Error processing the image: {e}")
        return False
def is_quickly_end(image_path=None):
    try:
        image = Image.open(screenshot_path)
        extracted_text = pytesseract.image_to_string(image)
        if "forfeits" in extracted_text or "concedes" in extracted_text or "lost" in extracted_text:
            print("The match end quickly !")
            # Example: tap screen
            os.system(f"adb -s {adb_device_id} shell input tap 799 508")
            return True
        else:
            return False
    except Exception as e:
        print(f"Error processing the image: {e}")
        return False
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
            adb_command = f"adb -s {adb_device_id} shell input tap 504 749"
            os.system(adb_command)
            time.sleep(2)
            # Perform 2 click because the second click is to confirm the action
            adb_command = f"adb -s {adb_device_id} shell input tap 975 514"
            os.system(adb_command)
            return True
        else:
            return False
    except ValueError:
        print(f"Could not parse a numeric tier from OCR: '{extracted_text}'")
        return None

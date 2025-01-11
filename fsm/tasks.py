# fsm/tasks.py
from library.capture import crop_screenshot, capture_screenshot
from global_variables import adb_device_id, screenshot_path
import pytesseract
from PIL import Image, ImageEnhance
import os
import time
import cv2
import sys
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
        extracted_text = pytesseract.image_to_string(image)
        
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
        extracted_text = pytesseract.image_to_string(image)

        if "LIMITED TIME OFFER!" in extracted_text:
            print("The image contains advertisement.")
            # Example: tap screen
            adb_command = f"adb -s {adb_device_id} shell input tap 1115 136"
            os.system(adb_command)
            return True
        elif "TIME REMAINING FORM" in extracted_text:
            print("Leave the champion event.")
            # Example: tap screen
            adb_command = f"adb -s {adb_device_id} shell input tap 53 37"
            os.system(adb_command)
            return True
        elif "LEADERBOARD" in extracted_text:
            print("The image contains advertisement.")
            # Example: tap screen
            adb_command = f"adb -s {adb_device_id} shell input tap 1483 134"
            os.system(adb_command)
            return True
        elif "PREMIUM SEASON PASS" in extracted_text:
            print("PREMIUM SEASON PASS.")
            # Example: tap screen
            adb_command = f"adb -s {adb_device_id} shell input tap 1360 91"
            os.system(adb_command)
            return True
        elif "DREAM POINT BOOSTS" in extracted_text:
            print("DREAM POINT BOOSTS.")
            # Example: tap screen
            adb_command = f"adb -s {adb_device_id} shell input tap 1373 138"
            os.system(adb_command)
            return True
        elif ("ACTIVATE" in extracted_text and "PASS!" in extracted_text):
            print("The image contains advertisement 2.")
            # Example: tap screen
            if adb_device_id is not None:
                adb_command = f"adb -s {adb_device_id} shell input tap 1522 97"
                os.system(adb_command)
            else:
                print("adb_device_id is not set.")
            return True
        elif "SPECIAL OFFER!" in extracted_text:
            print("The image contains advertisement.")
            # Example: tap screen
            adb_command = f"adb -s {adb_device_id} shell input tap 1115 142"
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
        extracted_text = pytesseract.image_to_string(image)
        if "disconnected" in extracted_text:
            print("The image contains the word DISCONNECTED.")
            adb_command = f"adb -s {adb_device_id} shell input tap 784 463"
            os.system(adb_command)
            return True
        elif "Failed to establish" in extracted_text or "Failed to connect" in extracted_text:
            print("Disconnected.")
            # Example: tap screen
            adb_command = f"adb -s {adb_device_id} shell input tap 782 538"
            os.system(adb_command)
            return True
        elif "not stable" in extracted_text or "error" in extracted_text:
            print("Disconnected.")
            # Example: tap screen
            adb_command = f"adb -s {adb_device_id} shell input tap 782 538"
            os.system(adb_command)
            return True
        elif "You" in extracted_text and "match" in extracted_text:
            print("You forfeit the match.")
            adb_command = f"adb -s {adb_device_id} shell input tap 795 501"
            os.system(adb_command)
            return True
        elif "communicating" in extracted_text:
            print("The image contains the word communicating.")
            adb_command = f"adb -s {adb_device_id} shell input tap 584 542"
            os.system(adb_command)
            return True
        elif "The match" in extracted_text or "You forfeit the match" in extracted_text:
            print("The match has been abandoned.")
            adb_command = f"adb -s {adb_device_id} shell input tap 812 501"
            os.system(adb_command)
            return True       
        else:
            return False
    except Exception as e:
        print(f"Error processing the image: {e}")
def is_disconnected_1(image_path=None):
    output_path = "cropped_screenshot.png"  # Path to save the cropped screenshot
    crop_box = (571, 405, 1021, 446)  # Define the cropping region (left, top, right, bottom
    cropped_path = crop_screenshot(screenshot_path, output_path, crop_box)
    # if cropped_path:
    #     print("Cropping successful.")
    # else:
    #     print("Cropping failed.")
    try:
        image = Image.open(output_path)
        extracted_text = pytesseract.image_to_string(image)

        if "Lost connection" in extracted_text:
            print("The image contains the word lost connection.")
            # Example: tap screen
            adb_command = f"adb -s {adb_device_id} shell input tap 805 497"
            os.system(adb_command)
            return True
        else:
            return False
    except Exception as e:
        print(f"Error processing the image: {e}")
        return False
def is_100_games():
    try:
        image = Image.open(screenshot_path)
        extracted_text = pytesseract.image_to_string(image)
        if "You've played 100 games today." in extracted_text:
            print("The image contains 100 games.")
            # Close the BlueStacks app
            adb_command_close_app = f"taskkill /IM HD-Player.exe /F"
            os.system(adb_command_close_app)
            
            print("BlueStacks app closed.")
            # Exit the current Python script
            print("Exiting the script.")
            sys.exit(0)
        
            return True
        else:
            return False
    except Exception as e:
        print(f"Error processing the image: {e}")
        return False
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
        extracted_text = pytesseract.image_to_string(image)

        if "CONTINUE" in extracted_text:
            print("The image contains the word continue.")
            # Example: tap screen
            adb_command = f"adb -s {adb_device_id} shell input tap 1464 846"
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
        if "forfeits" in extracted_text or "concedes" in extracted_text or "lost" in extracted_text or ("Your" in extracted_text and "match" in extracted_text):
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
        extracted_text = pytesseract.image_to_string(image)

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
def is_live_season():
    try:
        image = Image.open(screenshot_path)
        extracted_text = pytesseract.image_to_string(image)
        if "LIVE" in extracted_text or "SEASON" in extracted_text:
            print("Enter Live Event.")
            # Example: tap screen
            os.system(f"adb -s {adb_device_id} shell input tap 401 570")
            return True
        else:
            return False
    except Exception as e:
        print(f"Error processing the image: {e}")
        return False
def is_sign_out():
    try:
        image = Image.open(screenshot_path)
        extracted_text = pytesseract.image_to_string(image)
        if "You have been signed out" in extracted_text:
            print("Continue to sign in again.")
            # Example: tap screen
            adb_command = f"adb -s {adb_device_id} shell input tap 790 557"
            os.system(adb_command)
            return True
        else:
            return False
    except Exception as e:
        print(f"Error processing the image: {e}")
#    _____                         _____          __  __       _       _     
#   / ____|                       |  __ \        |  \/  |     | |     | |    
#  | |     __ _ _ __ ___  ___ _ __| |__) | __ ___| \  / | __ _| |_ ___| |__  
#  | |    / _` | '__/ _ \/ _ \ '__|  ___/ '__/ _ \ |\/| |/ _` | __/ __| '_ \ 
#  | |___| (_| | | |  __/  __/ |  | |   | | |  __/ |  | | (_| | || (__| | | |
#   \_____\__,_|_|  \___|\___|_|  |_|   |_|  \___|_|  |_|\__,_|\__\___|_| |_|                                                                           

def is_play():
    output_path = "cropped_screenshot.png"  # Path to save the cropped screenshot
    crop_box = (29, 112, 128, 181)  # Define the cropping region (left, top, right, bottom
    cropped_path = crop_screenshot(screenshot_path, output_path, crop_box)
    # if cropped_path:
    #     print("Cropping successful.")
    # else:
    #     print("Cropping failed.")
    try:
        image = Image.open(output_path)
        extracted_text = pytesseract.image_to_string(image)

        if "PLAY" in extracted_text or "NOW" in extracted_text:
            print("The image contains the word play.")
            # Example: tap screen
            adb_command = f"adb -s {adb_device_id} shell input tap 358 261"
            os.system(adb_command)
            return True
        else:
            return False
    except Exception as e:
        print(f"Error processing the image: {e}")
        return False
def is_play_1():
    output_path = "cropped_screenshot.png"  # Path to save the cropped screenshot
    crop_box = (1408, 828, 1517, 869)  # Define the cropping region (left, top, right, bottom
    cropped_path = crop_screenshot(screenshot_path, output_path, crop_box)
    # if cropped_path:
    #     print("Cropping successful.")
    # else:
    #     print("Cropping failed.")
    try:
        image = Image.open(output_path)
        extracted_text = pytesseract.image_to_string(image)

        if "PLAY" in extracted_text :
            print("The image contains the word play.")
            # Example: tap screen
            adb_command = f"adb -s {adb_device_id} shell input tap 1444 846"
            os.system(adb_command)
            return True
        else:
            return False
    except Exception as e:
        print(f"Error processing the image: {e}")
        return False
def is_resume():
    output_path = "cropped_screenshot.png"  # Path to save the cropped screenshot
    crop_box = (1113, 732, 1268, 768)  # Define the cropping region (left, top, right, bottom
    cropped_path = crop_screenshot(screenshot_path, output_path, crop_box)
    # if cropped_path:
    #     print("Cropping successful.")
    # else:
    #     print("Cropping failed.")
    try:
        image = Image.open(output_path)
        extracted_text = pytesseract.image_to_string(image)

        if "RESUME" in extracted_text :
            print("The image contains the word RESUME.")
            # Example: tap screen
            adb_command = f"adb -s {adb_device_id} shell input tap 1165 744"
            os.system(adb_command)
            return True
        else:
            return False
    except Exception as e:
        print(f"Error processing the image: {e}")
        return False                                                                                                                                                                
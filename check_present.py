import cv2
import numpy as np
import os
from global_variables import *
from PIL import Image
import pytesseract
# Specify your ADB device ID (replace with the actual device ID from `adb devices`)
adb_device_id = "emulator-5554"

def detect_template_and_tap(screenshot_path, template_path, adb_device_id, threshold=0.8):
    """
    Detect a template in a screenshot and tap on the detected location using ADB.

    Args:
        screenshot_path (str): Path to the screenshot image.
        template_path (str): Path to the template image.
        adb_device_id (str): The ADB device ID (use `adb devices` to get this).
        threshold (float): Matching threshold (default is 0.8).

    Returns:
        bool: True if the template was detected and tapped, False otherwise.
    """
    # Load the screenshot and the template
    screenshot = cv2.imread(screenshot_path, 0)  # Load screenshot in grayscale
    template = cv2.imread(template_path, 0)  # Load template in grayscale

    if screenshot is None or template is None:
        raise ValueError("Screenshot or template image not found. Check paths.")

    # Perform template matching
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Check if the match exceeds the threshold
    if max_val >= threshold:
        print("Template detected!")
        print(f"Location: {max_loc}")
        # Tap on the detected location using ADB
        x, y = max_loc
        adb_tap_command = f"adb -s {adb_device_id} shell input tap {x} {y}"
        os.system(adb_tap_command)  # Execute the ADB command
        print(f"Tapped on location: ({x}, {y})")
        return True
    else:
        print("Template not detected.")
        return False
def crop_center(image_path, output_path, crop_width, crop_height):
    # Open the image
    image = Image.open(image_path)
    width, height = image.size

    # Calculate cropping box
    left = (width - crop_width) // 2
    top = (height - crop_height) // 2
    right = left + crop_width
    bottom = top + crop_height

    # Crop the image
    cropped_image = image.crop((left, top, right, bottom))
    cropped_image.save(output_path)
    return output_path

def is_OK(adb_device_id):
    # Paths for full screenshot and cropped image
    screenshot_path = "screenshot.png"
    cropped_path = "cropped_center.png"

    # Crop the center of the screenshot
    crop_width, crop_height = 1000, 300  # Adjust these values as needed
    crop_center(screenshot_path, cropped_path, crop_width, crop_height)

    # Extract text from the cropped image
    extracted_text = pytesseract.image_to_string(cropped_path)

    # Check for the word "OKE"
    if "OK" in extracted_text.upper():
        print("The word 'OK' is present in the image.")
        # Simulate a tap at a fixed position (adjust as needed)
        adb_command = f"adb -s {adb_device_id} shell input tap 782 499"
        os.system(adb_command)
        return True
    else:
        return False
def is_promotion(adb_device_id):
        # Paths for full screenshot and cropped image
    screenshot_path = "screenshot.png"
    cropped_path = "cropped_center.png"

    # Extract text from the cropped image
    extracted_text = pytesseract.image_to_string(cropped_path)
    # Check for the word "OKE"
    if "promotion" in extracted_text:
        print("The word 'promotion' is present in the image.")
        # Simulate a tap at a fixed position (adjust as needed)
        adb_command = f"adb -s {adb_device_id} shell input tap 782 499"
        os.system(adb_command)
        return True
    else:
        return False
def is_champion(adb_device_id):
        # Paths for full screenshot and cropped image
    screenshot_path = "screenshot.png"
    cropped_path = "cropped_center.png"

    # Extract text from the cropped image
    extracted_text = pytesseract.image_to_string(cropped_path)
    # Check for the word "OKE"
    if "champion" in extracted_text:
        print("The word 'champion' is present in the image.")
        # Simulate a tap at a fixed position (adjust as needed)
        adb_command = f"adb -s {adb_device_id} shell input tap 788 540"
        os.system(adb_command)
        return True
    else:
        return False
# Example usage
def is_LiveEvents(adb_device_id):
    # Load the image
    image_path = 'screenshot.png'
    image = Image.open(image_path)

    # Extract text with bounding box information
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

    # Iterate through the data to find the word "CONTINUE"
    for i in range(len(data['text'])):
        if data['text'][i].strip().upper() == "SCORED":
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            print(f"The word 'CONTINUE' is present at location: ({x}, {y}), width: {w}, height: {h}.")

            # Calculate the center of the bounding box
            center_x = x + w // 2 - 200
            center_y = y + h // 2
            print(f"Simulating touch at: ({center_x}, {center_y})")

            # Send ADB command to tap at the calculated position
            adb_command = f"adb -s {adb_device_id} shell input tap {center_x} {center_y}"
            os.system(adb_command)
            print(f"ADB Command Executed: {adb_command}")
            return True  # Word found and tapped
    return False  # Word not found
def is_limited_time_offer(adb_device_id):
            # Extract text from the image
    image_path = 'screenshot.png'
    extracted_text = pytesseract.image_to_string(image_path)

    # Check if the word "continue" is in the extracted text
    if "OFFER!" in extracted_text:
        print("The word 'OFFER!' is present in the image.")
        # Send ADB command to tap at the calculated position
        adb_command = f"adb -s {adb_device_id} shell input tap 1117 138"
        os.system(adb_command)

def is_opponent_forfeit(adb_device_id):
            # Extract text from the image
    image_path = 'screenshot.png'
    extracted_text = pytesseract.image_to_string(image_path)

    # Check if the word "continue" is in the extracted text
    if "forfeits" in extracted_text or "opponent" in extracted_text:
        print("The word 'forfeits' is present in the image.")
        # Send ADB command to tap at the calculated position
        adb_command = f"adb -s {adb_device_id} shell input tap 803 504"
        os.system(adb_command)
def is_season(adb_device_id):
            # Extract text from the image
    image_path = 'screenshot.png'
    extracted_text = pytesseract.image_to_string(image_path)

    # Check if the word "continue" is in the extracted text
    if "SEASON" in extracted_text:
        print("The word 'SEASON' is present in the image.")
        # Send ADB command to tap at the calculated position
        adb_command = f"adb -s {adb_device_id} shell input tap 1365 91"
        os.system(adb_command)
        
def is_dream_point_boost(adb_device_id):
        # Extract text from the image
    image_path = 'screenshot.png'
    extracted_text = pytesseract.image_to_string(image_path)

    # Check if the word "continue" is in the extracted text
    if "POINT" in extracted_text:
        print("The word 'POINT' is present in the image.")
        # Send ADB command to tap at the calculated position
        adb_command = f"adb -s {adb_device_id} shell input tap 1380 149"
        os.system(adb_command)
def is_advertisement(adb_device_id):
        # Load the image
    image_path = 'screenshot.png'
    image = Image.open(image_path)

    # Extract text with bounding box information
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

    # Iterate through the data to find the word "CONTINUE"
    for i in range(len(data['text'])):
        if data['text'][i].strip().upper() == "FREE":
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            print(f"The word 'FREE' is present at location: ({x}, {y}), width: {w}, height: {h}.")

            # Send ADB command to tap at the calculated position
            adb_command = f"adb -s {adb_device_id} shell input tap 1554 37"
            os.system(adb_command)
            print(f"ADB Command Executed: {adb_command}")
            return True  # Word found and tapped
    return False  # Word not found

def is_continue(adb_device_id):
    # Load the image
    image_path = 'screenshot.png'
    image = Image.open(image_path)

    # Extract text with bounding box information
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

    # Iterate through the data to find the word "CONTINUE"
    for i in range(len(data['text'])):
        if data['text'][i].strip().upper() == "LIVE":
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            print(f"The word 'CONTINUE' is present at location: ({x}, {y}), width: {w}, height: {h}.")

            # Calculate the center of the bounding box
            center_x = x + w // 2
            center_y = y + h // 2
            print(f"Simulating touch at: ({center_x}, {center_y})")

            # Send ADB command to tap at the calculated position
            adb_command = f"adb -s {adb_device_id} shell input tap 1459 846"
            os.system(adb_command)
            print(f"ADB Command Executed: {adb_command}")
            return True  # Word found and tapped

    return False  # Word not found
    


def is_concede(adb_device_id):
    detect_template_and_tap(
        "screenshot.png", 
        "image/LiveMatch/concede.png", 
        adb_device_id
    )

# Call functions
is_OK(adb_device_id)

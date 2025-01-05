# library/capture.py
import os
from PIL import Image
def capture_screenshot(adb_device_id, screenshot_path):
    """
    Example function to capture a screenshot from the device using adb.
    """
    adb_command = f"adb -s {adb_device_id} exec-out screencap -p > {screenshot_path}"
    os.system(adb_command)
    # print(f"Screenshot saved to {screenshot_path}")

def crop_screenshot(input_path, output_path, crop_box):
    """
    Crops a screenshot with a specified location and size.

    Args:
        input_path (str): Path to the input image (screenshot).
        output_path (str): Path to save the cropped image.
        crop_box (tuple): A tuple (left, top, right, bottom) specifying the crop area.

    Returns:
        str: Path to the cropped image.
    """
    try:
        # Open the input image
        image = Image.open(input_path)
        
        # Crop the image
        cropped_image = image.crop(crop_box)
        
        # Save the cropped image
        cropped_image.save(output_path)
        # print(f"Cropped image saved to {output_path}")
        return output_path
    except Exception as e:
        print(f"Error cropping image: {e}")
        return None
# crop_screenshot("screenshot.png", "cropped_screenshot.png", (100, 200, 500, 600))
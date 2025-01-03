from PIL import Image
import pytesseract
import os

def is_continue(adb_device_id):
    # Load the image
    image_path = 'image.png'
    image = Image.open(image_path)

    # Extract text with bounding box information
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

    # Iterate through the data to find the word "CONTINUE"
    for i in range(len(data['text'])):
        if data['text'][i].strip().upper() in ["SEASON"]:
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            print(f"The word 'CONTINUE' is present at location: ({x}, {y}), width: {w}, height: {h}.")

            # Calculate the center of the bounding box
            center_x = x + w // 2
            center_y = y + h // 2
            print(f"Simulating touch at: ({center_x}, {center_y})")

            # Send ADB command to tap at the calculated position
            adb_command = f"adb -s {adb_device_id} shell input tap {center_x} {center_y}"
            os.system(adb_command)
            print(f"ADB Command Executed: {adb_command}")
            return True  # Word found and tapped

    print("The word 'CONTINUE' is NOT present in the image.")
    print(data)
    return False  # Word not found
is_continue("emulator-5554")

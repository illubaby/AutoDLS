import os
def capture_screenshot(adb_device_id, output_path="screenshot.png"):
    """
    Captures a screenshot from the specified ADB device.

    Args:
        adb_device_id (str): The ADB device ID (use `adb devices` to get this).
        output_path (str): Path to save the screenshot (default is "screenshot.png").
    """
    capture_command = f"adb -s {adb_device_id} exec-out screencap -p > {output_path}"
    os.system(capture_command)
    print(f"Screenshot captured and saved to {output_path}")
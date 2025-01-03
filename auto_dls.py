from library import *
from check_present import *
import cv2
import numpy as np
import time
from global_variables import *
# Main Program
def main():
    adb_device_id = "emulator-5554"  # Replace with your ADB device ID
    screenshot_path = "screenshot.png"

    while True:
        capture_screenshot(adb_device_id, screenshot_path)

        print("\nChecking for LiveEvents...")
        is_LiveEvents(adb_device_id)

        print("\nChecking for Continue...")
        is_continue(adb_device_id)

        print("\nChecking for Advertisement...")
        is_advertisement(adb_device_id)
        print("\nChecking for Limited Time Offer...")
        is_limited_time_offer(adb_device_id)
        print("\nChecking for Deam Point Boost...")
        is_dream_point_boost(adb_device_id)
        print("\nChecking for Opponent Forfeit...")
        is_opponent_forfeit(adb_device_id)
        print("\nChecking for OK...")
        is_OK(adb_device_id)
        print("\nChecking for Promotion...")
        is_promotion(adb_device_id)
        print("\nChecking for Champion...")
        is_champion(adb_device_id)
        print("\nChecking for Season...")
        is_season(adb_device_id)
        # Wait for 1 second before repeating
        time.sleep(2)

if __name__ == "__main__":
    main()
from PIL import Image
import matplotlib.pyplot as plt
from library.capture import capture_screenshot
from global_variables import *
capture_screenshot(adb_device_id, screenshot_path)
def click_and_log_on_image(image_path):
    # Load the image
    image = Image.open(image_path)

    # Function to capture mouse clicks
    def on_click(event):
        if event.xdata and event.ydata:
            print(f"Clicked at: ({int(event.xdata)}, {int(event.ydata)})")

    # Display the image
    fig, ax = plt.subplots()
    ax.imshow(image)
    fig.canvas.mpl_connect('button_press_event', on_click)
    plt.axis("off")
    plt.show()

# Path to your screenshot
image_path = "End1.png"  # Replace with the path to your screenshot
click_and_log_on_image(image_path)

from PIL import Image
import matplotlib.pyplot as plt

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
image_path = "screenshot.png"  # Replace with the path to your screenshot
click_and_log_on_image(image_path)

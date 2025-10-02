import os
import random
import ctypes

# Folder path containing images (relative to script location)
image_folder = os.path.join(os.path.dirname(__file__), 'Archive')

# Check if folder exists
if not os.path.exists(image_folder):
    print(f"Error: Folder '{image_folder}' does not exist!")
    exit(1)

# Get list of image files in folder
images = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

# Check if any images were found
if not images:
    print(f"Error: No image files found in '{image_folder}'")
    exit(1)

# Choose a random image
selected_image = random.choice(images)

# Full path to selected image
image_path = os.path.join(image_folder, selected_image)

# Set wallpaper (Windows)
SPI_SETDESKWALLPAPER = 20
result = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

if result:
    print(f"Wallpaper successfully set to: {selected_image}")
else:
    print(f"Error: Failed to set wallpaper to {selected_image}")

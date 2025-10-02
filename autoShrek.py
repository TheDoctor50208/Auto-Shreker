import os
import random
import ctypes

# Folder path containing images
image_folder = r'C:\Path\To\Your\ImageFolder'

# Get list of image files in folder
images = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]

# Choose a random image
selected_image = random.choice(images)

# Full path to selected image
image_path = os.path.join(image_folder, selected_image)

# Set wallpaper (Windows)
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

print(f"Wallpaper set to {selected_image}")

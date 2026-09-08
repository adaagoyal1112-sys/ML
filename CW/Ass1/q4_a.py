import numpy as np
from PIL import Image

def img_to_array(path):

    img = Image.open(path)

    if img.mode == "RGB":
        arr = np.array(img)
        arr_2d = arr.reshape(arr.shape[0], -1)

        np.savetxt("image_rgb.txt", arr_2d, fmt="%d")

        print("RGB image saved")

    else:
        arr = np.array(img.convert("L"))

        np.savetxt("image_gray.txt", arr, fmt="%d")

        print("Grayscale image saved")


# 👇 PASTE YOUR IMAGE PATH HERE
img_to_array(r"C:\Users\ADAA GOYAL\OneDrive\Pictures\Cute Wallpaper.jpeg")
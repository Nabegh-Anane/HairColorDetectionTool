import cv2
import numpy as np
import os
import json
from PIL import Image

def get_limits(color):
    c = np.uint8([[color]])  # BGR values
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]  # Get the hue value

    if hue >= 165:  # Upper limit for divided red hue
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)
    elif hue <= 15:  # Lower limit for divided red hue
        lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    else:
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit

def detect_hair_color(image_path, color_name, color_bgr):
    image = cv2.imread(image_path)
    hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=color_bgr)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    hair_detected = bbox is not None

    result = {
        "name": os.path.basename(image_path),
        "hair": hair_detected,
        "color": color_name
    }

    if color_name == "yellow" and hair_detected:
        result["accept"] = True

    return result

def process_images(folder_path):
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    results = []

    colors = {
        "black": [0, 0, 0],
        "white": [255, 255, 255],
        "red": [0, 0, 255],
        "green": [0, 255, 0],
        "blue": [255, 0, 0],
        "yellow": [0, 255, 255],
        "cyan": [255, 255, 0],
        "magenta": [255, 0, 255],
        "silver": [192, 192, 192],
        "gray": [128, 128, 128],
        "maroon": [0, 0, 128],
        "olive": [0, 128, 128],
        "purple": [128, 0, 128],
        "teal": [128, 128, 0],
        "navy": [128, 0, 0],
        "orange": [0, 165, 255],
        "pink": [203, 192, 255],
        "lime": [0, 255, 128],
        "brown": [42, 42, 165],
        "gold": [0, 215, 255],
        "beige": [220, 245, 245],
        "tan": [140, 180, 210],
        "chocolate": [30, 105, 210],
        "coral": [80, 127, 255]
    }

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        for color_name, color_bgr in colors.items():
            result = detect_hair_color(image_path, color_name, color_bgr)
            results.append(result)

    return results

def main():
    folder_path = './images'  # Update this path to your images folder
    results = process_images(folder_path)

    with open('hair_color_detection_results.json', 'w') as json_file:
        json.dump(results, json_file, indent=2)

    print("Hair color detection completed. Results saved to 'hair_color_detection_results.json'.")

if __name__ == "__main__":
    main()

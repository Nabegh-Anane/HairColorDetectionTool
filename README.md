# Hair Color Detection Tool

## Description

The **Hair Color Detection Tool** is a Python application that analyzes images to detect hair color from a predefined range of colors. The program leverages the OpenCV library for image processing and HSV (Hue, Saturation, Value) for accurate color identification. It generates a JSON file containing detection results for each image.

### Key Features:
1. **Color Detection**: Identifies hair colors based on BGR/HSV values.
2. **JSON Output**: Produces a JSON file containing information about images, detected colors, and conditional acceptance for certain colors (e.g., "yellow").
3. **Batch Processing**: Can analyze multiple images in a folder.

---

## Advantages

- **Reliable and Fast**: Utilizes OpenCV for efficient image processing.
- **Extensible**: Easily add new colors or modify detection parameters.
- **Comprehensive Documentation**: Generates a well-structured JSON file for easy integration into other systems.
- **Supports Multiple Formats**: Compatible with various standard image formats.

---

## Requirements

Before running this project, ensure your environment meets the following prerequisites:
- Python 3.x installed
- The following Python libraries installed:
  - OpenCV (`cv2`)
  - NumPy (`numpy`)
  - PIL (Pillow)
- A folder containing images to be analyzed (default: `./images`)

---

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone <URL_of_your_repository>
   cd <repository_name>
   ```

2. Install the required dependencies using pip:
   ```bash
   pip install opencv-python numpy pillow
   ```

3. Add your images to a folder named `images` at the project root, or update the path in the `main()` function.

---

## Usage

1. Place your images in the `./images` folder or update the path in the `main` function.
2. Run the main script:
   ```bash
   python script_name.py
   ```
3. The results will be saved in a file named `hair_color_detection_results.json` in the project directory.

### Example JSON Output:
```json
[
  {
    "name": "image1.jpg",
    "hair": true,
    "color": "yellow",
    "accept": true
  },
  {
    "name": "image2.jpg",
    "hair": false,
    "color": "red"
  }
]
```

---

## Future Improvements

1. **Graphical Interface**: Add a user interface to upload images and view results.
2. **Performance Optimization**: Enable parallel processing for large image directories.
3. **Video Format Support**: Extend detection to video files by analyzing frame by frame.
4. **Precision Enhancements**: Allow dynamic adjustments of HSV thresholds for varied lighting conditions.
5. **Multi-Criteria Detection**: Add the ability to detect multiple colors in a single image.

---

## Author

**Nabegh Anane**  
Feel free to contribute by submitting suggestions via issues or pull requests. 😊


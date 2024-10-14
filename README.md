# Color Detection

This project is a Python application for detecting colors in video capture using OpenCV, numpy and Pillow. The tool allows you to specify colors in BGR format and detect them in an image, converting them into HSV format for processing. 

## Features
- Detect colors in a video capture using OpenCV.
- Convert BGR colors to HSV for improved color matching.

## Installation

### Prerequisites
- Python 3.x
- [OpenCV](https://opencv.org/) (cv2)
- [Pillow](https://python-pillow.org/)
- [Numpy](https://numpy.org/)

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/Azur4ok/color_detection.git
   cd color_detection
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
3. Install dependencies:
    ```bash
    pip install -r requirements.txt

## Usage
1. Add the color you want to detect in the script by specifying the BGR values
2. Run the main.py file
   ```bash
   python main.py
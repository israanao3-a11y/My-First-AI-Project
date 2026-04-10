import cv2
import numpy as np

def analyze_plant_health(image_path):
    # 1. Load the plant image
    image = cv2.imread(image_path)
    
    if image is None:
        print("Error: Could not find the image file.")
        return

    # 2. Convert to Grayscale (simplifying the data)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 3. Detect spots or holes (thresholding)
    _, threshold = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)

    print("--- Plant Leaf Analysis Complete ---")
    # This shows the AI can now 'see' the patterns
    cv2.imshow('Original Leaf', image)
    cv2.imshow('AI Perspective (Spots)', threshold)
    cv2.waitKey(0)

if __name__ == "__main__":
    print("Starting OpenCV Plant Detection...")
    # Make sure you have an image named 'leaf.jpg' in the same folder
    analyze_plant_health('leaf.jpg')
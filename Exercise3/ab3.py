#!/usr/bin/env python3

import sys
import cv2
import numpy as np

def custom_erosion(img, kernel_size):
    """
    Morphological erosion in grayscale
    """
    h, w = img.shape  
    pad = kernel_size // 2 
    out = np.zeros_like(img) 

    # Iterate through every pixel in the image
    for y in range(h):
        for x in range(w):
            # Define the neighborhood bounds considering the image limits
            y_start = max(0, y - pad)
            y_end = min(h, y + pad + 1)
            x_start = max(0, x - pad)
            x_end = min(w, x + pad + 1)

            # Extract the valid neighborhood region
            roi = img[y_start:y_end, x_start:x_end]

            # Assign the minimum value in the valid region
            out[y, x] = np.min(roi)

    return out


import cv2
import numpy as np

def custom_dilation(img, kernel_size):
    """
    Morphological dilation in grayscale.
    """
    h, w = img.shape 
    pad = kernel_size // 2 
    out = np.zeros_like(img)

    # Iterate through every pixel in the image
    for y in range(h):
        for x in range(w):
            # Define the valid neighborhood bounds (handling borders)
            y_start = max(0, y - pad)  
            y_end = min(h, y + pad + 1)  
            x_start = max(0, x - pad) 
            x_end = min(w, x + pad + 1)

            # Extract the valid neighborhood region
            roi = img[y_start:y_end, x_start:x_end]

            # Assign the maximum value in the valid region
            out[y, x] = np.max(roi)

    return out

def main():
    if len(sys.argv) < 4:
        print("Usage: 3 <kernel_size> <input_image> <output_image> <operation> (erosion/dilation)")
        sys.exit(1)

    i = int(sys.argv[1])
    input_image_path = sys.argv[2]
    output_image_path = sys.argv[3]
    operation = sys.argv[4]

    # Load the image in grayscale
    img = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: could not read image {input_image_path}")
        sys.exit(1)

    # Define the kernel size
    kernel_size = 2 * i + 1

    if operation == "erosion":  
        # Perform morphological opening
        erosion = custom_erosion(img, kernel_size)

        # Save the resulting image
        cv2.imwrite(output_image_path, erosion)
        print(f"Opening done with a {kernel_size}x{kernel_size} kernel.")
        print(f"Output image saved to: {output_image_path}")
    elif operation == "dilation":
        # Perform morphological closing
        dilation = custom_dilation(img, kernel_size)

        # Save the resulting image
        cv2.imwrite(output_image_path, dilation)
        print(f"Closing done with a {kernel_size}x{kernel_size} kernel.")
        print(f"Output image saved to: {output_image_path}")
    else:
        print("Invalid operation. Please choose 'erosion' or 'dilation'.")
        sys.exit(1)

if __name__ == "__main__":
    main()


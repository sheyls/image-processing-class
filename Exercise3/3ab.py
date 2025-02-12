#!/usr/bin/env python3

import sys
import cv2
import numpy as np

def custom_erosion(img, kernel_size):
    """
    Morphological erosion in grayscale.
    For each pixel, we take the minimum value within the local neighborhood
    defined by kernel_size x kernel_size.
    """
    # 'pad' is half the kernel size (integer division).
    pad = kernel_size // 2

    # BORDER_REPLICATE copies the outermost pixels so we can safely get neighborhoods near edges.
    img_padded = cv2.copyMakeBorder(img, pad, pad, pad, pad, cv2.BORDER_REPLICATE)

    # Output image of the same size as the original.
    out = np.zeros_like(img)

    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            # Extract the region of interest from the padded image.
            # This region is kernel_size x kernel_size around (x, y).
            roi = img_padded[y : y + kernel_size, x : x + kernel_size]
            # Erosion in grayscale: take the minimum value in the neighborhood.
            out[y, x] = np.min(roi)

    return out

def custom_dilation(img, kernel_size):
    """
    Morphological dilation in grayscale.
    For each pixel, we take the maximum value within the local neighborhood
    defined by kernel_size x kernel_size.
    """
    pad = kernel_size // 2
    img_padded = cv2.copyMakeBorder(img, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    out = np.zeros_like(img)

    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            roi = img_padded[y : y + kernel_size, x : x + kernel_size]
            # Dilation in grayscale: take the maximum value in the neighborhood.
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


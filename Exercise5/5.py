#!/usr/bin/env python3

import sys
import cv2
import numpy as np
from Exercise4.ab4 import custom_opening, custom_closing
from Exercise2.b2.b2 import compare_images


def main():
    if len(sys.argv) < 4:
        print("Usage: python ab5.py <i> <input_image> <operation> (opening/closing) <output_text_name>?")
        sys.exit(1)

    i = int(sys.argv[1])
    input_image_path = sys.argv[2]
    operation = sys.argv[3]
    output_text_path = sys.argv[4]

    img = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: could not load image {input_image_path}")
        sys.exit(1)

    kernel_size = 2 * i + 1

    # Apply opening once
    opened_once = custom_opening(img, kernel_size)

    # Apply opening again on the result
    opened_twice = custom_opening(opened_once, kernel_size)

    # Save intermediate results
    cv2.imwrite("output/exercise_4a_output_01.pgm", opened_once)
    cv2.imwrite("output/exercise_4a_output_02.pgm", opened_twice)

    # Compare both results and write the result in a text file
    identical = compare_images("output/exercise_04a_output_01.pgm", "output/exercise_04a_output_02.pgm", output_text_path)

    with open(output_text_path, "w") as f:
        f.write(f"Opening is idempotent: {identical}\n")

    print(f"Comparison result saved in {output_text_path}")

    print("Opening is idempotent: ", identical)

    return identical

if __name__ == "__main__":
    main()

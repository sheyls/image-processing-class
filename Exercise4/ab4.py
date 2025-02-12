import sys
import cv2
from Exercise3.ab3 import custom_erosion, custom_dilation

def custom_opening(img, kernel_size):
    return custom_erosion(custom_dilation(img, kernel_size), kernel_size)

def custom_closing(img, kernel_size):
    return custom_dilation(custom_erosion(img, kernel_size), kernel_size)

def main():
    if len(sys.argv) < 4:
        print("Usage: 4 <kernel_size> <input_image> <output_image> <operation> (opening/closing)")
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

    if operation == "opening":  
        # Perform morphological opening
        opening = custom_erosion(img, kernel_size)

        # Save the resulting image
        cv2.imwrite(output_image_path, opening)
        print(f"Opening done with a {kernel_size}x{kernel_size} kernel.")
        print(f"Output image saved to: {output_image_path}")
    elif operation == "closing":
        # Perform morphological closing
        closing = custom_closing(img, kernel_size)

        # Save the resulting image
        cv2.imwrite(output_image_path, closing)
        print(f"Closing done with a {kernel_size}x{kernel_size} kernel.")
        print(f"Output image saved to: {output_image_path}")
    else:
        print("Invalid operation. Please choose 'opening' or 'closing'.")
        sys.exit(1)

if __name__ == "__main__":
    main()


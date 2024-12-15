import cv2

def image_to_sketch(input_image, output_image="sketch.png"):
    image = cv2.imread(input_image)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - gray_image
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    sketch = cv2.divide(gray_image, 255 - blurred_image, scale=256)
    cv2.imwrite(output_image, sketch)
    print(f"Sketch saved as {output_image}")

# Example usage
image_to_sketch("your_image.jpg")  # Replace with your image file

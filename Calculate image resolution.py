from PIL import Image

# Load the image
image_path = "path_to_your_image.jpg"  # Replace with your image path
image = Image.open("C:\\Users\\ankit\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-10-31 234334.png")

# Get image resolution
width, height = image.size
print(f"Resolution: {width}x{height}")

# Show the image
image.show()

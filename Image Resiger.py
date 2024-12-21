from PIL import Image

def resize_image():
    print("Welcome to the Image Resizer!")
    try:
        input_path = input("Enter the path to the image you want to resize (e.g., 'image.jpg'): ")
        output_path = input("Enter the path to save the resized image (e.g., 'resized_image.jpg'): ")
        width = int(input("Enter the new width: "))
        height = int(input("Enter the new height: "))
        
        with Image.open(input_path) as img:
            resized_img = img.resize((width, height))
            resized_img.save(output_path)
            print(f"Image resized and saved as {output_path}")
    except FileNotFoundError:
        print("Error: File not found. Please check the file path and try again.")
    except ValueError:
        print("Error: Invalid input for width or height. Please enter numbers only.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the image resizer
resize_image()

class InvalidFileExtensionError(Exception):
    """Custom exception for invalid file extensions."""
    def __init__(self, message="File must have a .txt extension"):
        self.message = message
        super().__init__(self.message)

def open_text_file(file_name):
    """Open a file only if it has a .txt extension."""
    if not file_name.endswith(".txt"):
        raise InvalidFileExtensionError(f"Invalid file extension: {file_name}. Only .txt files are allowed.")
    try:
        with open(file_name, "r") as file:
            print(file.read())
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_name}' does not exist.")

# Example usage
try:
    open_text_file("document.pdf")  # Invalid extension
except InvalidFileExtensionError as e:
    print(f"Custom exception caught: {e}")
except FileNotFoundError as e:
    print(f"File error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

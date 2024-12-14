import qrcode

def generate_qr_code(data, file_name="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(file_name)
    print(f"QR Code saved as {file_name}")

# Example usage
text = "https://www.python.org"
generate_qr_code(text)

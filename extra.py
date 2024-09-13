import qrcode

# Define the data that you want to encode in the QR code
data = "https://www.example.com"

# Create a QRCode object with desired settings
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Error correction level
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Thickness of the border (minimum is 4)
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the generated QR code as an image file
img.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png'.")

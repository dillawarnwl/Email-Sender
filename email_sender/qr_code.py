import qrcode

# Contact information
contact_info = {
    "first_name": "Ali",
    "last_name": "Dillawar",
    "phone_number": "03156765056",
}

# Format vCard
vcard_data = f"BEGIN:VCARD\nVERSION:3.0\nN:{contact_info['last_name']};{contact_info['first_name']}\nTEL:{contact_info['phone_number']}\nEND:VCARD"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(vcard_data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image or display it as needed
img.save("contact_qr.png")

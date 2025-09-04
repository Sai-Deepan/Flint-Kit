# Sai

import pyqrcode
from PIL import Image

link = input("Enter the link to generate QR code: ")
qr_code = pyqrcode.create(link)
qr_code.png("QR_Code.png", scale=6)
img = Image.open("QR_Code.png")
img.show()
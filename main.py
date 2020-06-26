import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

# generate QR code

qr = pyqrcode.create("Coding With Evan")
qr.png("myCode.png", scale=8)

# read QR code

d = decode(Image.open("myCode.png"))
print(d[0].data.decode("ascii"))



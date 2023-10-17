import pyqrcode

text = input("Enter the text to generate a QR code: ")

qr_code = pyqrcode.create(text)

qr_code.svg('qr_code.svg', scale = 8)
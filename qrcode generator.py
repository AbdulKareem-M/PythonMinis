import pyqrcode

print("welcome")

secret_msg = input("enter the secret message")

code = pyqrcode.create(secret_msg)

code.png("QRCODE.png", scale=5)

print("QRcode generated successfully")
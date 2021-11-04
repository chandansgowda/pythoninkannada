import qrcode

print("QR Code Generator")
print("Created by @chandan")

data = input("Enter input>> ")

qr = qrcode.make(data)

qr.save("C:/Users/chand/Desktop/qrcode.png")

print("QR Code generation successful")


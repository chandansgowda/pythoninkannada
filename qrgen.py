import qrcode

print("QR Code Generator")
print("Created by @-Mohan")

data = input("Enter input>> ")
qr = qrcode.make(data)
qr.save("qrcode.png")

print("QR Code generated")


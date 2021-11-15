import qrcode

data = input("Enter the information to store in the generated QR Code: ")
print("Your entered info stored Successfully!")

qr = qrcode.make(data)

file_location = input("Enter the QR Code location to be stored: ")
qr.save(file_location)

print("Great..! Your QR code is generated Successfully and Safely")

import qrcode

data = "https://algol.homelinux.no/"
img = qrcode.make(data)
print(type(img))
img.save("qr.png")

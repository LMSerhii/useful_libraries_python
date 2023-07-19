import qrcode


def get_qrcode(url='https://www.google.com.ua', name='default'):
    qr = qrcode.make(data=url)
    qr.save(stream=f"{name}.png")

    return f"QR code was created "


def get_info():
    qr = qrcode.QRCode()
    data = "Serhii Leonov"
    qr.add_data(data)

    im = qr.make_image()
    im.show()


def main():
    # get_qrcode(url="https://github.com/LMSerhii", name="GitHub")
    # get_qrcode(url="https://www.linkedin.com/in/leonovserhii/", name="Linkedin")
    get_info()


if __name__ == '__main__':
    main()




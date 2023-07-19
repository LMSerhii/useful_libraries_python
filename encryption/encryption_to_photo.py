from stegano import lsb
from stegano import exifHeader
from steganocryptopy.steganography import Steganography


def lsb_method_encoding():
    """ encrypt to image with lsb """
    secret = lsb.hide("img/1.png", "secret text")
    secret.save("img/1_secret.png")


def lsb_method_decoding():
    """ decrypt to image with lsb """
    result = lsb.reveal("img/1_secret.png")
    print(result)


def exifheader_method_encoding():
    """ encrypt to image with exifHeader"""
    secret = exifHeader.hide("img/2.jpg", "img/2_secret.jpg", "Твой секретный код")


def exifheader_method_decoding():
    """ decrypt to image with exifHeader"""
    result = exifHeader.reveal("img/2_secret.jpg").decode()
    print(result)


def steganography_method_encoding():
    """ encrypt to image with steganography"""
    Steganography.generate_key('')
    secret = Steganography.encrypt("key.key", "img/3.png", "secret_message.txt")
    secret.save("img/3_secret.png")


def steganography_method_decoding():
    """ encrypt to image with steganography"""
    result = Steganography.decrypt(key="key.key", img="img/3_secret.png")
    print(result)


def main():
    # lsb_method_encoding()
    # lsb_method_decoding()
    # exifheader_method_encoding()
    # exifheader_method_decoding()
    # steganography_method_encoding()
    steganography_method_decoding()


if __name__ == '__main__':
    main()
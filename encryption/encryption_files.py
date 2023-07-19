import pyAesCrypt
import os


def encryption(file, password):
    """ encryption function"""

    buffer_size = 512 * 1024

    pyAesCrypt.encryptFile(
        f"{file}",
        f"{file}.crp",
        password,
        buffer_size,
    )

    print(f"File {os.path.splitext(file)[0]} is encrypted")

    os.remove(file)


def decryption(file, password):
    """ decryption function"""

    buffer_size = 512 * 1024

    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size,
    )

    print(f"File {os.path.splitext(file)[0]} is decrypted")

    os.remove(file)


def walking_by_dirs(dir, password, choice):

    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        if os.path.isfile(path) and choice == '0':
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        elif os.path.isfile(path) and choice == '1':
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(path, password, choice)


def main():
    choice = input("If you want encrypt files enter '0' or '1' for decryption: ")
    directory_path = input("Enter your directory path: ")
    password = input("Enter your password: ")
    walking_by_dirs(directory_path, password, choice)


if __name__ == '__main__':
    main()


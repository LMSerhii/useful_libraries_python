from PyPDF2 import PdfFileWriter, PdfFileReader


def encryption():
    """ this function encrypts the pdf file """

    while True:

        greetings = input("want to continue encrypting enter 'yes' or 'no' if you want to exit ")
        if greetings == 'no':
            break
        else:
            incoming_file = input("[+] Enter incoming file: ")
            password = input("[+] Enter password: ")
            output_file = input("[+] Enter output file: ")

            pdf_writer = PdfFileWriter()
            try:
                pdf_reader = PdfFileReader(incoming_file)
            except FileNotFoundError:
                print(f"[INFO] No file with path: {incoming_file}")
                continue
            for page in range(pdf_reader.numPages):
                file_reader = pdf_reader.getPage(page)
                pdf_writer.addPage(file_reader)

            pdf_writer.encrypt(password)

            with open(output_file, "wb") as file:
                pdf_writer.write(file)

        print(f"Created - {output_file}")
        break


def decryption():
    """ this function decrypts pdf file """

    while True:

        greetings = input("want to continue decrypting enter 'yes' or 'no' if you want to exit ")
        if greetings == 'no':
            break
        else:
            incoming_file = input("[+] Enter incoming file: ")
            password = input("[+] Enter password: ")
            output_file = input("[+] Enter output file: ")

            pdf_writer = PdfFileWriter()
            try:
                pdf_reader = PdfFileReader(incoming_file)
            except FileNotFoundError:
                print(f"[INFO] No file with path: {incoming_file}")
                continue

            if pdf_reader.isEncrypted:
                pdf_reader.decrypt(password)

            for page in range(pdf_reader.numPages):
                file_reader = pdf_reader.getPage(page)
                pdf_writer.addPage(file_reader)

            with open(output_file, "wb") as file:
                pdf_writer.write(file)

        print(f"File - {output_file} decrypted ")
        break


def main():
    choose = input("""
        Hello! 
        this program will encrypt your file if you want to encrypt the file enter: '0'
        and if you want to the decrypt enter: '1'
        """)
    encryption() if choose == "0" else decryption()


if __name__ == '__main__':
    main()
import img2pdf
import requests
from art import tprint

headers = {
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}


def get_data():
    tprint("DOWNLOAD\n   IMAGE", "twisted")
    list_pdf = []
    for i in range(1, 165):
        url = f"https://presto-ps.ua/magazine/files/mobile/{i}.jpg"
        req = requests.get(url=url, headers=headers)
        response = req.content

        with open(f"media_presto/{i}.jpg", "wb") as file:
            file.write(response)
            print(f"Downloaded {i} of 164")

        list_pdf.append(f'media_presto/{i}.jpg')

    print("#" * 20)
    print(list_pdf)
    print("#" * 20)

    tprint("CREATE\n  PDF", "twisted")
    with open("presto.pdf", "wb") as file:
        file.write(img2pdf.convert(list_pdf))

    tprint("PDF \n  file   created \n  successfully!!!")


def main():
    get_data()
    # write_to_pdf()


if __name__ == "__main__":
    main()
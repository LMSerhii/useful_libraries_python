import csv
import re
from pathlib import Path

import pandas as pd
import tabula as tb
import pdfplumber


def get_data_in_pdf(file_path):
    """  """
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        rep = [' ', ',']
        name = file_path.split('/')[-1].split(".")[0]
        for i in rep:
            if i in name:
                name = name.replace(i, '_')
        with pdfplumber.PDF(open(file=file_path, mode="rb")) as pdf:
            pages = [page.extract_table() for page in pdf.pages]
        for page in pages:
            for row in page:
                with open(f"data/csv_files/{name}.csv", "a") as file:
                    writer = csv.writer(file)
                    writer.writerow(row)
    else:
        return "File not exists, check the file path!"


def get_data_in_excel(file_path):
    """  """


def get_data_in_csv(file_path):
    """  """
    with open(file=file_path, mode="r") as file:
        rows = csv.reader(file)
        for row in rows:
            category = row[0]
            vendor_code = row[1]
            item_code = row[2]
            item_name = row[3]
            item_price = row[5]
            if category != '':
                category = category.split('.')
                if len(category) > 1:
                    category = category[1].strip()
                else:
                    category = category[0].strip()
                print(category)
            #     print('#' * 50)
            # else:
            #     print(f"{vendor_code} - {item_code} - {item_name} - {item_price}")
            # print(category)



def main():
    # get_data_in_pdf(file_path="data/pdf_files/Прайс_инструмент,_электро_инструмент,_химия_2.pdf")
    # get_data_in_excel()
    get_data_in_csv(file_path="data/csv_files/Прайс_инструмент__электро_инструмент__химия_2.csv")


if __name__ == "__main__":
    main()



import csv
import os

from pdf2image import convert_from_path
from PIL import Image
from pylibdmtx.pylibdmtx import decode


def decode_write_csv(decode_list):
    with open('examples.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(decode_list)
    print("Successfully")

def read_qr_code(filename):
    result = decode(Image.open(filename))
    return str(result[0].data)

def add_decode(path):
    pages = convert_from_path(path)
    decode_list = ["decodes"]
    for i in range(len(pages)):
        print(f"Page {i+1} is processing...")
        a=f"img/page{i+1}.png"
        pages[i].save(a, 'PNG')
        data=str(read_qr_code(a))
        decode_list.append(data[2:-1])
        os.remove(a)

    return decode_write_csv(decode_list)

if __name__ == '__main__':
    add_decode("39.pdf")
    print("Success!")



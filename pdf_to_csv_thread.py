############################################################################################################ Using Multiple Threads to Speed Up Python Programs ############################################################################################################

import csv
import logging
import os
import threading
import time

# 3rd party
import pandas
from pdf2image import convert_from_path
from PIL import Image
from pylibdmtx.pylibdmtx import decode

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('thread.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

from functools import wraps


def timer(func):
    """timer decorator"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        finish = time.perf_counter()
        logger.info(f"Finished in {round(finish-start, 2)} second(s)")
        return result
    return wrapper

def my_logger(func):
    """logger decorator"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"{func.__name__} ran with args: {args}, and kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper


@my_logger
def deccode_write_csv_pandas(decode_list: list) -> bool:
    """write decode to csv file using pandas"""
    try:
        df = pandas.DataFrame(decode_list, columns=['decodes'])
        df.to_csv('examples.csv', index=False, sep=',')
        return True
    except Exception as e:
        logger.error(e)
        return False

@my_logger
def decode_write_csv(decode_list: list) -> bool:
    """write decode to csv file

    Args:
        decode_list (list): list of decode data

    Returns:
        bool: True or False
    """
    try:
        with open('examples.csv', mode='w', newline='') as file:
            fieldnames = ['decodes']
            writer = csv.writer(file, lineterminator='\n', delimiter='\n')
            writer.writerow(fieldnames)
            # for i in decode_list:
            #     writer.writerow([i]+ '\n')
            writer.writerow(decode_list)
        return True
    except Exception as e:
        logger.error(e)
        return False

@my_logger
def read_qr_code(filename: str) -> str or bool:
    """read qr code from image file and return decode data"""
    try:
        result = decode(Image.open(filename))
        return str(result[0].data)
    except Exception as e:
        logger.error(e)
        return False

@my_logger
def decode_writer(mode: str, decode_list: list) -> bool:
    """decode writer

    Args:
        mode (str): mode to write decode
        decode_list (list): list of decode data

    Returns:
        bool: True or False
    """
    try:
        if mode in {'1', 'cvs'}:
            return decode_write_csv(decode_list)
        elif mode in {'2', 'pandas'}:
            return deccode_write_csv_pandas(decode_list)
        else:
            logger.error("Mode not found")
            return False
    except Exception as e:
        logger.error(e)
        return False

@my_logger
def add_decode(path: str, mode: str = 'cvs') -> bool or str:
    """add decode to list

    Args:
        path (str): path to pdf file
        mode (str, optional): pandas or cvs. Defaults to 'cvs'.

    Returns:
        bool or str: True or False or decode_list
    """
    try:
        pages = convert_from_path(path)
        decode_list: list = []
        for page in range(len(pages)):
            print(f"Page {page+1} is processing...", end='\r')
            page_path: str = f"img/page{page+1}.png"
            pages[page].save(page_path, 'PNG')
            data = str(read_qr_code(page_path))
            decode_list.append(data[2:-1])
            os.remove(page_path)
        return decode_writer(mode=mode, decode_list=decode_list)
    except Exception as e:
        logger.error(e)
        return False



@timer
@my_logger
def main(mode):
    """Tread run code"""
    try:
        t1 = threading.Thread(target=add_decode, args=["39.pdf", mode])
        t1.start()
        t1.join()
        return bool(t1.is_alive())
    except Exception as e:
        logger.exception(e)
        return False


if __name__ == '__main__':
    print("+=======================================+")
    mode_input = input("Enter mode number: \n1. cvs\n2. pandas\n")
    main(mode=mode_input)
    print("+=======================================+")


# Task 

# last video we use @decorator
# use @decorator to make a timer function
# use @decorator to make a logger function


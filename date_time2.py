"""Превратите строку "01/01/25 12:10:03.234567" в объект datetime"""
from datetime import datetime

def main():
    d_string="01/01/25 12:10:03.234567"

    get_date=datetime.strptime(d_string,"%y/%m/%d %H:%M:%S.%f")
    return d_string

if __name__ == '__main__':
    print(main())

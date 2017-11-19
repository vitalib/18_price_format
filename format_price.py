import argparse
import sys


def format_price(price):
    '''Format price into pretty view'''
    try:
        price = "{:,.2f}".format(float(price)).replace(',', ' ')
        if price[-2:] == '00':
            price = price[:-3]
    except:
        pass
    return price


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('price', help='price of goods')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_arguments()
    print(format_price(args.price))

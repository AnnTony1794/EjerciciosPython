from collections import OrderedDict


def magia():
    n = int(input())
    ordered_dict = OrderedDict()

    for i in range(0, n):
        item_name = input()
        price = input()
        ordered_dict[item_name] = price

if __name__ == '__main__':
    n = int(input())
    magia()
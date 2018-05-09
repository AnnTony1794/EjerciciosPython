# -*- conding: utf-8 -*-

def espiral(dimention):
    values = (lambda x: x * x)(dimention)

    matrix = [[0 for x in range(dimention)] for y in range(dimention)]

    for i in range(0, dimention):
        print(matrix[i])


def run():
    print('Generar matriz espiral')
    dimention = int(input('Dimensión de la espiral\n\n'))

    print(espiral(dimention))


if __name__ == '__main__':
    run()

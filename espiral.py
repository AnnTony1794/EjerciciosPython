# -*- conding: utf-8 -*-

def espiral(dimention):
    values = (lambda x: x * x)(dimention)
    counter = (lambda val: int((val / 2) + 1) if val % 2 != 0 else int(val / 2))(dimention)
    matrix = [[0 for x in range(dimention)] for y in range(dimention)]
    total_dimention = dimention
    n = 0

    print(counter)

    for i in range(0, counter):

        for x in range(n, dimention):
            matrix[i][x] = values
            values -= 1

        n += 1

        for y in range(n, dimention):
            matrix[y][dimention-1] = values
            values -= 1

        for x in range(n, dimention):
            matrix[dimention-1][total_dimention - (x + 1)] = values
            values -= 1

        n += 1

        for x in range(n, dimention):
            matrix[total_dimention - x][i] = values
            values -= 1

        dimention -= 1
        n -= 1

    for i in range(0, total_dimention):
        print(matrix[i])


def run():
    print('Generar matriz espiral')
    dimention = int(input('Dimensión de la espiral\n\n'))

    espiral(dimention)


if __name__ == '__main__':
    run()

# -*- conding: utf-8 -*-

def espiral(dimention):
    values = (lambda x : x*x)(dimention)

    matrix = [[0 for x in range(dimention)]  for y in range(dimention)]
    xp = 0
    n = 0
    m = 0

    for y in range(0, dimention):

        for x in range(xp, dimention):
            matrix[xp][x] = values
            values -= 1
        dimention -= 1
        n += 1

        for x in range(n, dimention + 1):
            matrix[x][dimention] = values
            values -= 1

        for x in range(n, dimention + 1):
            matrix[dimention][dimention - x] = values
            values -= 1
        n += 1
        dimention -= 1
        for x in range(m, dimention):
            matrix[dimention-x][m] = values
            values -= 1

        print(matrix[y])




def run():
    print('Generar matriz espiral')
    dimention = int(input('Dimensión de la espiral\n\n'))

    print(espiral(dimention))

if __name__ == '__main__':
    run()
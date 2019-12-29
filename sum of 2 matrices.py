# Программа, которая складывает две матрицы
# N - количесто строк, M - столбцов


def add(a1: list, b1: list):
    """
    :param a1: строка первой матрицы
    :param b1: строка второй матрицы
    :return: строку матрицы c, в которой содержатся суммы элементов матриц a и b
    """
    for el in range(N):
        for elem in range(M):
            c[el][elem] = int(a[el][elem]) + int(b[el][elem])


N = int(input('Введите количество строк матриц: '))
M = int(input('Введите количество столбцов матриц: '))
a = [[0 for i in range(M)] for x in range(N)]
b = c = a.copy()

for i in range(N):
    a[i] = input(f'Введите {M} элемент(-а/-ов) {i + 1} строки первой матрицы через пробел: ').split(' ')

print('--' * 20)

for i in range(N):
    b[i] = input(f'Введите {M} элемент(-а/-ов) {i + 1} строки второй матрицы через пробел: ').split(' ')

add(a, b)

print('Сумма двух данных матриц равняется:')

for i in range(N):
    for x in c[i]:
        print(x, ' ', end='')
    if i != N-1:
        print(' ')



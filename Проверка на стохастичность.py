# N - строк, M - столбцов


def stochastic(a: list, n, m):
    row = []
    for i in range(n):
        if sum(a[i]) == 1:
            return print('Матрица является стохастической (по рядам)!')
    print('Данная матрица не стохастична по рядам.')
    column = []
    for k in range(m):
        for i in range(n):
            column.append(float(a[i][k]) + float((a[i+1][k] if i+1 < N else 0)))
        if sum(column) == 1:
            return print('Матрица является стохастической (по столбцам)!')
        else:
            column.clear()
    print('Данная матрица не стохастична по столбцам.')


N = int(input('Введите количество строк матрицы, которую хотите проверить на стохастичность: '))
M = int(input('Введите количество столбцов матрицы: '))
matrix = [[] for i in range(N)]

for rows in range(N):
    matrix[rows] = input(f'Введите {M} элементов {N} столбца матрицы через пробел: ').split(' ')

for i in range(N):
    for k in range(M):
        matrix[i][k] = float(matrix[i][k])

stochastic(matrix, N, M)

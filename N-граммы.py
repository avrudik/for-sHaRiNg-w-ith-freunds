# Биграммы - все пары слов, которые входят в текст. На вход идут два аргумента: строка и целое число.
# Вернуть все N-граммы в данном тексте


def make_a_list(some_line, n):
    output_list = []
    for index in range(len(some_line)):
        for words in range(n):
            output_list.append(some_line[index + words]
                               if index + words < len(some_line) else some_line[(index + words) % len(some_line)])
        print(output_list)
        output_list.clear()


line = input('Введите строку со словами через пробел без знаков препинания: ').split(' ')
N = int(input('Введите количество слов, по которому будет проверяться строка: '))

make_a_list(line, N)

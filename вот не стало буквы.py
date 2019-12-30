def remove_letter(a):
    """Убирает из строки букву 'a', если она есть"""
    if a in line:
        line.remove(a)
        if a in line:
            line.remove(a)
        print(f'{"".join(line)} (не стало буквы {a})')


line = list(input('Введите строку: '))

for i in line:
    for num_of_letter in range(int('410', 16), int('44F', 16)):
        letter = chr(num_of_letter)
        remove_letter(letter)

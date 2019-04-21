numbers = []


def append_number(num, num1):
    i = 0
    while i < num1:
        print(f"Добавление числа {i} в список")
        numbers.append(i)
        i += num

        print("Numbers now: ", numbers)


append_number(2, 25)

print(f"Вывод: {numbers}")

numb = []

for i in range(0, 25, 2):
    print(f"Добавление числа {i} с помощью цикла")
    numb.append(i)
    print("Numb now: ", numb)

print("Вывод: ", numb)

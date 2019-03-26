print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

print(f"So you're {age} old, {height} tall and {weight} heavy.")

#Пример изученного из интернета

name = input("Как вас зовут?: ")
age = int(input("Сколько Вам лет?: "))
fruit = input("Какой фрукт вы хотите купить?: ")
orange = 65.79
print(f"Цена апельсина {orange}")
count = int(input("Сколько апельсинов хотите купить?: "))
summa = count * orange
buy = input("Вы хотите купить? ")
if buy == "yes":
    print(f"Вас зовут {name}, вам {age} года и Вы купили {count} штук, за {summa}")
elif buy == "no":
    print(f"Вас зовут {name}, вам {age} года и Вы не купили {count}")
else:
    print(f"Вы ввели неправильное слово")



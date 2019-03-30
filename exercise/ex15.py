from sys import argv

#script, filename = argv
#Открывает файл переданный как аргумент в терминале и присваивается переменной txt
#txt = open(filename)

#print(f"Here's your file {filename}")
#Печатает переменную txt спомощью функции read файла, которая передается в терминале через аргумент
#print(txt.read())

print("Type the filename again:")
# Вводится с коммандной строки либо текст либо файл с который мы уже открыли и присвоили переменной txt
file_again = input("> ")
#В эту переменную мы присваиваем введенный в переменную file_again либо файл либо строку
txt_again = open(file_again)

print(txt_again.read())

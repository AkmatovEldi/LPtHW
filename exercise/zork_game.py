from sys import argv

script, game_name = argv

stroka = "------------------------------------"
print(stroka)
print(f"Добро пожаловать в игру 'Спаситель - 2019!' {game_name}")
loop = 4

while True:
    while loop == 4:
        if loop == 4:
            print(stroka)
            print("""Ты стоишь на улице,
            И видишь 3 происходящих одновременно опасных ситуаций.
            Где могут пострадать живые существа!
            """)
            action = input(f"Готов помочь им? {game_name} ")

        if action.lower() == "да":
            print(stroka)
            print("И так начнем...")
            loop = 5

        elif action.lower() == "нет":
            print(stroka)
            print(f"Приходи если наберешься храбрости! {game_name} ")
            exit()

        else:
            print("Введите 'да' или 'нет'")

    while loop == 5:
        if loop == 5:
            print(stroka)
            print("""1) Cлепой проходит дорогу на красный цвет светофора
            2) Кошка сорвалась и падает с 9-го этажа 
            3) Человек упал в обморок
            """)
            action_save = input(f"Кого ты спасешь? {game_name} ")

        if action_save.lower() == "кошку":
            print(stroka)
            print(""""Это правильный выбор, так как
            Слепой не умрет так как машина остановится
            Человеку, который упал в обморок ты можешь вызвать скорую, но не как не спасти 
            """)
            exit()

        elif action_save.lower() == "слепого":
            print(stroka)
            print("""Ты проиграл, так как
            Машина может остановится при виде слепого
            """)
            loop = 10

        elif action_save.lower() == "человека":
            print(stroka)
            print("""Ты проиграл, так как
            Человеку, который упал в обморок ты можешь вызвать скорую, но не как не спасти
            """)
            loop = 10

        elif action_save.lower() == "никого":
            print(stroka)
            print(f"Ты бездушный! {game_name}")
            loop = 10
        else:
            print("Выбери кого спасти 'кошку', 'слепого' или 'человека'")

    while loop == 10:
        if loop == 10:
            con_act = input("Хочешь попробовать еще раз? ")

        if con_act.lower() == "да":
            loop = 5

        elif con_act.lower() == "нет":
            exit()



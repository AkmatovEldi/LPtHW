people = 30
cars = 30
trucks = 400


if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("Thst's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")


if people > cars or trucks == cars:
    print("Мы можем поехать на любом")
elif people == cars and trucks > cars:
    print("То едем на Грузовиках")


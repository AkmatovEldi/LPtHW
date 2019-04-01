def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def age_person(name, age):
    print(f"Your name is {name}, you {age} old yers.")
    print("---------------\n")


print("Input value:")
age_person("Eldi", 23)


print("Input variables:")
name_person = "Kaha"
age_val = 21

age_person(name_person, age_val)


print("Input math")
age_person("Eldi"+"Kaha", 20 + 3)


print("Input with shell")
name_sh = input("Input name: ")
age_sh = input("Input age: ")
age_person(name_sh, age_sh)


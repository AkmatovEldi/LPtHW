def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b


def substract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b


def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

def add_multiply(a, b):
    print(f"Сначало прибавляем {a} + {b}, а потом умножаем на {b}")
    age = a + b
    return age * b

print("Let's do some math with just functions!")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
trushno = add_multiply(10, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, substract(height, multiply(weight, add_multiply(trushno, divide(iq, 2)))))

print("That becomes: ", what, "Can you do it by hand?")


print("My Function")

print(f"Сумма {trushno}")



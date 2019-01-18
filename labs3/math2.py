from random import randint, choice
from calc import eval
total = 0
while True:
    x = randint(0, 9)
    y = randint(1,9)
    error = randint(-1,1)
    pheptinh = choice(["+", "-", "*", "/"])
    r = eval(x, y,pheptinh) + error
    print(f"{x} {pheptinh} {y} = {r}")
    user_answer = input("Y/N ").upper()
    if user_answer == "Y":
        if error == 0:
            total += 1
        else:
            total += 0
            break
    elif user_answer == "N":
        if error == 0:
            total +=0
            break
        else:
            total += 1

print("Your Score: ", total)
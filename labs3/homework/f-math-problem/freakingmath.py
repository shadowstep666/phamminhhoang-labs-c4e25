from random import *
from calc import eval

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x=randint(0,9)
    y=randint(1,9)
    error=randint(-1,1)
    op=choice(["+","-","*","/"])
    result=eval(x, y,op) + error

    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    if user_choice == True:
        if result == eval(x, y, op):
            return True
        else:
            return False
    elif user_choice == False:
        if result == eval(x, y, op):
            return False
        else:
            return True

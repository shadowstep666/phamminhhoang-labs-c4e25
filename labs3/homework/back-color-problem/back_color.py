from random import *

def is_inside(positions, rectangle):
    if rectangle[0] <= positions[0] <= rectangle[0] + rectangle[2] and rectangle[1] <= positions[1] <= rectangle[3] + rectangle[1]:
        # print("True")
        return True
    else:
        # print("False")
        return False
shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    return [
                choice(["BLUE","RED","YELLOW","GREEN"]),
                choice(["#3F51B5","#C62828","#FFD600","#4CAF50"]),
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
# truong hop text xuat hien o duoi thi ta  chon theo ten
    if quiz_type == 0 :
        if text == "BLUE": 
            if is_inside([x,y],shapes[0]["rect"])==True:
                return True
            else:
                return False
        if text == "RED": 
            if is_inside([x,y],shapes[1]["rect"])==True:
                return True
            else:
                return False
        if text == "YELLOW": 
            if is_inside([x,y],shapes[2]["rect"])==True:
                return True
            else:
                return False
        if text == "GREEN": 
            if is_inside([x,y],shapes[0]["rect"])==True:
                return True
            else:
                return False
#truong hop text o phia tren thi chon theo mau
    elif quiz_type == 1: 
        if color == '#3F51B5':
            if is_inside([x,y], shapes[0]['rect']) == True:
                return True
            else:
                return False
        elif color == '#C62828':
            if is_inside([x,y], shapes[1]["rect"]) == True:
                return True
            else:
                return False
        elif color == '#FFD600':
            if is_inside([x,y], shapes[2]["rect"]) == True:
                return True
            else:
                return False
        elif color == '#4CAF50':
            if is_inside([x,y], shapes[3]['rect']) == True:
                return True
            else:
                return False

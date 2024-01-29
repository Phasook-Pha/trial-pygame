import random

def change_coor(coor, ran):
    change_x = random.randint(-ran, ran)
    change_y = random.randint(-ran, ran)
    return (coor[0] + change_x, coor[1] + change_y)

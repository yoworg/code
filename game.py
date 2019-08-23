from gameworld import Animal, draw_grid
import time

def cats():
    for i in range(2,8):
        yield Animal(row=i, col=i)


def mice():
    for i in range(7,1,-1):
        yield Animal(row=7, col=i)

mouse = Animal(row=7, col=7)

for cat, mouse in zip(cats(), mice()):
    draw_grid(cat, mouse)
    time.sleep(.4)
import time
import os
from pynput import keyboard
from map import Map
from helicopter import Helicopter

TICK_SLEEP = 0.150
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_WIDTH, MAP_HEIGHT = 10, 10
MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}

field = Map(MAP_WIDTH, MAP_HEIGHT)
field.generateForest(4, 10)
field.generateRiver(10)
field.generateRiver(20)

helicopter = Helicopter(MAP_WIDTH, MAP_HEIGHT)

tick = 1


def actionKey(key):
    global helicopter
    pressedKey = key.char
    print(pressedKey)
    if pressedKey in MOVES.keys():
        dx = MOVES[pressedKey][0]
        dy = MOVES[pressedKey][1]
        helicopter.move(dx, dy)


listener = keyboard.Listener(
    on_press=None,
    on_release=actionKey,
)
listener.start()

while True:
    os.system("cls")
    field.printMap(helicopter)
    tick += 1
    time.sleep(TICK_SLEEP)
    if tick % TREE_UPDATE == 0:
        field.generateTree()
    if tick % FIRE_UPDATE == 0:
        field.updateFires()

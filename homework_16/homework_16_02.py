# Создайте класс Черепашка, который хранит позиции x и y черепашки,
# а также s - количество клеточек, на которое она перемещается за ход
#
# у этого класс есть методы:
#
# go_up() - увеличивает y на s
# go_down() - уменьшает y на s
# go_left() - уменьшает x на s
# go_right() - увеличивает y на s
# evolve() - увеличивает s на 1
# degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
# count_moves(x2, y2) - возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции
import math
class Turtle:
    def __init__(self, x, y, s, x2, y2):
        self.x = x
        self.y = y
        self.s = s
        self.x2 = x2
        self.y2 = y2
    def go_up(self):
        self.y += self.s
    def go_down(self):
        self.y -= self.s
    def go_left(self):
        self.x -= self.s
    def go_right(self):
        self.x += self.s
    def evolve(self):
        self.s += 1
    def degrade(self):
        if (self.s > 1):
            self.s -= 1
    def count_moves(self):
        countX = self.x2 - self.x
        countY = self.y2 - self.y
        countXY = countX + countY
        countWithStepSize = math.floor(countXY / self.s)
        print(f'Минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции = {countWithStepSize}')

turtle = Turtle(1,1,1,50,30)

command = 0

while command != 69:
    print("Enter action:")
    print("1. up")
    print("2. down")
    print("3. left")
    print("4. right")
    print("5. evolve")
    print("6. degrade")
    print("7. count moves")
    print("69. stop")
    command = int(input())

    if command == 1:
        turtle.go_up()
    elif command == 2:
        turtle.go_down()
    elif command == 3:
        turtle.go_left()
    elif command == 4:
        turtle.go_right()
    elif command == 5:
        turtle.evolve()
    elif command == 6:
        turtle.degrade()
    elif command == 7:
        turtle.count_moves()
    elif command == 69:
        print("Goodbye, see you later!")
    else:
        print("Invalid action, enter action from menu")
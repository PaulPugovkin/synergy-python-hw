from utils import randCell

# 🚁

class Helicopter:
    def __init__(self, width, height):
        initLocation = randCell(width, height)
        rx, ry = initLocation[0], initLocation[1]
        self.x = rx
        self.y = ry
        self.height = height
        self.width = width

    def move(self, dx, dy):
        print('heli move')
        nx = dx + self.x
        ny = dy + self.y
        isInFrame = 0 <= nx < self.height and 0 <= ny < self.width
        if isInFrame:
            self.x, self.y = nx, ny


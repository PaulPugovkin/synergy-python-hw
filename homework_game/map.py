from utils import randBool, randCell, randCell2

# 0 поле 🟩
# 1 дерево 🌲
# 2 река 🟦
# 3 госпиталь 🏥
# 4 апгрейд шоп 🏪
# 5 огонь 🔥
# рамка ⬛

cellTypes = "🟩🌲🟦🏥🏪🔥"


class Map:

    def __init__(self, w, h):
        self.cells = [[0 for i in range(w)] for j in range(h)]
        self.width = w
        self.height = h

    def checkBounds(self, x, y):
        if x < 0 or y < 0 or x >= self.height or y >= self.width:
            return False
        return True

    def printMap(self, helicopter):
        print("⬛" * (self.width + 2))
        for ri in range(self.height):
            print("⬛", end="")
            for ci in range(self.width):
                cell = self.cells[ri][ci]
                if (helicopter.x == ri and helicopter.y == ci):
                    print("🚁", end="")
                elif 0 <= cell < len(cellTypes):
                    print(cellTypes[cell], end="")
            print("⬛")
        print("⬛ " * (self.width + 2))

    def generateRiver(self, l):
        rc = randCell(self.width, self.height)
        rx = rc[0]
        ry = rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randCell2(rx, ry)
            rx2 = rc2[0]
            ry2 = rc2[1]
            if self.checkBounds(rx2, ry2):
                if self.cells[rx2][ry2] != cellTypes[2]:
                    self.cells[rx2][ry2] = 2
                    rx, ry = rx2, ry2
                    l -= 1

    def generateForest(self, r, mxr):
        for row in range(self.height):
            for cell in range(self.width):
                if randBool(r, mxr):
                    self.cells[row][cell] = 1

    def generateTree(self):
        c = randCell(self.width, self.height)
        cx, cy = c[0], c[1]
        isTree = self.cells[cx][cy] == 1
        isFire = self.cells[cx][cy] == 5
        if self.checkBounds(cx, cy) and not isFire and not isTree:
            self.cells[cx][cy] = 1

    def addFire(self):
        c = randCell(self.width, self.height)
        cx, cy = c[0], c[1]
        isTree = self.cells[cx][cy] == 1
        if isTree:
            self.cells[cx][cy] = 5

    def updateFires(self):
        for row in range(self.height):
            for cell in range(self.width):
                cell = self.cells[row][cell]
                if cell == 5:
                    self.cells[row][cell] = 0
        for i in range(5):
            self.addFire()

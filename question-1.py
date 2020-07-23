def pathTodestination(x, y, destX, destY):
    if (x > destX or y > destY):
        return 0
    if (x == destX and y == destY):
        return 1
    toRight = pathTodestination(x + 1, y, destX, destY)
    toBottom = pathTodestination(x, y + 1, destX, destX)
    return toRight + toBottom

pathTodestination(0, 0, 7, 3)
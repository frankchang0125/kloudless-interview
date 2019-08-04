import re


def coordinate(pos):
    p = re.split(r'(\d+)', pos)
    y = int(p[1]) - 1
    x = ord(p[2]) - ord('A')
    return x, y


def solution(N, S, T):
    if len(S) == 0 or len(T) == 0:
      return "0,0"

    m = []

    for i in range(N):
        m.append([])
        for j in range(N):
            m[i].append(-1)

    positions = S.split(',')
    ship = 0
    shipSizes = []

    for i in range(len(positions)):
        start, end = positions[i].split(' ')
        startX, startY = coordinate(start)
        endX, endY = coordinate(end)

        size = 0
        for y in range(startY, endY + 1):
            for x in range(startX, endX + 1):
                m[y][x] = ship
                size += 1
        shipSizes.append(size)
        ship += 1

    hits = T.split(' ')
    hitCounts = [0 for x in range(len(shipSizes))]

    for i in range(len(hits)):
        x, y = coordinate(hits[i])
        ship = m[y][x]
        if ship >= 0:
            hitCounts[ship] += 1
        m[y][x] = -1

    sunk = 0
    hit = 0

    for i in range(len(shipSizes)):
        if hitCounts[i] == shipSizes[i]:
            sunk += 1
        elif hitCounts[i] != 0:
            hit += 1

    return "{},{}".format(sunk, hit)

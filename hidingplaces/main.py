from collections import deque

def toCoordinates(square):
    return (ord(square[0]) - ord('a'), int(square[1])-1)

def toSquare(coords):
    return f'{chr(coords[0] + ord("a"))}{coords[1]+1}'

def neighbors(square):
    if square[0] - 2 >= 0 and square[1] - 1 >= 0:
        yield (square[0] - 2, square[1] - 1)
    if square[0] - 1 >= 0 and square[1] - 2 >= 0:
        yield (square[0] - 1, square[1] - 2)
    if square[0] - 2 >= 0 and square[1] + 1 < 8:
        yield (square[0] - 2, square[1] + 1)
    if square[0] - 1 >= 0 and square[1] + 2 < 8:
        yield (square[0] - 1, square[1] + 2)
    if square[0] + 2 < 8 and square[1] - 1 >= 0:
        yield (square[0] + 2, square[1] - 1)
    if square[0] + 1 < 8 and square[1] - 2 >= 0:
        yield (square[0] + 1, square[1] - 2)
    if square[0] + 2 < 8 and square[1] + 1 < 8:
        yield (square[0] + 2, square[1] + 1)
    if square[0] + 1 < 8 and square[1] + 2 < 8:
        yield (square[0] + 1, square[1] + 2)

def main():
    n = int(input())
    for _ in range(n):
        isFound = [[False for _ in range(8)] for _ in range(8)]
        currLayer = []
        currMaxDist = 0
        inCoord = toCoordinates(input())
        fringe = deque([(0, inCoord)])
        isFound[inCoord[0]][inCoord[1]] = True
        while len(fringe) > 0:
            currElement = fringe.popleft()
            if currElement[0] > currMaxDist:
                currLayer = []
                currMaxDist = currElement[0]
            currLayer.append(currElement[1])
            for neighbor in neighbors(currElement[1]):
                if not isFound[neighbor[0]][neighbor[1]]:
                    fringe.append((currElement[0]+1, neighbor))
                    isFound[neighbor[0]][neighbor[1]] = True
        print(currMaxDist, end='')
        for c in sorted(currLayer, key=lambda x : 10 * (8 - x[1]) + (x[0])):
            print(f' {toSquare(c)}', end='')
        print()

if __name__ == '__main__':
    main()
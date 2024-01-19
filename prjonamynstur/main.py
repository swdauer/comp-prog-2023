def stitchSize(c):
    if c == ".":
        return 20
    elif c == "O":
        return 10
    elif c == "\\":
        return 25
    elif c == "/":
        return 25
    elif c == "A":
        return 35
    elif c == "^":
        return 5
    elif c == "v":
        return 22

if __name__ == "__main__":
    n = int(input().split()[0])

    totalSize = 0
    for i in range(n):
        line = input()
        for c in line:
            totalSize += stitchSize(c)
    print(totalSize)
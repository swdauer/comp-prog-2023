nx = tuple(map(int, input().split()))
numNeeded = sum([int(input()) for _ in range(nx[0])])
if nx[1] >= numNeeded:
    print("Jebb")
else:
    print("Neibb")
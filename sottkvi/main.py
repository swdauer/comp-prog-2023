if __name__ == '__main__':
    firstLine = tuple(map(int, input().split()))
    n = firstLine[0]
    k = firstLine[1]
    d = firstLine[2]
    numFriends = 0
    for _ in range(n):
        val = int(input())
        if val + 13 < k + d:
            numFriends += 1
    print(numFriends)
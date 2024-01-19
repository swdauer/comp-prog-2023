if __name__ == '__main__':
    n = int(input())
    sums = [0, 0, 0]
    for _ in range(n):
        for i, c in enumerate(input().split()):
            sums[i] += 1 if c == 'J' else 0
    print(min(min(sums[0], sums[1]), sums[2]))
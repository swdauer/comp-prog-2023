def main():
    n = int(input())
    runningTotal = 0
    for _ in range(n):
        gb = tuple(map(int, input().split()))
        runningTotal += gb[0]
        if runningTotal < gb[1]:
            print('impossible')
            return
    print('possible')

if __name__ == '__main__':
    main()
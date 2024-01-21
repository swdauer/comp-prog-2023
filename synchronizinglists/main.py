def main():
    firstIter = True
    while True:
        n = int(input())
        if n == 0:
            return

        if not firstIter:
            print()
        else:
            firstIter = False
        
        l1 = [int(input()) for _ in range(n)]
        l2 = [int(input()) for _ in range(n)]

        sortls = dict(zip(sorted(l1), sorted(l2)))
        for x in l1:
            print(sortls[x])

if __name__ == '__main__':
    main()
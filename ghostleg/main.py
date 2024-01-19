def main():
    nm = tuple(map(int, input().split()))
    l = [x+1 for x in range(nm[0])]
    for _ in range(nm[1]):
        swap = int(input())
        l[swap-1], l[swap] = l[swap], l[swap-1]
    for i in l:
        print(i)

if __name__ == '__main__':
    main()
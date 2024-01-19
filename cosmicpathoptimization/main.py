def main():
    m = int(input())
    ave = sum(map(int, input().split())) // m
    print(ave)

if __name__ == '__main__':
    main()
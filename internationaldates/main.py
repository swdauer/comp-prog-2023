def main():
    i = tuple(map(int, input().split('/')))
    if (i[0] > 12):
        print('EU')
    elif (i[1] > 12):
        print('US')
    else:
        print('either')

if __name__ == '__main__':
    main()
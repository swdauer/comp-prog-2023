import math

def main():
    pw = tuple(map(int, input().split()))
    numPounds = math.floor(pw[1] * pw[0] / 100)
    print('[' + '#' * numPounds + '-' * (pw[1] - numPounds) + '] |', end='')
    if pw[0] < 10:
        print('   ', end='')
    elif pw[0] < 100:
        print('  ', end='')
    else:
        print(' ', end='')
    print(pw[0], '%', sep='')

if __name__ == '__main__':
    main()
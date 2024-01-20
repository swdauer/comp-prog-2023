def main():
    k = int(input())
    a = int(input())
    b = int(input())
    output = []
    for i in range(k // a + 1):
        if (k - i * a) % b == 0:
            output.append((i, (k - i * a) // b))
    print(len(output))
    for o in output:
        print(f'{o[0]} {o[1]}')


if __name__ == '__main__':
    main()
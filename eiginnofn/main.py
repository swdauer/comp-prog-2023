def constructNameSets(names):
    a, b, c = [], [], []
    for n in names:
        if len(n) == 1:
            a.append(n[0])
        else:
            b.append(n[0])
            c.append(n)
    return [frozenset(a), frozenset(b), dict(c)]


def main():
    n = int(input())
    names = constructNameSets(map(lambda _ : tuple(input().split()), range(n)))
    m = int(input())
    for _ in range(m):
        name = input()
        if name in names[0]:
            print('Jebb')
        elif name in names[1]:
            print(f'Neibb en {name} {names[2][name]} er heima')
        else:
            print('Neibb')

if __name__ == '__main__':
    main()
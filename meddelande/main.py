import functools

if __name__ == '__main__':
    letterTuples = []
    n = int(input().split()[0])
    for i in range(n):
        line = input()
        for j, c in enumerate(line):
            if c != '.':
                letterTuples.append((c, i+j))
    print(functools.reduce(lambda a, b : a + b[0],
                           sorted(letterTuples,
                                  key=lambda x : x[1]),
                           ""))
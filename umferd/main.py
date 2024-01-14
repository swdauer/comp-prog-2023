n = int(input())
m = int(input())
numEmpties = sum(map(lambda x : sum(map(lambda y : 1 if y == "." else 0, x)),
                [input() for _ in range(m)]))
print(numEmpties / (n*m))
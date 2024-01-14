input()

def probability(n):
    numOccurances = 6 - abs(7 - n)
    return numOccurances / 36

print(sum(map(lambda x : probability(int(x)), input().split())))
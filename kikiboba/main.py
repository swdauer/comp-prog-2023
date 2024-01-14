def count(word, letter):
    return sum(map(lambda x : 1 if x == letter else 0, word))

word = input()
kCount = count(word, "k")
bCount = count(word, "b")
if kCount == 0 and bCount == 0:
    print("none")
elif kCount > bCount:
    print("kiki")
elif bCount > kCount:
    print("boba")
else:
    print("boki")
s = input()
l = input()
word = [s[int(l[i*3:i*3+3])-1] for i in range(len(l) // 3)]
print("".join(word))
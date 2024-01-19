word1 = input()
word2 = input()
output = ""

i = 0
j = 0
while i < len(word1) and j < len(word2):
    if word1[i] < word2[j]:
        output += word1[i]
        i += 1
    else:
        output += word2[j]
        j += 1

if i < len(word1):
    output += word1[i:]
elif j < len(word2):
    output += word2[j:]

print(output)
input()
output = ""
for word in input().split():
    if word[0].isupper():
        output += word[0]
print(output)
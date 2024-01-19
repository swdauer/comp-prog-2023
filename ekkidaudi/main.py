
if __name__ == "__main__":
    word1 = input().split("|")
    word2 = input().split("|")
    output = ""
    for i in range(len(word1) * 2):
        if i % 2 == 0:
            output += word1[i//2]
        else:
            output += word2[(i-1)//2] + ' '
    print(output)
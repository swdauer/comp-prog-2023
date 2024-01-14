import functools

if __name__ == "__main__":
    n = int(input())
    words = [input().encode() for _ in range(n)]
    outputLength = functools.reduce(lambda x, y : max(x, y), map(len, words))
    output = bytearray(outputLength)
    for i in range(outputLength):
        numLetters = 0
        currByte = 0
        for word in words:
            if len(word) > i:
                numLetters += 1
                currByte += word[i]
        output[i] = currByte // numLetters
    print(output.decode())

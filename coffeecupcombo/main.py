if __name__ == "__main__": 
    length = int(input())
    lectures = input()

    numCups = 0
    numAttended = 0
    for i in lectures:
        if i == "1":
            numAttended += 1
            numCups = 2
        else:
            if numCups > 0:
                numAttended += 1
                numCups -= 1
    print(numAttended)

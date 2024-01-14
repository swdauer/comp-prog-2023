windSpeed = int(input())
numRoads = int(input())

for _ in range(numRoads):
    roadSpeedPair = tuple(input().split())
    if int(roadSpeedPair[1]) >= windSpeed:
        print(roadSpeedPair[0], "opin")
    else:
        print(roadSpeedPair[0], "lokud")
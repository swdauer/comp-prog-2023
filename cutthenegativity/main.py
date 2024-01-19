n = int(input())
output = []
for i in range(n):
    flights = map(int, input().split())
    for j, flight in enumerate(flights):
        if flight != -1:
            output.append(f"{i+1} {j+1} {flight}")

print(len(output))
[print(x) for x in output]
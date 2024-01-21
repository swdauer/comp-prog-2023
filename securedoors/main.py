def main():
    n = int(input())
    building = {}
    for _ in range(n):
        line = input().split()
        if line[0] == 'entry':
            if not (line[1] in building) or building[line[1]] == False:  
                building[line[1]] = True
                print(f'{line[1]} entered')
            else:
                print(f'{line[1]} entered (ANOMALY)')
        else:
            if not (line[1] in building) or building[line[1]] == False:
                building[line[1]] = False
                print(f'{line[1]} exited (ANOMALY)')
            else:
                building[line[1]] = False
                print(f'{line[1]} exited')

if __name__ == '__main__':
    main()
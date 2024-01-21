def isGreater(curr, wl):
    csum = sum(curr)
    wlsum = sum(wl)
    if wlsum == 0:
        return True
    elif wlsum * curr[0] > csum * wl[0]:
        return True
    else:
        return False

def main():
    n = int(input())
    score = reversed(input())
    
    winLoss = [0, 0]
    currMaxWinLoss = [0, 0]
    for i, s in enumerate(score):
        if i == 0 and s == 'G':
            print('1-0')
            return
        if s == 'G':
            winLoss[0] += 1
        elif s == 'A':
            winLoss[1] += 1
        if isGreater(winLoss, currMaxWinLoss):
            currMaxWinLoss = winLoss.copy()

    if currMaxWinLoss[0] == 0 and currMaxWinLoss[1] == 0:
        print('0-0')
    elif currMaxWinLoss[0] == 0:
        print('0-1')
    else:
        print(f'{currMaxWinLoss[0]}-{currMaxWinLoss[1]}')

if __name__ == '__main__':
    main()
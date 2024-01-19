def main():
    levelNames = [
        'Logn',
        'Andvari',
        'Kul',
        'Gola',
        'Stinningsgola',
        'Kaldi',
        'Stinningskaldi',
        'Allhvass vindur',
        'Hvassvidri',
        'Stormur',
        'Rok',
        'Ofsavedur',
        'Farvidri'
    ]
    levels = [
        3, 16, 34,
        55, 80, 108,
        139, 172, 208,
        245, 285, 327
    ]
    windStr = tuple(map(int, input().split('.')))
    wind = windStr[0]*10 + windStr[1]
    for i, l in enumerate(levels):
        if wind < l:
            print(levelNames[i])
            return
    print(levelNames[-1])

if __name__ == '__main__':
    main()
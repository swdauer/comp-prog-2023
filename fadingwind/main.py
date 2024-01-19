def main():
    hkvs = list(map(int, input().split()))
    h, k, v, s = hkvs[0], hkvs[1], hkvs[2], hkvs[3]
    dist = 0
    while h > 0:
        v = (v + s) - max(1, (v+s) // 10)
        if v >= k:
            h += 1
        elif v > 0:
            h -= 1
            if h == 0:
                v = 0
        if v <= 0:
            h = 0
            v = 0
        dist += v
        if s > 0:
            s -= 1
    print(dist)


if __name__ == '__main__':
    main()
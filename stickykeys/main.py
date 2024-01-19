import io

def main():
    word = input()
    prev = ''
    output = io.StringIO()
    for c in word:
        if c != prev:
            output.write(c)
        prev = c
    print(output.getvalue())

if __name__ == '__main__':
    main()
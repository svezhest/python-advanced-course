import sys


def main():
    if len(sys.argv) == 1:
        f = sys.stdin
    elif len(sys.argv) == 2:
        f = open(sys.argv[1])
    else:
        print('Usage: python 1.1.py file.txt')
        sys.exit(1)

    for idx, line in enumerate(f):
        print('{spaces}{idx}  {line}'.format(spaces=' ' *
              (6 - len(str(idx + 1))), idx=idx + 1, line=line), end='')

    f.close()


if __name__ == '__main__':
    main()

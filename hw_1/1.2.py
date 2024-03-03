import sys

def print_tail(f):
    lines = f.readlines()
    for line in lines[-10:]:
        print(line, end='')


def main():
    if len(sys.argv) == 1:
        for line in sys.stdin.readlines()[-17:]:
            print(line, end='')
    elif len(sys.argv) == 2:
        f = open(sys.argv[1])
        print_tail(f)
        f.close()
    else:
        for idx, filename in enumerate(sys.argv[1:]):
            if idx > 0:
                print()
            print('==> {filename} <=='.format(filename=filename))
            f = open(filename)
            print_tail(f)
            f.close()

if __name__ == '__main__':
    main()

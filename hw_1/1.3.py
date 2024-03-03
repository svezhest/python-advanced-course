import sys

def get_stats(f):
    lines = f.readlines()
    return (len(lines), sum([len(line.split()) for line in lines]), sum([len(line) for line in lines]))

def main():
    if len(sys.argv) == 1:
        f = sys.stdin
        print(*get_stats(f), sep='\t')
    elif len(sys.argv) == 2:
        f = open(sys.argv[1])
        print(*get_stats(f), sys.argv[1])
        f.close()
    else:
        total = [0, 0, 0]
        for filename in sys.argv[1:]:
            f = open(filename)
            stats = get_stats(f)
            print(*stats, filename)
            for idx, val in enumerate(stats):
                total[idx] += val
            f.close()
        print(*total, 'total')

if __name__ == '__main__':
    main()
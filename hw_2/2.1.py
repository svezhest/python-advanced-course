from latex_generators import generate_latex_table


def main():
    a, b, c = 7, 8, 9
    matrix = [
        [1, 2, 3],
        ["d", "e", "f"],
        [a, b, c]
    ]

    text = '\\documentclass{article}\n\\begin{document}\n' + \
        generate_latex_table(matrix) + '\n\\end{document}'
    with open('artifacts/2.1.txt', 'w') as f:
        f.write(text)


if __name__ == "__main__":
    main()

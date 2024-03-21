# После этого, используя вашу библиотеку,
# сгенерировать по полученному латеху PDF
# с таблицей из задачи 2.1 и картинкой.
# PDF -  первый артефакт задачи,
# ссылка на репозиторий в PyPI/Anaconda - второй.

import os
from latex_generators import generate_latex_table, insert_image_latex


def main():
    a, b, c = 7, 8, 9
    matrix = [
        [1, 2, 3],
        ["d", "e", "f"],
        [a, b, c]
    ]

    text = '\\documentclass{article}\n\\usepackage{graphicx}\n\\begin{document}\n' + \
        generate_latex_table(
            matrix) + '\n\\\\\\\\\n' + insert_image_latex('../resources/1.png') + '\n\\end{document}'
    
    # totally bad and not recommended way
    os.chdir('hw_2/artifacts')

    with open('2.2.tex', 'w') as f:
        f.write(text)

    os.system('pdflatex 2.2.tex')


if __name__ == "__main__":
    main()

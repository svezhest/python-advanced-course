def generate_latex_table(matrix):
    assert len(matrix) > 0

    begin = '\\begin{tabular}{|' + '|'.join(['c'] * (len(matrix[0]))) + '|}'
    end = '\\end{tabular}'

    return '\n\\hline\n'.join(
        (
            begin,
            *(' & '.join(map(str, row)) + ' \\\\' for row in matrix),
            end
        )
    )


def insert_image_latex(image_path):
    return f'\\begin{{figure}}\n\\centering\n\\end{{figure}}\\includegraphics[width=\\textwidth]{{"{image_path}"}}\n'

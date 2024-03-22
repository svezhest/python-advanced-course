import numpy as np
from matrix_mixin import Matrix


def main():
    np.random.seed(0)
    matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))

    matrix3 = matrix1 + matrix2
    matrix4 = matrix1 @ matrix2
    matrix5 = matrix2 * matrix2

    artifacts_dir = 'hw_3/artifacts/3.2'

    matrix3.save(f'{artifacts_dir}/matrix+.txt')
    matrix4.save(f'{artifacts_dir}/matrix@.txt')
    matrix5.save(f'{artifacts_dir}/matrix*.txt')


if __name__ == '__main__':
    main()

from matrix import Matrix
import numpy as np

def main():
    np.random.seed(0)
    matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))

    matrix3 = matrix1 + matrix2
    matrix4 = matrix1 @ matrix2
    matrix5 = matrix2 * matrix2

    artifacts_dir = 'hw_3/artifacts/3.1'
    with open(f'{artifacts_dir}/matrix+.txt', 'w') as f:
        f.write(str(matrix3))
    with open(f'{artifacts_dir}/matrix@.txt', 'w') as f:
        f.write(str(matrix4))
    with open(f'{artifacts_dir}/matrix*.txt', 'w') as f:
        f.write(str(matrix5))
    
if __name__ == '__main__':
    main()

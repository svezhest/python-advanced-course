class Matrix:
    def __init__(self, data):
        self.data = data

    def check_dims(self, other):
        return len(self.data) == len(other.data) and (len(self.data) == 0 or len(self.data[0]) == len(other.data[0]))

    def __add__(self, other):
        if not self.check_dims(other):
            raise ValueError("shape(Matrix A) != shape(Matrix B)")

        return Matrix([[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(self.data, other.data)])

    def __mul__(self, other):
        if not self.check_dims(other):
            raise ValueError("shape(Matrix A) != shape(Matrix B)")

        return Matrix([[a * b for a, b in zip(row1, row2)] for row1, row2 in zip(self.data, other.data)])

    def __matmul__(self, other):
        rows = len(self.data)

        if rows == 0:
            raise ValueError("cannot multiply a matrix with no rows")

        cols = len(self.data[0])

        if cols == 0:
            raise ValueError("cannot multiply a matrix with no columns")

        other_rows = len(other.data)

        if other_rows != cols:
            raise ValueError("shape(transpose(Matrix A)) != shape(Matrix B)")

        other_cols = len(other.data[0])

        if other_cols != rows:
            raise ValueError("shape(transpose(Matrix A)) != shape(Matrix B)")

        res = [[0 for _ in range(rows)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                for k in range(rows):
                    res[i][k] += self.data[i][j] * other.data[j][k]

        return Matrix(res)

    def __str__(self):
        return '[' + ',\n'.join(f'[{", ".join(map(str, row))}]' for row in self.data) + ']'
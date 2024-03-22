import numpy as np


class GetSetMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = np.array(value)


class StrMixin:
    def __str__(self):
        return '[' + ',\n'.join(f'[{", ".join(map(str, row))}]' for row in self.data) + ']'


class FileMixin:
    def save(self, path):
        with open(path, "w") as f:
            f.write(str(self))


class Matrix(GetSetMixin, StrMixin, FileMixin):
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        return Matrix(np.add(self.data, other.data))

    def __mul__(self, other):
        return Matrix(np.multiply(self.data, other.data))

    def __matmul__(self, other):
        return Matrix(np.dot(self.data, other.data))

    def __sub__(self, other):
        return Matrix(np.subtract(self.data, other.data))

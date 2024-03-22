import numpy as np
import matrix_mixin


class HashMixin:
    # простой хэш, напоминающий реальный хэщ для строки,
    # только не использующий степени, и за счёт этого
    # легко приводящий к коллизиям. кроме того,
    # коллизии возникнут при преобразовании float -> int.
    # оно и прекрасно. мы же хотим коллизии
    def __hash__(self) -> int:
        res = 0

        for i, row in enumerate(self.data):
            for j, x in enumerate(row):
                res += ((i + 7) * ((j + 5) * x + 3) + 1)
                res %= 1_000_000_007

        return int(res)


cache = {}


class Matrix(matrix_mixin.Matrix, HashMixin):
    def __matmul__(self, other):
        key = f'{hash(self)}${hash(other)}'
        if key in cache:
            return cache[key]

        res = super().__matmul__(other)
        cache[key] = res
        return res


def main():
    a = Matrix([[1.35, 2], [0, 5]])
    b = Matrix([[1, 1], [1, 1]])
    c = Matrix([[0.1, 2], [1.1, 5]])
    d = b
    ab = a @ b
    cd_fake = c @ d

    artifacts_dir = 'hw_3/artifacts/3.3'

    ab.save(f'{artifacts_dir}/ab.txt')
    cd_fake.save(f'{artifacts_dir}/cd_fake.txt')

    cache.clear()

    cd = c @ d
    cd.save(f'{artifacts_dir}/cd.txt')

    with open(f'{artifacts_dir}/hash.txt', 'w') as f:
        f.write(
            f'hash a: {hash(a)}\nhash b: {hash(b)}\nhash c: {hash(c)}\n' +
            f'hash d: {hash(d)}\nhash ab: {hash(ab)}\nhash cd_fake: {hash(cd_fake)}\nhash cd: {hash(cd)}')


if __name__ == '__main__':
    main()

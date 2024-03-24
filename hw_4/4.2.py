import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import multiprocessing
import sys

from helpers import timeit


def integrate(f, a, b, *, n_jobs=1, n_iter=1000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


def integrate_get_chunks(a, b, *, n_chunks, n_iter):
    step = (b - a) / n_iter
    chunk_size = n_iter // n_chunks
    return [[((a + i * step), step) for i in range(start, min(start + chunk_size, n_iter))] for start in range(0, n_iter, chunk_size)]


def chunk_job(f, chunk):
    return sum(f(x) * step for x, step in chunk)


def integrate_parallel(executor, f, chunks):
    futures = [executor.submit(chunk_job, f, chunk) for chunk in chunks]
    return sum(future.result() for future in futures)


def integrate_threads(f, a, b, *, n_jobs, n_iter):
    print(f'jobs = {n_jobs}, ', end='')
    res = None
    chunks = integrate_get_chunks(a, b, n_chunks=n_jobs * 10, n_iter=n_iter)
    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        res = integrate_parallel(executor, f, chunks)
    print(f'res = {res}, ', end='')


def integrate_processes(f, a, b, *, n_jobs, n_iter):
    print(f'jobs = {n_jobs}, ', end='')
    res = None
    chunks = integrate_get_chunks(a, b, n_chunks=n_jobs * 10, n_iter=n_iter)
    with ProcessPoolExecutor(max_workers=n_jobs) as executor:
        res = integrate_parallel(executor, f, chunks)
    print(f'res = {res}, ', end='')


def single_job(f, a, b, *, n_iter):
    print(f'jobs = {1}, ', end='')
    res = integrate(f, a, b, n_jobs=1, n_iter=n_iter)
    print(f'res = {res}, ', end='')


def main():
    n_iter = 10_000_000
    print(f'n_iter = {n_iter}')

    print(
        'jobs = {n_jobs}, res = {integrate(*args)}, {method_name} execution_time')

    timeit(single_job, math.cos, 0, math.pi / 2, n_iter=n_iter)

    for n_jobs in range(1, multiprocessing.cpu_count() * 2):
        timeit(integrate_threads, math.cos, 0,
               math.pi / 2, n_jobs=n_jobs, n_iter=n_iter)

    for n_jobs in range(1, multiprocessing.cpu_count() * 2):
        timeit(integrate_processes, math.cos, 0,
               math.pi / 2, n_jobs=n_jobs, n_iter=n_iter)


if __name__ == "__main__":
    main()

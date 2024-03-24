import time


def timeit(job, *args, **kwargs):
    start = time.perf_counter()
    job(*args, **kwargs)
    end = time.perf_counter()
    print(job.__name__, end - start)

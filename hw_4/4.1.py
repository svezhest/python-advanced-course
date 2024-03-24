'''
Взять функцию подсчета чисел Фибоначчи и сравнить время исполнения кода 
(вызова функции от большого числа n (чтобы была видна разница в запусках на потоках и процессах) 
10 раз через 10 потоков\процессов) при использовании threading и multiprocessing

Необходимо сравнить время выполнения при синхронном запуске, использовании потоков и процессов. 

Артефакт - текстовый файл с результатами запуска различными методами.
'''

import sys
import threading
import multiprocessing

from helpers import timeit


def fibonacci(n):
    if n < 0:
        raise ValueError('n must be positive')
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def single_thread(x, n_times):
    for _ in range(n_times):
        fibonacci(x)


def many_threads(x, n_threads):
    threads = [threading.Thread(target=fibonacci, args=(x, ))
               for _ in range(n_threads)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def many_processes(x, n_processes):
    processes = [multiprocessing.Process(
        target=fibonacci, args=(x,)) for _ in range(n_processes)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()


def main():
    sys.stdout = open('hw_4/artifacts/4.1.txt', 'w')
    n = 10
    x = 33

    timeit(single_thread, x, n)
    timeit(many_threads, x, n)
    timeit(many_processes, x, n)


if __name__ == '__main__':
    main()

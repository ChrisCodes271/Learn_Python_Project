# This time I will attempt to create a method that will allow me to count to 1000000000 with 8 processes running
# simultaniously. I want to condense it down as far as possible.

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    start = time.perf_counter()  # establish start time.
    for i in range(17):  # while loop that will create a new process.
        core = []  # establish core list
        p = Process(target=counter, args=(62500000,))
        p.start()
        core.append(p)
    for process in core:
        process.join()

    stop = time.perf_counter()  # establish stop time
    elapsed_time = stop - start  # Calculate total time elapsed.
    print(elapsed_time)


if __name__ == '__main__':
    main()
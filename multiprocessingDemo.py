# multiprocessing = running tasks in paralell on different cpu cores, bypass GIL used for threading.
# better for cpu bound task (heavy cpu usage) vs. multithreading which is better for io bound tasks.

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    start = time.perf_counter()

    a = Process(target=counter, args=(62500000,))

    # Initial a process counting to 1000000000 took 45 seconds. Lets multiprocess and split the work with b below.

    b = Process(target=counter, args=(62500000,))

    # When multiprocessing with 2 processes it took 23  seconds. Lets DOUBLE it to FOUR!

    c = Process(target=counter, args=(62500000,))

    d = Process(target=counter, args=(62500000,))

    # With 4 processes it took only 13 seconds! But I'm crazy and I have 16 cores... so I'll double it AGAIN!

    e = Process(target=counter, args=(62500000,))

    f = Process(target=counter, args=(62500000,))

    g = Process(target=counter, args=(62500000,))

    h = Process(target=counter, args=(62500000,))

    # With multiprocessing utilizing 8 cores. I was able to take a task that took 8 seconds and cut it down to 8 seocnds!

    i = Process(target=counter, args=(62500000,))

    j = Process(target=counter, args=(62500000,))

    k = Process(target=counter, args=(62500000,))

    l = Process(target=counter, args=(62500000,))

    m = Process(target=counter, args=(62500000,))

    n = Process(target=counter, args=(62500000,))

    o = Process(target=counter, args=(62500000,))

    p = Process(target=counter, args=(62500000,))

    # *EVIL SCIENTIST LAUGH* Only 6 seconds this time. Definitely DR when creating and running new processes.

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()
    i.start()
    j.start()
    k.start()
    l.start()
    m.start()
    n.start()
    o.start()
    p.start()

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()
    i.join()
    j.join()
    k.join()
    l.join()
    m.join()
    n.join()
    o.join()
    p.join()

    stop = time.perf_counter()
    elapsed = stop - start

    print('Finished in:', elapsed, ' Seconds.')

    print(cpu_count())


if __name__ == '__main__':  # setting if __name__ == main allows you to avoid hiccups.
    # Just call main() at the end of your code and put all your code in the main function.
    main()

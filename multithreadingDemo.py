# thread = a flow of execution. Like a seperate order of instructions.
# Each thread takes a turn running to achieve concurrency
# GIL = Global interpreter lock is the limiting factor
# allows 1 thread to hold control of the interpreter at a time

# 2 categories

# CPU bound = program / task spends most of its time waiting for internal events (CPU intensive)
# multiprocessing

# IO bound = program / task spends most of time waiting for external events (user input, web scraping)
# multithreading

import threading
import time

def eat_breakfast(): #3 functions with seperate times. Lets run them all together below
    time.sleep(3)
    print('You had breakfast')

def drink_coffee():
    time.sleep(4)
    print('You drank coffee')

def study():
    time.sleep(5)
    print('You finished studying')

#eat_breakfast() #In this showing of the functions. One thread is being used . Total time is 12 seconds... long time
#drink_coffee()
#study()

x = threading.Thread(target=eat_breakfast, args=()) #you can throw args in this as well
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join() #This will cause code after this point to wait
y.join()
z.join()

print(threading.active_count()) #Show active thread
print(threading.enumerate())
print(time.perf_counter()) #this will show how long it takes main thread to do its instructions.


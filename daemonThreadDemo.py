#daemon thread = a thread that runs in the background, not important for program to run
# program will not wait for daemon threads to complete before exiting
# non-daemon threads cannot normally be killed, stay alive until task in complete

# ex. background tasks, garbage collection, io waiting, long running process, etc.

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print()
        print('Active for: ', count, ' seconds.')

x = threading.Thread(target=timer,daemon=True)
x.setDaemon(False) #This will set something as a daemon or non daemon. Must be done before start function
x.isDaemon() #This will check if something is a daemon
x.start()


answer = input('Do you wish to exit?')


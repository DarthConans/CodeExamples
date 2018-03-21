import threading
from random import randint

shared_resource = []

def write_to_list(list):
    for i in range(1000):
        if len(list) < 10:
            list.append(randint(0, 9))
        else:
            list.pop()
            list.append(randint(0, 9))
        if i % 200 == 0:
            print len(list)

threads = []
for j in range(3):
    threads.append(threading.Thread(target = write_to_list, args=(shared_resource,)))
    threads[j].start()
for thread in threads:
    thread.join()
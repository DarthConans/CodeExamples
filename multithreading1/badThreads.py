import threading
import time

long_array = range(1, 100000000)

def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts]
             for i in range(wanted_parts) ]

def square_array(array):
    for i in range(len(array)):
        array[i] = array[i] * array[i]


start = time.time()
for i in range(2):
    square_array(long_array)
    print i
end = time.time()
print "Non-threaded took " + str(end - start) + " seconds."

shorter_arrays = split_list(long_array, 4)
start = time.time()
for i in range(2):
    threads = []
    for j in range(4):
        threads.append(threading.Thread(target = square_array, args=(shorter_arrays[i],)))
        threads[j].start()
    for thread in threads:
        thread.join()
    print i
end = time.time()
print "Threaded took " + str(end - start) + " seconds."




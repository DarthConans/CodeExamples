import pickle
import threading
import time
import concurrent.futures as confu

def read_file(filename, dest_list):
    f = open(filename, 'r')
    local_list = pickle.load(f)
    f.close()
    for i in range(len(local_list)):
        local_list[i] = local_list[i] * local_list[i]
    dest_list.append(local_list)

dest_list = []

start = time.time()
for i in range(100):
    name = "data" + str(i) + ".txt"
    read_file(name, dest_list)
end = time.time()
print len(dest_list)
print "Non-threaded took " + str(end - start) + " seconds."

threads = []
dest_list = []
start = time.time()
for i in range(100):
    name = "data" + str(i) + ".txt"
    threads.append(threading.Thread(target = read_file, args=(name, dest_list)))
    threads[i].start()
for thread in threads:
    thread.join()
end = time.time()
print len(dest_list)
print "Threaded took " + str(end - start) + " seconds."


dest_list = []
start = time.time()
pool = confu.ThreadPoolExecutor(max_workers = 5)
for i in range(100):
    name = "data" + str(i) + ".txt"
    pool.submit(read_file, name, dest_list)
pool.shutdown()
end = time.time()
print len(dest_list)
print "Thread Pool took " + str(end - start) + " seconds."
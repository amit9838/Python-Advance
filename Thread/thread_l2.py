# Creating multiple threads
# Comparing execution time between threads and normal execution 

import threading
import time


def sleeper(n, name):
    print(f"Start : Hi im {name} and im going to sleep for {n} seconds.\n>>>>>>>>\n")
    time.sleep(n)
    print(f"End: {name} has woken up from sleep\n<<<<<<<<<\n")


thread_list = []

sample_size = 6

# Executing using threads
t_start = time.time()
for i in range(sample_size):
    t = threading.Thread(target=sleeper,name=f"thread{i}",args=(i,f"thread{i}"))
    t.start()
    print(f"thread{t.name} has started")
    thread_list.append(t)
    
# Join all the threads
for t in thread_list:
    t.join()
    
t_end = time.time()

print("Total execution time for threads : {}".format(t_end-t_start))

# Executing using iteration
t_start = time.time()
for i in range(sample_size):
    sleeper(i,f"Iteration{i}")
    
    
t_end = time.time()
print("Total execution time for iteration : {}".format(t_end-t_start))


""" Threading:
    # Threads concept:
    - In threading , multuple processes runs simultaneously utilizing the muliprocessing architecture 
      to run diffrent diffrent threads on diffrent processers.
    - These threads runs independent of other threads.
    
    # Threading in python: 
    - It it very much possible that when two threads runs independely then there is a change of,
      race condition when two threads try to access the same variable at the same time.
    - In python there is a technique called global lock which prevents such incindents, with this technique
      python allows only one thread to execute at point of time, these threads are executed by switching b/w
      diffrent threads, this switching is so fast so that it seems like all the threads are running the same
      time.
    - python provides a bulit-in module in called 'threading' which provides this functionality.
    """

import threading
import time

# Thread applies to a method/function and uses it as target


def sleeper(n, name):
    print(f"Hi im {name} and im going to sleep for {n} seconds.\n")
    time.sleep(n)
    print(f"{name} has woken up from sleep\n")


thread = threading.Thread(target=sleeper, args=(5, "thread-1"))

thread.start()

# .join() method of thread restricts the main thread from running untill, given thread is executed. 
# thread.join()  

# These lines are executed by main thread
print("hello-1 from main-thread")
print("hello-2 from main-thread")

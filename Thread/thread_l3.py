# Creating Multiple threads
# Also learn the dependency of a thread on other thread
# Dependency: Lets's say thread1 returns weather data from api, and thread2 is going to 
# need that data for some calculation 
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, target, args=()):
        super(MyThread, self).__init__(target=target, args=args)
        self._result = None

    def run(self):
        # The run method is called when the thread is started
        self._result = self._target(*self._args)

    def get_result(self):
        return self._result

def my_function():
    # Simulate some work and return a result
    time.sleep(3)
    return "Hello from the thread!"

# Create a thread with the target function and its arguments
my_thread = MyThread(target=my_function)

# Start the thread
my_thread.start()

# Wait for the thread to finish 
# this can be used to block the further executuion untill this thread finishes its work
my_thread.join()

# Get the result from the thread
result = my_thread.get_result()

print("Result from the thread:", result)

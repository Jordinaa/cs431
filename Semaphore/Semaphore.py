import threading

class Semaphore:
    def __init__(self, inital_value) -> None:
        self.lock = threading.Condition(threading.Lock())
        self.value = inital_value

    def P(self):                
        # context manager automatically aquire and release the lock
        with self.lock:
            # if semaphore is 0 or less, wait until it becomes positive
            while self.value <= 0: 
                # while value is less than 0 (not running) it will lock the process
                self.lock.wait()
                print("waiting")
            # decrease the semaphore value
            self.value -= 1

    def V(self):
        with self.lock:
            # increase the semaphore value
            self.value += 1
            # notify the waiting threads
            self.lock.notify()
            print("notified")
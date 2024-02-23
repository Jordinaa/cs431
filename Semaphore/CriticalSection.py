from Semaphore import Semaphore # import the semaphore class
import time

class CriticalSection:
    def __init__(self) -> None:
        self.semaphore = Semaphore(1) # create a semaphore instance with an initial value of 1

    def critical_section(self, p):
        # entry section
        self.semaphore.P()

        # CS
        print(f"Process {p} entered CS")
        time.sleep(5)

        # exit section
        print(f"Process {p} exiting CS")
        self.semaphore.V()
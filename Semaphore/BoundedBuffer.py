from Semaphore import Semaphore

class BoundedBuffer:
    def __init__(self, size) -> None:
        self.semaphore_empty = Semaphore(size)
        self.semaphore_full = Semaphore(0)
        self.buffer = []
        # self.buffer = [None] * size

    def produce(self, item):
        # wait until there's space in the buffer
        self.semaphore_empty.P()

        # produce the item and add it to the buffer
        self.buffer.append(item)
        print(f"Produced item {item}")

        # signal that a slot is full
        self.semaphore_full.V()

    def consume(self):
        # wait until there's at least one item in the buffer
        self.semaphore_full.P()

        # consume the item and remove it from the buffer
        item = self.buffer.pop(0)
        print(f"Consumed item {item}")

        # signal that a slot is empty
        self.semaphore_empty.V()
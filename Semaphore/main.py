import threading
from CriticalSection import CriticalSection
from BoundedBuffer import BoundedBuffer

def test_critical_section():
    cs = CriticalSection() # create a CS instance
    threads = [] # create threads to simulate access to the CS 

    for i in range(5):
        t = threading.Thread(target=cs.critical_section, args=(i,))
        threads.append(t)
        t.start()

    # wait for all threads to finish
    for t in threads:
        t.join()

def test_bounded_buffer():
    # create BoundedBuffer instance with buffer size 5
    bb = BoundedBuffer(5)

    # create produced and consumer threads
    producer_thread = threading.Thread(target=lambda: [bb.produce(i) for i in range(10)])
    consumer_thread = threading.Thread(target=lambda: [bb.consume() for _ in range(10)])

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
                                       
# test_critical_section()
test_bounded_buffer()
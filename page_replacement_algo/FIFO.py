# Author: Jordan Taranto
# CS431 
# references: 
# https://stackoverflow.com/questions/74307591/is-there-a-more-elegant-way-of-finding-minimum-in-array-in-this-case
    # used this for float('inf') to find min value in array which is phenonemnal and fairly fast

# These algos are pretty stratight forward since we have been doing FIFO all semester just different size matrices etc
def fifo_page_replacement(reference_string, num_frames):
    print("\nQ2 FIFO PAGE REPLACEMENT ALGO:")
    frames = [-1] * num_frames
    page_faults = 0
    queue = []

    # simulate page access 
    for page in reference_string:
        if page not in frames:
            if -1 in frames:
                frames[frames.index(-1)] = page
            else:
                # pop element in queue and put new page
                frames[queue.pop(0)] = page
            queue.append(frames.index(page))
            page_faults += 1
            print(f"page fault: Page {page} loaded into frames: {frames}")
        else:
            print(f"page {page} already in frames: {frames}")

    print(f"Total page faults: {page_faults}\n")


# Author: Jordan Taranto
# CS431 

def lru_page_replacement(reference_string, num_frames):
    print("\nQ3 LRU PAGE REPLACEMENT ALGO:")
    # init frames with -1 being the indicator that they are empty frames
    frames = [-1] * num_frames
    page_faults = 0
    # used a dict here to keep track of the last time a page was used
    last_used = {}

    # simulate page replacement 
    for i, page in enumerate(reference_string):
        # check if frame is in page 
        if page not in frames:
            # increment page fault because page isn't present in frame
            page_faults += 1
            # fill first empy frame if exists
            if -1 in frames:
                frames[frames.index(-1)] = page
            # find leaset recentl used page and replace LRU page with current page
            else:
                lru_page = min(last_used, key=last_used.get)
                # check if lru page exists otherwise errors out 
                if lru_page in frames: 
                    frames[frames.index(lru_page)] = page
                else:
                    frames[0] = page
        # if no page fault print status of frame
        else:
            print(f"Page {page} already in frames: {frames}")
        last_used[page] = i

    print(f"Total page faults: {page_faults}\n")
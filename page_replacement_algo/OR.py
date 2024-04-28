# Author: Jordan Taranto
# CS431 
# references: 
# https://stackoverflow.com/questions/74307591/is-there-a-more-elegant-way-of-finding-minimum-in-array-in-this-case
    # used this for float('inf') to find min value in array which is phenonemnal and fairly fast

def optimal_page_replacement(reference_string, num_frames):
    print("\nQ1 OPTIMAL PAGE REPLACEMENT ALGO:")
    frames = [-1] * num_frames
    page_faults = 0

    # simulate page access
    for i, page in enumerate(reference_string):
        if page not in frames:
            if -1 in frames:
                frames[frames.index(-1)] = page
            else:
                # references float inf above 
                next_use = [float('inf')] * num_frames
                for j in range(num_frames):
                    if frames[j] not in reference_string[i+1:]:
                        next_use[j] = float('inf')
                    else:
                        # find the next use of the page
                        next_use[j] = reference_string[i+1:].index(frames[j])
                frames[next_use.index(max(next_use))] = page
            page_faults += 1
            print(f"page fault: Page {page} loaded into frames: {frames}")
        else:
            print(f"page {page} already in frames: {frames}")

    print(f"Total page faults: {page_faults}\n")

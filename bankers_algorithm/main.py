# Author(s): Jordan Taranto

from BankersAlgorithm import BankersAlgorithm

# init the data from the image in the assignment
# found the same data from the image in the assignment to use at geeks to geeks, cleaned it up a bit 
# https://www.geeksforgeeks.org/bankers-algorithm-in-operating-system/
processes = [0, 1, 2, 3, 4]
resources = [10, 5, 7]

allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2],
]

max_demand = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3],
]

# create instance of BankersAlgorithm
bankers_algo = BankersAlgorithm(processes, resources, max_demand, allocation)

# display the sequence 
bankers_algo.display_safe_sequence()

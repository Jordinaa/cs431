# Author: Jordan Taranto
# CS431 

from OR import optimal_page_replacement
from FIFO import fifo_page_replacement
from LRU import lru_page_replacement

REFERENCE_STRING = [0, 1, 4, 0, 2, 3, 0, 1, 0, 2, 3, 4, 2, 3]
NUM_FRAMES = 4

# Question 1 Optimal algorithm
optimal_page_replacement(REFERENCE_STRING, NUM_FRAMES)
# Question 2 FIFO algorithm
fifo_page_replacement(REFERENCE_STRING, NUM_FRAMES)
# Question 3 LRU algorithm
lru_page_replacement(REFERENCE_STRING, NUM_FRAMES)
# Question 4 Ranking of page algorithm performance 
print("Q4 Ranking of algos")
print("1. Optimal Page Replacement Algorithm")
print("2. LRU Page Replacement Algorithm")
print("3. FIFO Page Replacement Algorithm")
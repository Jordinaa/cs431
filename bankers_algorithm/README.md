Author: Jordan Taranto
Assignment 2
CS431

# Section 1: Code Implementation 
#### main.py
![main.py](/bankers_algorithm/assets/img/main.png)

#### BankersAlgorithm.py
![main.py](/bankers_algorithm/assets/img/BankersAlgo.png)

# Section 2: Outputs
#### Output of sequence 
![Output](/bankers_algorithm/assets/img/output.png)
# Section 3: Implementation Details

#### Thought process: 
The first part was converting the data we will be using into the necessary matrixes. Fortunately I found a [GeeksForGeeks](https://www.geeksforgeeks.org/bankers-algorithm-in-operating-system/) post with the same data so I copied that over and cleaned it up. 
#### Challenges: 
This was much more straightforward then the scheduling algorithm. The first assignment helped get me in the mindset for how to conceptualize operating systems and writing code moving forward. So didn't really have many challenges. 
#### Insights: 
Provided a good foundation for avoiding deadlocks. I noticed that it doesn't prioritize processes. So moving forward I think that would be very beneficial, based off of metrics like minimum waiting time, FIFO, etc. just like what we talked about in class with the restaurant example. 

# References: 
- https://ray.so/#code=&title=&padding=16&theme=breeze
- https://www.geeksforgeeks.org/bankers-algorithm-in-operating-system/
- https://dev.to/ryanangry07/bankers-algorithm-deadlock-avoidance-5ejj
- https://stackoverflow.com/questions/63796782/bankers-algorithm-can-i-allocate-resources-to-a-process-if-work-is-less-than

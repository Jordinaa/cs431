# Jordan Taranto
#### Homework 1
#### CS431
### Github: 
# Section 1 - Code Implementation
``` main.py
from Input import ProcessCSV
from Scheduling import Scheduling


# Global variables change input file name here
FILE_PATH = "homework-1/test/input.csv"

if __name__ == "__main__":
	# read in CSV file
	data = ProcessCSV(FILE_PATH)
	# get list of processes
	processes = data.return_processes()
	# print out each process
	data.print_processes()
	
	# shortest job first
	sjf = Scheduling(processes)
	sjf_att = sjf.shortest_job_first()
	print(f"Average turnaround time: {sjf_att}")
	print(sjf.sjf_turnaround_time)
	
	# shortest remaining time first
	srt = Scheduling(processes)
	srt_att = srt.shortest_remaining_time()
	print(f"Average turnaround time: {srt_att}")
	print(srt.srt_turnaround_time)
```

# Section 2 - Outputs

# Section 3 - Implementation Details
### Challenges faced:
- 
# Thought process
- Input class 
	- which takes file path and any number of inputs and automatically assigns it to a list of lists
	- settled on just one class for simplicity and assignments sake
- process class
	- can be called inside of the input class making a list of objects 
		- tried this but inheritance vs composition but wasn't sure can check git repo for this implementation 
	- takes list of lists allowing for more detailed analysis on processes
- CLI GUI class
	- uses dashes fixed on at the top for x amount of time
	- below this is shows how and which process ran when 
# Tasks:
- [ ] Structure
	- [ ] main.py - for testing and simulating processes
	- [ ] Input.py - process the input file (CSV only) 
	- [ ] Scheduling.py- scheduling algorithms 

- [ ] Class that processes CSV file 
	- [x] Class attributes
		- [x] process
		- [x] arrival time
		- [x] cpu time
		- [x] priority

- [ ] Shortest Job First (SJF)
	- [ ] function
		- [ ] function runs loop finished goes onto next process
	- [ ] Computer average turn around time
	- [ ] non preemptive

- [ ] Shortest Remaining Time (SRT)
	- [ ] SRT Function 
		- [ ] process is running and when next one joins it uses a check function 
	- [ ] Check function 
	- [ ] Computer average turn around time
	- [ ] preemptive version of SJF

- [ ] Final Report
	- [ ] screenshots of output

# References
- Reading CSVs and other data my github repo
	- https://github.com/Jordinaa/supervisor/blob/master/scripts/fesupervisor.py

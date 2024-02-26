# Jordan Taranto
#### Homework 1
#### CS431
### Github: https://github.com/Jordinaa/cs431/tree/main/homework-1
# Section 1 - Code Implementation
### Main.py
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
### Input.py
```Input.py
import csv 
# reference is from an older project of mine
# https://github.com/Jordinaa/supervisor/blob/master/scripts/fesupervisor.py

class ProcessCSV: 
    def __init__(self, file_path):
        self.file_path = file_path
        self.processes_list = []
        self.read_input()

    # input CSV file read data and assign to class attributes and append to list of processes
    def read_input(self):
        self.csv_file = open(self.file_path, 'r')
        with self.csv_file as file:
            reader = csv.reader(file)
            # skips the header row in CSV
            next(reader)
            for row in reader:
                # read each row in the csv and assign to class attributes
                self.process_name = row[0]
                self.arrival_time = int(row[1])
                self.burst_time = int(row[2])
                self.priority = int(row[3])
                # appends data from csv to the list of processes (orginally had a process object but changed to list for simplicity)
                self.processes_list.append([self.process_name, self.arrival_time, self.burst_time, self.priority])
        # close the csv file 
        self.csv_file.close()

    # returns the list of processes
    def return_processes(self):
        return self.processes_list

    # prints the list of processes (for troubleshooting)
    def print_processes(self):
        for process in self.processes_list:
            print(f"Name: {process[0]}\nArrival Time: {process[1]}\nBurst Time: {process[2]}\nPriority: {process[3]}\n")
```
### Scheduling.py
```Scheduling.py
class Scheduling:
    def __init__(self, list_of_processes):
        self.processes = list_of_processes
        self.process_length = len(self.processes)

    def shortest_job_first(self):
        current_time = 0
        total_turnaround_time = 0
        # sort processes by arrival time first 
        # https://stackoverflow.com/questions/4174941/how-to-sort-a-list-of-lists-by-a-specific-index-of-the-inner-list
        processes = sorted(self.processes, key=lambda arrival_time: arrival_time[1])

        while processes:
            # get the next available process based on current time (0 for first loop)
            available_processes = [process for process in processes if process[1] <= current_time]
            # if no process available at current time increment current time
            if not available_processes:
                current_time += 1
                continue
            
            # now sort the available processes by burst time
            # used min since this simply grabs the process with the shortest burst time (the loop above sorts the whole list by arrival time)
            process_queue = min(available_processes, key=lambda burst_time: burst_time[2])

            # remove from the process from the list
            processes.remove(process_queue)
            arrival_time = process_queue[1]
            burst_time = process_queue[2]
            completion_time = current_time + burst_time
            turnaround_time = completion_time - arrival_time
            total_turnaround_time += turnaround_time
            print(f"Process: {process_queue[0]} Arrival Time: {arrival_time} Burst Time: {burst_time} Completion Time: {completion_time} Turnaround Time: {turnaround_time}")

            # adds to current time since burst time is the time it takes to complete the process 
            current_time += burst_time

        # calculate the average turnaround time 
        average_turnaround_time = total_turnaround_time / self.process_length
        return average_turnaround_time

    def shortest_remaining_time(self):
        # Same as above so copied contents from SJT function and modified it
        current_time = 0
        total_turnaround_time = 0
        processes = sorted(self.processes, key=lambda arrival_time: arrival_time[1])
    
        while processes:
            # almost the same as above but I have another condition where it is comparing the burst time of the process
            available_processes = [process for process in processes if process[1] <= current_time and process[2] > 0]
            if not available_processes:
                current_time += 1
                continue
            process_queue = min(available_processes, key=lambda burst_time: burst_time[2])

            # subtracting burst time directly from the process list not recommended (i would have a process class)
            # this is the preemptive part which helps determine shortest remaining time 
            process_queue[2] -= 1
            if process_queue[2] == 0:
                processes.remove(process_queue)
                arrival_time = process_queue[1]
                completion_time = current_time + 1
                turnaround_time = completion_time - arrival_time
                total_turnaround_time += turnaround_time
                print(f"Process: {process_queue[0]} Arrival Time: {arrival_time} Completion Time: {completion_time} Turnaround Time: {turnaround_time}")
            
            # increment current time
            current_time += 1
    
        average_turnaround_time = total_turnaround_time / self.process_length
        return average_turnaround_time
```
# Section 2 - Outputs
###  Inputs.py
Here is my first file `Inputs.py` with class `ProcessCSV` which is responsible for importing the CSV file.

![inputs](/assets/img/input.png)

### Scheduling.py
Here is my second file is `Scheduling.py` with class `Scheduling` this includes **shortest job first** output 

![inputs](/assets/img/sjf_output.png)

**shortest time remaining** output

![inputs](/assets/img/srt_output.png)

# Section 3 - Implementation Details
### Thought Process:
My thought process going into this was what are my inputs and how am I going to process them. 

asdf [inputs](/assets/img/srt_output.png)

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


# References
- Reading CSVs and other data my github repo
	- https://github.com/Jordinaa/supervisor/blob/master/scripts/fesupervisor.py

# Author: Jordan Taranto

class Scheduling:
    def __init__(self, list_of_processes):
        self.processes = list_of_processes

    # shorter the required CPU time the higher the priority
    # arbitration rule: if same CPU time then selects based on arrival times
    # non-preemptive
    def shortest_job_first(self):
        # calculate turnaround time
        # time start at 0 these are outside the for loop to keep track of time moving forward
        current_time = 0
        total_turnaround_time = 0

        # https://stackoverflow.com/questions/4174941/how-to-sort-a-list-of-lists-by-a-specific-index-of-the-inner-list
        # sorted_burst_time = sorted(self.processes, key=lambda cpu_time: cpu_time[2])


        # sort by fasest process burst time 
        # https://stackoverflow.com/questions/4174941/how-to-sort-a-list-of-lists-by-a-specific-index-of-the-inner-list

        sorted_burst_time = sorted(self.processes, key=lambda cpu_time: cpu_time[2])
        # iterate through sorted process list
        for process in sorted_burst_time:
            arrival_time = process[1]
            burst_time = process[2]

            # calculate completion time which is the start time for the first process
            # add to it has the algo completes 
            completion_time = current_time + burst_time
            # difference between completion time and arrival time
            turnaround_time = completion_time - arrival_time
            # accumulate total turnaround time
            total_turnaround_time += turnaround_time
            # since SJF we add to it immediatly since it is non-preemptive
            current_time += burst_time
        # average turnaround time is the sum of turnaround time divded by number of processes
        average_turnaround_time = total_turnaround_time / len(sorted_burst_time)
        return average_turnaround_time

    
    # shorter the CPU time the remaining CPU time the higher the priority 
    # arbitration rule: if same remaining time requirement selects based on arrival times
    # preemptive 
    def shortest_remaining_time(self):
        pass

    # time between arrival and departure and is the sum of total CPU time and waiting time
    # TAT = waiting time + CPU Burst time
    # Average TAT = sum of all TAT / mean of n individual turnaround times
    def calculate_turnaround_time(self):
        pass


        # this is a callback function that can update attributes of the class to be processed 
    # def callback(self):
    #     self.process_name = self.process_name
    #     self.arrival_time = self.arrival_time
    #     self.burst_time = self.burst_time
    #     self.priority = self.priority

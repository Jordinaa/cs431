# Author: Jordan Taranto

class Scheduling:
    def __init__(self, list_of_processes):
        self.processes = list_of_processes

    def sort_processes(self, priority):
        pass

    def scheduler(self):
        pass

    # shorter the required CPU time the higher the priority
    # arbitration rule: if same CPU time then selects based on arrival times
    # non-preemptive
    def shortest_job_first(self):
        pass
    
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
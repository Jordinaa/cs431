# Author: Jordan Taranto

class Scheduling:
    def __init__(self, list_of_processes):
        self.processes = list_of_processes
        self.process_length = len(self.processes)

    def shortest_job_first(self):
        # init variables for average turnaround time
        current_time = 0
        total_turnaround_time = 0
        # sort processes by arrival time first 
        # https://stackoverflow.com/questions/4174941/how-to-sort-a-list-of-lists-by-a-specific-index-of-the-inner-list
        processes = sorted(self.processes, key=lambda arrival_time: arrival_time[1])

        while processes:
            # get the next available process based on current time (0 for first loop)
            available_processes = [process for process in processes if process[1] <= current_time]
            if not available_processes:
                # if no process available at current time increment current time
                current_time += 1
                continue
            
            # now sort the available processes by burst time
            # used min since this simply grabs the process with the shortest burst time (the loop above sorts the whole list)
            process_queue = min(available_processes, key=lambda burst_time: burst_time[2])
            print(process_queue)
            # remove from the list of processes so the while loop can end
            processes.remove(process_queue)
            arrival_time = process_queue[1]
            burst_time = process_queue[2]
            completion_time = current_time + burst_time
            turnaround_time = completion_time - arrival_time
            total_turnaround_time += turnaround_time
            # move current time to the process that was just completed time
            current_time += burst_time
        # calculate the average turnaround time 
        average_turnaround_time = total_turnaround_time / self.process_length
        return average_turnaround_time

    
    # shorter the CPU time the remaining CPU time the higher the priority 
    # arbitration rule: if same remaining time requirement selects based on arrival times
    # preemptive 
    def shortest_remaining_time(self):
        pass

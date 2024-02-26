# Author: Jordan Taranto

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

class Scheduling1:
    def __init__(self, list_of_processes):
        self.processes = list_of_processes
        self.process_length = len(self.processes)

        # Assuming each process is a list with [process name, arrival time, burst time, priority]
        # Add another element to each process for tracking remaining burst time
        for process in self.processes:
            process.append(process[2])  # Initially, remaining burst time equals the burst time

    def shortest_job_first(self):
        # init variables for TAT and ATT
        current_time = 0
        total_turnaround_time = 0
        
        # sort processes list by arrival time first 
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

    def shortest_remaining_time(self):
        # Very similiar to SJF copied code and modified
        current_time = 0
        total_turnaround_time = 0

        processes = sorted(self.processes, key=lambda x: x[1])  # Sort by arrival time initially

        while completed_processes < len(processes):
            # Filter processes that have arrived by current time
            available_processes = [p for p in processes if p[1] <= current_time and p[4] > 0]

            if not available_processes:
                current_time += 1
                continue

            # Among the available processes, choose the one with the shortest remaining burst time
            next_process = min(available_processes, key=lambda x: x[4])
            next_process[4] -= 1  # Decrement remaining time by 1 unit

            # Check if the process is completed
            if next_process[4] == 0:
                completed_processes += 1
                completion_time = current_time + 1  # +1 because we just completed a unit of time
                turnaround_time = completion_time - next_process[1]
                total_turnaround_time += turnaround_time

            current_time += 1  # Increment time

        average_turnaround_time = total_turnaround_time / len(processes)
        print(average_turnaround_time)
        return average_turnaround_time

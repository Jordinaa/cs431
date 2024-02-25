# Author: Jordan Taranto
import csv 

class ProcessCSV: 
    def __init__(self, file_path):
        self.file_path = file_path
        self.processes = []
        self.read_input()

    # reads the input data and appends process objects to the processes list which can be called 
    def read_input(self):
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            # skips the header row in CSV
            # future work will use pandas to read CSV (lets goooo dataframes!)
            next(reader)
            for row in reader:
                # read the csv rows
                process_name = row[0]
                arrival_time = int(row[1])
                burst_time = int(row[2])
                priority = int(row[3])
                # appends the Process object to the processes list 
                # not a good way to do this inheritance vs composition 
                self.processes.append(Process(process_name, arrival_time, burst_time, priority))

    def return_process(self):
        return self.processes

# For future work, have all sorts of detailed information you can print out about the process
class Process:
    def __init__(self, process_name, arrival_time, burst_time, priority):
        self.process = process_name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority

    def print_Process_Information(self):
        print(f"")

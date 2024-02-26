# Author: Jordan Taranto
import csv 
# reference is from an older project of mine
# https://github.com/Jordinaa/supervisor/blob/master/scripts/fesupervisor.py
class ProcessCSV: 
    def __init__(self, file_path):
        self.file_path = file_path
        self.processes_list = []
        self.read_input()

        self.process_name = self.process_name
        self.arrival_time = self.arrival_time
        self.burst_time = self.burst_time
        self.priority = self.priority

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
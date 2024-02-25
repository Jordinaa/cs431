# Author: Jordan Taranto
# Test file for testing different things etc. 
from Input import ProcessCSV
from Scheduling import Scheduling

# Global variables change input file name here
FILE = "homework-1/test/input.csv"

if __name__ == "__main__":
    # read in CSV file 
    data = ProcessCSV(FILE)
    # get list of processes
    processes = data.return_processes()
    # print out each processes
    data.print_processes()

    # give scheduling class the list of processes to utilize 
    test = Scheduling(processes)
    average_turnaround_time = test.shortest_job_first()
    print(average_turnaround_time)
    

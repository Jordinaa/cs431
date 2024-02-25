# Author: Jordan Taranto

from Input import ProcessCSV

# Global variables change input file name here
FILE = "homework-1/test/input.csv"


if __name__ == "__main__":
    # read in CSV file 
    data = ProcessCSV(FILE)
    processes = data.return_process()
    # print out the processes
    for process in processes:
        print(process.process, process.arrival_time, process.burst_time, process.priority)
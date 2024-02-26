# Author: Jordan Taranto
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
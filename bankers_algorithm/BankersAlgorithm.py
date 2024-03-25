# Author(s): Jordan Taranto

# References: 
# https://www.geeksforgeeks.org/bankers-algorithm-in-operating-system/
# https://dev.to/ryanangry07/bankers-algorithm-deadlock-avoidance-5ejj
# https://stackoverflow.com/questions/63796782/bankers-algorithm-can-i-allocate-resources-to-a-process-if-work-is-less-than

class BankersAlgorithm:
    def __init__(self, processes, resources, max_demand, allocation):
        # initalize the data which will be initalized into main.py 
        self.processes = processes
        self.resources = resources
        self.max_demand = max_demand
        self.allocation = allocation
        # when initialized, calculate the resources available and the need for each process
        self.resources_available = self.calculate_available_resources()
        self.need = self.calculate_need()

    def calculate_available_resources(self):
        # find the available resources for each process
        # this initalizes the matrix with 0
        available = [0 for _ in range(len(self.resources))]
        # iterate over each process
        for i in range(len(self.resources)):
            available[i] = self.resources[i]
            # subtract allocated resources from available resources
            for j in range(len(self.processes)):
                available[i] -= self.allocation[j][i]

        return available

    def calculate_need(self):
        # find the need matrix for each process
        # same idea has above 
        # this initalizes the matrix with 0
        need = [[0 for _ in range(len(self.resources))] for _ in range(len(self.processes))]
        # iterate over each process
        for i in range(len(self.processes)):
            # then iterate over each resource
            for j in range(len(self.resources)):
                # calculate the need for each process 
                need[i][j] = self.max_demand[i][j] - self.allocation[i][j]
        return need

    def is_safe(self):
        work = self.resources_available[:]
        finish = [False] * len(self.processes)
        safe_sequence = []
        # this was a pain lol 
        while len(safe_sequence) < len(self.processes):
            found = False
            for i in range(len(self.processes)):
                if not finish[i] and all(self.need[i][j] <= work[j] for j in range(len(self.resources))):
                    for j in range(len(self.resources)):
                        work[j] += self.allocation[i][j]
                    safe_sequence.append(i)
                    finish[i] = True
                    found = True
            if not found:
                return (False, [])
        return (True, safe_sequence)

    def display_safe_sequence(self):
        # displays the safe sequence for printing to the terminal 
        is_safe, sequence = self.is_safe()
        if is_safe:
            print("Safe sequence is: ", end="")
            print(*[f'P{seq}' for seq in sequence])
        else:
            print("The system is not safe. I repeat, the system is not safe")


# author: Jordan Taranto
import matplotlib.pyplot as plt
import networkx as nx

# RAG allocation graph class implementation 
class RAG:
    def __init__(self, processes_list, resources_list):
        # init an empty directed graph
        self.graph = nx.DiGraph()

        # store list of process and resources
        self.processes_list = processes_list
        self.resources_list = resources_list

    def add_edge(self, process, resource):
        # add edge from process to resource
        self.graph.add_edge(process, resource)
    
    def visualize(self):
        # generate layout positions for the processes
        layout = nx.spring_layout(self.graph)

        # draw the graph
        nx.draw(self.graph, layout, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, font_weight='bold')

    def detect_deadlock(self):
        # find cycles in the graph
        cycles = list(nx.simple_cycles(self.graph))
        
        # check if cycles are found
        if cycles:
            print('Deadlock detected')
            print('Processes involved in the deadlock:', cycles)
        else:
            print('No deadlocks detected')

    plt.title('Resource Allocation Graph')
    plt.show()


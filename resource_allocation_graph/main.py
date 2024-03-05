from RAG import RAG

processes = ['P1', 'P2', 'P3', 'P4']
resources = ['R1', 'R2', 'R3', 'R4']

rag = RAG(processes, resources)

# Graph 1 - no deadlock
rag.add_edge('P1', 'R1')
rag.add_edge('R2', 'P1')
rag.add_edge('R2', 'P2')
rag.add_edge('R1', 'P2')
rag.add_edge('P2', 'R3')
rag.add_edge('R3', 'P3')

rag.visualize()
rag.detect_deadlock()

# Graph 2 - deadlock 
rag.add_edge('P1', 'R1')
rag.add_edge('R2', 'P1')
rag.add_edge('R2', 'P2')
rag.add_edge('R1', 'P2')
rag.add_edge('P2', 'R3')
rag.add_edge('R3', 'P3')
rag.add_edge('P3', 'R2')

rag.visualize()
rag.detect_deadlock()

# Graph 3 - no deadlock
rag.add_edge('P1', 'R1')
rag.add_edge('R1', 'P2')
rag.add_edge('R1', 'P3')
rag.add_edge('P3', 'R2')
rag.add_edge('R2', 'P1')
rag.add_edge('R2', 'P4')

rag.visualize()
rag.detect_deadlock()
## Fabonacci numbers
#prev2 = 0
#prev1 = 1

#print(prev2)
#print(prev1)
#for fibo in range(18):
#    newFibo = prev1 + prev2
#    print(newFibo)
#    prev2 = prev1
#    prev1 = newFibo

#print(0)
#print(1)
#count = 2

#def fibonacci(prev1, prev2):
#    global count
#    if count <= 19:
#        newFibo = prev1 + prev2
#        print(newFibo)
#        prev2 = prev1
#        prev1 = newFibo
#        count += 1
#        fibonacci(prev1, prev2)
#    else:
#        return
#fibonacci(1,0)        


## DSA Arrays

#my_array = [7, 12, 9, 4, 11]
#minVal = my_array[0]

#for i in my_array:
#    if i < minVal:
#        minVal = i
        
#print('Lowest value: ', minVal)        

class GraphEdgeList:
    def __init__(self):
        self.edges = []

    def add_edge(self, u, v, weight=1):
        self.edges.append((u, v, weight))

    def display(self):
        for edge in self.edges:
            print(f"Edge from {edge[0]} to {edge[1]} with weight {edge[2]}")

# Tạo đồ thị
graph = GraphEdgeList()
graph.add_edge(0, 1, 4)
graph.add_edge(0, 2, 6)
graph.add_edge(1, 2, 2)
graph.add_edge(2, 3, 3)
graph.display()

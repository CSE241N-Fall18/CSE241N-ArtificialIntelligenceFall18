''' class Graph defines the bfs and dfs functions that operate on the graph  '''

class Graph:
    
    def __init__(self, adj):
        n = len(adj)
        self.graph = dict()
        for i in range(n):
            temp = []
            for j in range(n):
                if adj[i][j]:
                    temp.append(j)
            self.graph[i] = set(temp)

    def bfs_paths(self, start, goal):
    '''
    Generate and return any path from start to goal using breadth-first search
    Input : start node, goal node
    Output : list of nodes from to be traversed to reach from start to goal(the first node in this list will be the start node and the last node will be the goal node)
    '''
    #BEGIN YOUR CODE HERE
        
    
    #END YOUR CODE HERE


 
    def dfs_paths(self, start, goal):
    '''
    Generate and return any path from start to goal using depth-first search
    Input : start node, goal node
    Output : list of nodes from to be traversed to reach from start to goal(the first node in this list will be the start node and the last node will be the goal node)
    '''
    #BEGIN YOUR CODE HERE


    #END YOUR CODE HERE

''' class Graph defines the bfs and dfs functions that operate on the graph  '''

class Graph:
    
    def __init__(self, adj):
        n = len(adj)
        self.graph = dict()
        self.visited = []
        self.order_bfs = []
        self.order_dfs = []

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
        n = len(self.graph)
        self.visited = [False]*n

        self.visited[start] = True

        q = []
        q.append(start)

        while len(q):

            v = q.pop(0)
            self.order_bfs.append(v)

            for i in self.graph[v]:
                if i == goal :
                    break
                if self.visited[i] == False:
                    self.visited[i] = True
                    q.append(i)

        self.order_bfs.append(goal)
        return self.order_bfs
    #END YOUR CODE HERE






    def dfs_paths(self, start, goal):
        '''
    Generate and return any path from start to goal using depth-first search
    Input : start node, goal node
    Output : list of nodes from to be traversed to reach from start to goal(the first node in this list will be the start node and the last node will be the goal node)
    '''
    #BEGIN YOUR CODE HERE
        n = len(self.graph)
        self.visited = [False]*n
        self.visited[start] = True
        q = []
        q.append(start)

        while len(q):

            v = q.pop()
            self.order_dfs.append(v)

            for i in self.graph[v]:
                if i == goal:
                    break
                if self.visited[i] == False:
                    self.visited[i] = True
                    q.append(i)

        self.order_dfs.append(goal)
        return self.order_dfs

    #END YOUR CODE HERE
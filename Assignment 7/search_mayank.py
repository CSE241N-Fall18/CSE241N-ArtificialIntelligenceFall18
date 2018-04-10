"""
search.py: Search algorithms on grid.
"""
import heapq as hq

def finans

def heuristic(a, b):
    """
    Calculate the heuristic distance between two points.

    For a grid with only up/down/left/right movements, a
    good heuristic is manhattan distance.
    """

    # BEGIN HERE #

    return abs(a[0]-b[0]) + abs(a[1]- b[1])

    # END HERE #


def searchHillClimbing(graph, start, goal):
    """
    Perform hill climbing search on the graph.

    Find the path from start to goal.

    @graph: The graph to search on.
    @start: Start state.
    @goal: Goal state.

    returns: A dictionary which has the information of the path taken.
             Ex. if your path contains and edge from A to B, then in
             that dictionary, d[B] = A. This means that by checking
             d[goal], we obtain the node just before the goal and so on.

             We have called this dictionary, the "came_from" dictionary.
    """

    # Initialise the came_from dictionary
    came_from = {}
    came_from[start] = None

    # BEGIN HERE #

    stack = []
    stack.append(start)
    vis = {}
    vis[start] = 1
    dist[start]= -1
    while len(stack) !=0 :
        node = stack[len(stack)-1]
        stack.pop()

        edges = []
        for point in graph.neighboursOf(node):
            edges.append((heuristic(point,goal),point))
        edges.sort(reverse=True)
        
        for _,point in edges:
            if point not in vis:    
                stack.append(point)
                dist[point] = node
                vis[point] =1

    point = goal
    while point != -1:
        try:
            came_from[point] = dist[point]
            point = dist[point]
        except:
            point=-1


    # END HERE #

    return came_from


def searchBestFirst(graph, start, goal):
    """
    Perform best first search on the graph.

    Find the path from start to goal.

    @graph: The graph to search on.
    @start: Start state.
    @goal: Goal state.

    returns: A dictionary which has the information of the path taken.
             Ex. if your path contains and edge from A to B, then in
             that dictionary, d[B] = A. This means that by checking
             d[goal], we obtain the node just before the goal and so on.

             We have called this dictionary, the "came_from" dictionary.
    """


    # Initialise the came_from dictionary
    came_from = {}
    came_from[start] = None


    # BEGIN HERE #

    pq = []
    hq.heappush(pq,(heuristic(start,goal),start))
    vis = {}
    vis[start] = 1
    parent = {start:-1}
    while len(pq) !=0 :
        node = hq.heappop(pq)[1]

        for point in graph.neighboursOf(node):
            if point not in vis:
                hq.heappush(pq,(heuristic(point,goal),point))
                parent[point] = node
                vis[point] =1

    node = goal
    while node != -1:
        try:
            came_from[node] = parent[node]
            node = parent[node]
        except:
            node = -1
    # print(came_from)

    # END HERE #

    return came_from



def searchBeam(graph, start, goal, beam_length=3):
    """
    Perform beam search on the graph.

    Find the path from start to goal.

    @graph: The graph to search on.
    @start: Start state.
    @goal: Goal state.

    returns: A dictionary which has the information of the path taken.
             Ex. if your path contains and edge from A to B, then in
             that dictionary, d[B] = A. This means that by checking
             d[goal], we obtain the node just before the goal and so on.

             We have called this dictionary, the "came_from" dictionary.
    """

    # Initialise the came_from dictionary
    came_from = {}
    came_from[start] = None

    # BEGIN HERE #

    q = []
    q.append(start)
    vis = {}
    vis[start] = 1
    parent = {}
    parent[start] = -1
    while len(q)!=0:
        node = q[0]
        del q[0]
        edges = []
        for point in graph.neighboursOf(node):
            if point not in vis:    
                edges.append((heuristic(point,goal),point))
        edges.sort()
        edges = edges[:beam_length]
        for _,point in edges:
            q.append(point)
            vis[point] = 1
            parent[point] = node

    node = goal
    while node != -1:
        try:
            came_from[node] = parent[node]
            node = parent[node]
        except:
            node = -1

    # END HERE #

    return came_from


def searchAStar(graph, start, goal):
    """
    Perform A* search on the graph.

    Find the path from start to goal.

    @graph: The graph to search on.
    @start: Start state.
    @goal: Goal state.

    returns: A dictionary which has the information of the path taken.
             Ex. if your path contains and edge from A to B, then in
             that dictionary, d[B] = A. This means that by checking
             d[goal], we obtain the node just before the goal and so on.

             We have called this dictionary, the "came_from" dictionary.
    """

    # Initialise the came_from dictionary
    came_from = {}
    came_from[start] = None

    # BEGIN HERE #
    edges_length = 1
    dist = {start:0}

    pq = []
    hq.heappush(pq,(heuristic(start,goal),start))
    vis = {}
    parent = {start:-1}
    vis[start] = 1
    while len(pq) !=0 :
        node = hq.heappop(pq)[1]

        for point in graph.neighboursOf(node):
            if point not in vis:
                hq.heappush(pq,(heuristic(point,goal) + edges_length + dist[node],point))
                parent[point] = node
                dist[point] = dist[node] + edges_length
                vis[point] =1

    node = goal
    while node != -1:
        try:
            came_from[node] = parent[node]
            node = parent[node]
        except:
            node = -1
    # END HERE #

    return came_from


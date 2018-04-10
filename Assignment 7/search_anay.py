"""
search.py: Search algorithms on grid.
"""
import heapq as heap

def heuristic(a, b):
    """
    Calculate the heuristic distance between two points.

    For a grid with only up/down/left/right movements, a
    good heuristic is manhattan distance.
    """

    # BEGIN HERE #

    return abs(a[0]-b[0])+abs(a[1]-b[1])

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

    visited = []
    s = []
    s.append(start)
    visited.append(start)
    dist={}
    dist[start]=-1
    v = start
    while ((s) and v != goal):
        if(v == start):
           v= s.pop()
        neighbor=[]
        for i in graph.neighboursOf(v):
            if i not in visited:
                neighbor.append((heuristic(i,goal),i))
        neighbor.sort()
        neighbor.reverse()
        for i,j in neighbor:
            s.append(j)
            dist[j]=v
            visited.append(j)
        v = s.pop()
    point = goal
    while point != -1:
        try:
            came_from[point] = dist[point]
            point = dist[point]
        except:
            point = -1

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

    visited = []
    s = []
    h=heuristic(start,goal)
    heap.heappush(s,(h,start))
    visited.append(start)
    dist={}
    dist[start]=-1
    v = start
    while (s and v != goal):
        v = heap.heappop(s)
        for i in graph.neighboursOf(v[1]):
            if i not in visited:
                h=heuristic(i,goal)
                heap.heappush(s,(h,i))
                dist[i]=v[1]
                visited.append(i)

    point = goal
    while point != -1:
        try:
            came_from[point] = dist[point]
            point = dist[point]
        except:
            point = -1

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
    visited = []
    s = []
    s.append(start)
    visited.append(start)
    dist={}
    dist[start]=-1

    v = start
    while ((s) and v != goal):
        if (v == start):
            v = s.pop()
        neighbor = []
        for i in graph.neighboursOf(v):
            if i not in visited:
                neighbor.append((heuristic(i, goal), i))
        neighbor.sort()
        neighbor.reverse()
        neighbor=neighbor[0:beam_length]
        for i, j in neighbor:
            s.append(j)
            dist[j] = v
            visited.append(j)
        v = s.pop()
    point = goal
    while point != -1:
        try:
            came_from[point] = dist[point]
            point = dist[point]
        except:
            point = -1

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

    distance={}
    visited = []
    s = []
    dist_from_node = 1
    h = heuristic(start, goal)
    heap.heappush(s, (h, start))
    visited.append(start)
    distance[start]=0
    dist={}
    dist[start]=-1
    v = start
    while (s and v != goal):
        v = heap.heappop(s)
        for i in graph.neighboursOf(v[1]):
            if i not in visited:
                h = heuristic(i, goal) + dist_from_node + distance[v[1]]
                heap.heappush(s, (h, i))
                dist[i] = v[1]
                distance[i]=distance[v[1]]+dist_from_node

                visited.append(i)
    point = goal
    while point != -1:
        try:
            came_from[point] = dist[point]
            point = dist[point]
        except:
            point = -1

    # END HERE #

    return came_from


"""
search.py: Search algorithms on grid.
"""

import math




def heuristic(a, b):
    """
    Calculate the heuristic distance between two points.

    For a grid with only up/down/left/right movements, a
    good heuristic is manhattan distance.
    """

    # BEGIN HERE #
    (x1, y1) = a
    (x2, y2) = b
    d = 0
    
    if x1>x2:
        d += (x1-x2)
    else:
        d += (x2-x1)
        
    if y1>y2:
        d += (y1-y2)
    else:
        d += (y2-y1)
    
    return d

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
    if start == goal:
        
        return came_from
    
    (x1, y1) = start
    (x2, y2) = goal
    q = []
    q1 = []
    visited = [] 
    
    q.append(start)
    visited.append(start)
    
    while len(q):

        v = q.pop() 
               
        
    
        for i in graph.neighboursOf(v):
            if i == goal:
                came_from[i] = v
                return came_from
            
            if i not in visited:
                visited.append(i)
                q1.append(i)
                came_from[i] = v
                
        sorted(q1, key = lambda k:heuristic(goal,k), reverse = True)
        q.extend(q1)
        q1.clear()
    
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
    if start == goal:        
        return came_from
    
    (x1, y1) = start
    (x2, y2) = goal
    q = []
    q1 = []
    visited = [] 
    
    q.append(start)
    visited.append(start)
    
    while len(q):

        v = q.pop() 
               
        
    
        for i in graph.neighboursOf(v):
            if i == goal:
                came_from[i] = v
                return came_from
            
            
            if i not in visited:
                visited.append(i)
                q1.append(i)
                came_from[i] = v
                
        
        q.extend(q1)
        q1.clear()
        sorted(q, key = lambda k:heuristic(goal,k), reverse = True)
        
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
    w = beam_length
    n = 0
    if start == goal:        
        return came_from
    
    (x1, y1) = start
    (x2, y2) = goal
    q = []
    q1 = []
    visited = [] 
    
    q.append(start)
    q.append("*")
    visited.append(start)
    
    while len(q):
        
        v = q.pop(0)
        
        if v == "*":
            
            q.append("*")
            sorted(q1, key = lambda k:heuristic(goal,k), reverse = False)
            q.extend(q1[:w])
            q1.clear()
            n = 0
            continue
        
        n += 1
        for i in graph.neighboursOf(v):            
            if i == goal:  
                came_from[i] = v
                return came_from
            
            
            
            if i not in visited:
                visited.append(i)
                q1.append(i)
                came_from[i] = v
                
           
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
        
    
    
    inf = math.inf
    closedSet = []
    gScore = {}
    fScore = {}

    # The set of currently discovered nodes that are not evaluated yet.
     #Initially, only the start node is known.
    openSet = [start]
    
    # For each node, which node it can most efficiently be reached from.
    # If a node can be reached from many nodes, cameFrom will eventually contain the
    # most efficient previous step.
    

    # For each node, the cost of getting from the start node to that node.
    for i in range(graph.width*graph.height):
        gScore[i] =  inf 

    # The cost of going from start to start is zero.
    gScore[start] = 0

    # For each node, the total cost of getting from the start node to the goal
    # by passing by that node. That value is partly known, partly heuristic.
    for i in range(graph.width*graph.height):
        fScore[i] =  inf

    # For the first node, that value is completely heuristic.
    fScore[start] = heuristic(start, goal)
    
    current = start

    while len(openSet):       
        
        for node in openSet:
            
            if fScore[node] < fScore[current]:
                current = node
                #the node in openSet having the lowest fScore[] value"
        
        #if current == goal:
            #return came_from   # "is something leftout??"
        
        openSet.pop(openSet.index(current))
        
        closedSet.append(current)

        for neighbor in graph.neighboursOf(current):
            if neighbor in closedSet:
                continue		# Ignore the neighbor which is already evaluated."

            if neighbor not in openSet:	# Discover a new node"
                openSet.append(neighbor)
            
            # The distance from start to a neighbor"
            #the distance function may vary as per the solution requirements."
            tentative_gScore = gScore[current] + heuristic(current, neighbor)
            if tentative_gScore >= gScore[neighbor]:#using consistent heuristic
                continue		# This is not a better path."

            # This path is the best until now. Record it!"
            came_from[neighbor] = current
            gScore[neighbor] = tentative_gScore
            fScore[neighbor] = gScore[neighbor] + heuristic(neighbor, goal)
    # END HERE #

    return came_from


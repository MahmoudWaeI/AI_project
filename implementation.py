def astar(graph, start, goal):
    # Step 2: Initialize variables
    open_list = [start]     # List of open nodes to be visited
    # List of closed nodes that have already been visited
    closed_list = []        
    # Dictionary to keep track of each node's parent
    parent = {start: None}  
    # Dictionary to keep track of g score (cost so far) for each node
    g_score = {start: 0}    
    # Dictionary to keep track of f score (estimated total cost) for each node
    f_score = {start: heuristic(start, goal)}  

    # Step 4: Main loop
    while open_list:
        # Choose the node with the lowest f score as the current node
        current = min(open_list, key=lambda node: f_score[node])

        # If the current node is the goal node, stop and return the path from
        # start to goal
        if current == goal:
            return construct_path(parent, goal)

        # Remove the current node from the open list and add it to the closed list
        # open_list.remove(current)
        closed_list.append(current)

        # For each neighbor of the current node, do the following
        for neighbor in graph[current]:
            # If the neighbor is already in the closed list, skip it
            if neighbor in closed_list:
                continue

            # Calculate the tentative g score for the neighbor
            tentative_g_score = g_score[current] + graph[current][neighbor]

            # If the neighbor is not in the open list or the tentative g score is 
            # less than its current g score,
            # update the neighbor's g score and set its parent to be the current.
            if neighbor not in open_list or tentative_g_score < g_score[neighbor]:
                parent[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)


                # If the neighbor is not in the open list, add it to the open list
                if neighbor not in open_list:
                    open_list.append(neighbor)

    # Step 5: If the open list is empty and the goal node was not reached, then
    # there is no path from start to goal 
    return None

def heuristic(node, goal):
    # Define a heuristic function to estimate distance between two nodes
    pass

def construct_path(parent, goal):
    # Construct the path from start to goal using the parent dictionary
    pass

% Define the graph
graph = {
    'A': {'B': 3, 'C': 4},
    'B': {'D': 6, 'E': 7},
    'C': {'F': 5},
    'D': {},
    'E': {'F': 4},
    'F': {}
}

start = 'A'  % Start node
goal = 'F'   % Goal node

% Call the A* algorithm
path = astar(graph, start, goal)

% Report the results and outputs
if path:
    print(f"Shortest path from {start} to {goal}: {path}")
else:
    print(f"No path found from {start} to {goal}.")

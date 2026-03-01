"""
@file proj1_pranavjagdish_koli.py
@author Pranav Jagdish Koli
@brief The main Python file containing the BFS algorithm, move functions, and file generation logic.
@date 02-28-2026
@copyright Copyright (c) 2026
"""


import numpy as np
from collections import deque

# --- Data Structure Selection ---

def find_blank_tile(state):
    """Find the location (i, j) of the blank tile (0) in the state."""
    loc = np.where(state == 0)
    return int(loc[0][0]), int(loc[1][0])

# --- Action Subfunctions ---
# Each function checks if the move is valid, creates a new state, and returns it.
def Moving_Left(state):
    i, j = find_blank_tile(state)
    if j > 0:
        new_state = np.copy(state)
        new_state[i, j], new_state[i, j-1] = new_state[i, j-1], new_state[i, j]
        return True, new_state
    return False, state

def Moving_Right(state):
    i, j = find_blank_tile(state)
    if j < 2:
        new_state = np.copy(state)
        new_state[i, j], new_state[i, j+1] = new_state[i, j+1], new_state[i, j]
        return True, new_state
    return False, state

def Moving_Up(state):
    i, j = find_blank_tile(state)
    if i > 0:
        new_state = np.copy(state)
        new_state[i, j], new_state[i-1, j] = new_state[i-1, j], new_state[i, j]
        return True, new_state
    return False, state

def Moving_Down(state):
    i, j = find_blank_tile(state)
    if i < 2:
        new_state = np.copy(state)
        new_state[i, j], new_state[i+1, j] = new_state[i+1, j], new_state[i, j]
        return True, new_state
    return False, state

def get_string_rep(state):
    """It flattens matrix column-wise for file output."""
    return " ".join(map(str, state.flatten(order='F')))

def is_solvable(state):
    """A helper to check if a state can reach the goal using inversions."""
    flat = state.flatten(order='F')
    tiles = [t for t in flat if t != 0]
    inversions = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i] > tiles[j]:
                inversions += 1

    return inversions % 2 == 0

# --- BFS Algorithm ---
def solve_bfs(initial_state, goal_state):
    queue = deque([initial_state])
    initial_str = get_string_rep(initial_state)
    visited = {initial_str}
    
    # nodes_info: {current_str: (parent_str, node_index)}
    nodes_info = {initial_str: (None, 0)}
    all_explored = [initial_str]
    
    node_counter = 1
    goal_str = get_string_rep(goal_state)

    # BFS Loop
    while queue:
        current_node = queue.popleft()
        curr_str = get_string_rep(current_node)
        
        if curr_str == goal_str:
            return nodes_info, all_explored

        for action in [Moving_Up, Moving_Down, Moving_Left, Moving_Right]:
            status, new_node = action(current_node)
            node_str = get_string_rep(new_node)
            
            if status and node_str not in visited:
                visited.add(node_str)
                queue.append(new_node)
                nodes_info[node_str] = (curr_str, node_counter)
                all_explored.append(node_str)
                node_counter += 1
    return None, None

# --- Backtracking ---
def generate_path(nodes_info, goal_str):
    path = []
    curr = goal_str
    while curr is not None:
        path.append(curr)
        curr = nodes_info[curr][0]
    return path[::-1]

# --- Execution ---
# Initial state and Goal state.
initial = np.array([[8, 2, 3], 
                    [6, 5, 0], 
                    [7, 4, 1]])

goal = np.array([[1, 4, 7], 
                 [2, 5, 8], 
                 [3, 6, 0]])

if is_solvable(initial):
    print("Puzzle is solvable. Starting BFS...")
    data, explored = solve_bfs(initial, goal)
    
    if data:
        print("Goal Reached successfully!")
        # Textfile 1: Nodes.txt 
        with open('Nodes.txt', 'w') as f:
            for node in explored: 
                f.write(node + "\n")

        # Textfile 2: NodesInfo.txt
        with open('NodesInfo.txt', 'w') as f:
            f.write("Node_index\tParent_Node_index\tNode\n")
            for node_str, info in data.items():
                parent_str, idx = info
                p_idx = data[parent_str][1] if parent_str else 0
                f.write(f"{idx}\t{p_idx}\t{node_str}\n")

        # Textfile 3: nodePath.txt 
        path = generate_path(data, get_string_rep(goal))
        with open('nodePath.txt', 'w') as f:
            for p in path: 
                f.write(p + "\n")
else:
    print("Initial state is unsolvable.")
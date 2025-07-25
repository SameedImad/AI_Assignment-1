def bfs_bridge(initial_state):
    OPEN = [initial_state]
    CLOSED = []
    
    while OPEN:
        node_pair = OPEN.pop(0)  #pop first
        N = node_pair[0] if isinstance(node_pair, tuple) else node_pair
        parent = node_pair[1] if isinstance(node_pair, tuple) else None
        
        if goal_test_bridge(N):
            return reconstruct_path((N, parent), CLOSED)
        
        CLOSED.append((N, parent))
        children = move_gen_bridge(N)
        new_nodes = remove_seen_bridge(N, OPEN + [x[0] for x in CLOSED])
        new_pairs = [(node, (N, parent)) for node in new_nodes]
        OPEN.extend(new_pairs)
    
    return []

def move_gen_bridge(state):
    children = []
    people = state[0]
    umbrella = state[1]
    time = state[2]
    
    if umbrella == 0:  # Umbrella on start side
        for i in range(len(people)):
            for j in range(i + 1, len(people)):
                cross_time = max(people[i][1], people[j][1])
                if time + cross_time <= 60:
                    new_people = people[:i] + people[i+1:j] + people[j+1:]
                    new_state = (new_people + [(people[i][0], people[j][0], 1)], 1, time + cross_time)
                    children.append(new_state)
                    if i < len(people) - 1:
                        return_time = people[i][1]
                        if time + cross_time + return_time <= 60:
                            new_people_return = new_people + [(people[i][0], 0, 0)]
                            children.append((new_people_return, 0, time + cross_time + return_time))
    return children

def goal_test_bridge(state):
    return state[1] == 1 and len(state[0]) == 0 and state[2] <= 60

def remove_seen_bridge(node, seen):
    return [n for n in move_gen_bridge(node) if n not in [s[0] for s in seen]]

def reconstruct_path(node_pair, closed):
    path = [node_pair[0]]
    current = node_pair
    while current[1]:
        for pair in closed:
            if pair[0] == current[1][0]:
                path.insert(0, pair[0])
                current = pair
                break
    return path

def dfs_bridge(initial_state):
    OPEN = [initial_state]
    CLOSED = []
    
    while OPEN:
        node_pair = OPEN.pop(0)  #pop first
        N = node_pair[0] if isinstance(node_pair, tuple) else node_pair
        parent = node_pair[1] if isinstance(node_pair, tuple) else None
        
        if goal_test_bridge(N):
            return reconstruct_path((N, parent), CLOSED)
        
        CLOSED.append((N, parent))
        children = move_gen_bridge(N)
        new_nodes = remove_seen_bridge(N, OPEN + [x[0] for x in CLOSED])
        new_pairs = [(node, (N, parent)) for node in new_nodes]
        OPEN = new_pairs + OPEN
    
    return []
    
initial = [((('Amogh', 5, 0), ('Ameya', 10, 0), ('GM', 20, 0), ('GF', 25, 0)), 0, 0)]
result = bfs_bridge(initial)
print("BFS Path:", result)
result = dfs_bridge(initial)
print("\nDFS Path:", result)

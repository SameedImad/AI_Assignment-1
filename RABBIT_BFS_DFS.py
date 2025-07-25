def bfs_rabbit(initial_state):
    OPEN = [initial_state]
    CLOSED = []
    
    while OPEN:
        node_pair = OPEN.pop(0)  #pop first
        N = node_pair[0] if isinstance(node_pair, tuple) else node_pair
        parent = node_pair[1] if isinstance(node_pair, tuple) else None
        
        if goal_test_rabbit(N):
            return reconstruct_path((N, parent), CLOSED)
        
        CLOSED.append((N, parent))
        children = move_gen_rabbit(N)
        new_nodes = remove_seen_rabbit(N, OPEN + [x[0] for x in CLOSED])
        new_pairs = [(node, (N, parent)) for node in new_nodes]
        OPEN.extend(new_pairs)
    
    return []

def move_gen_rabbit(state):
    children = []
    empty_idx = state.index('_')
    if empty_idx > 0 and state[empty_idx - 1] in ['E1', 'E2', 'E3', 'W1', 'W2', 'W3']:
        new_state = state.copy()
        new_state[empty_idx], new_state[empty_idx - 1] = new_state[empty_idx - 1], '_'
        children.append(new_state)
    if empty_idx < len(state) - 1 and state[empty_idx + 1] in ['E1', 'E2', 'E3', 'W1', 'W2', 'W3']:
        new_state = state.copy()
        new_state[empty_idx], new_state[empty_idx + 1] = new_state[empty_idx + 1], '_'
        children.append(new_state)
    return children

def goal_test_rabbit(state):
    return state == ['W1', 'W2', 'W3', '_', 'E1', 'E2', 'E3']

def remove_seen_rabbit(node, seen):
    return [n for n in move_gen_rabbit(node) if n not in [s[0] for s in seen]]

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


def dfs_rabbit(initial_state):
    OPEN = [initial_state]
    CLOSED = []
    
    while OPEN:
        node_pair = OPEN.pop(0)
        N = node_pair[0] if isinstance(node_pair, tuple) else node_pair
        parent = node_pair[1] if isinstance(node_pair, tuple) else None
        
        if goal_test_rabbit(N):
            return reconstruct_path((N, parent), CLOSED)
        
        CLOSED.append((N, parent))
        children = move_gen_rabbit(N)
        new_nodes = remove_seen_rabbit(N, OPEN + [x[0] for x in CLOSED])
        new_pairs = [(node, (N, parent)) for node in new_nodes]
        OPEN = new_pairs + OPEN
    
    return []

initial = ['E1', 'E2', 'E3', '_', 'W1', 'W2', 'W3']
result = bfs_rabbit(initial)
print("BFS Path:", result)
result1=dfs_rabbit(initial)
print("\nDFS Path:",result)

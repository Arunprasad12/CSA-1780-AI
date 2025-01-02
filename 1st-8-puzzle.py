import heapq
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
initial_state = (1, 2, 3, 4, 0, 6, 7, 5, 8)
def manhattan_distance(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_row = (state[i] - 1) // 3
            goal_col = (state[i] - 1) % 3
            curr_row = i // 3
            curr_col = i % 3
            distance += abs(goal_row - curr_row) + abs(goal_col - curr_col)
    return distance
def generate_moves(state):
    moves = []
    empty_index = state.index(0)
    if empty_index - 3 >= 0:
        moves.append(empty_index - 3)
    if empty_index + 3 < 9:
        moves.append(empty_index + 3)
    if empty_index % 3 != 0:
        moves.append(empty_index - 1)
    if (empty_index + 1) % 3 != 0:
        moves.append(empty_index + 1)
    return moves
def solve_puzzle(initial_state):
    open_set = [(manhattan_distance(initial_state), initial_state)]
    heapq.heapify(open_set)
    closed_set = set()
    parent_map = {initial_state: None}
    while open_set:
        _, current_state = heapq.heappop(open_set)
        if current_state == goal_state:
            path = []
            while current_state is not None:
                path.insert(0, current_state)
                current_state = parent_map[current_state]
            return path
        closed_set.add(current_state)
        moves = generate_moves(current_state)
        for move in moves:
            new_state = list(current_state)
            new_state[current_state.index(0)], new_state[move] = new_state[move], new_state[current_state.index(0)]
            new_state = tuple(new_state)
            if new_state not in closed_set:
                if (manhattan_distance(new_state), new_state) not in open_set:
                    heapq.heappush(open_set, (manhattan_distance(new_state), new_state))
                    parent_map[new_state] = current_state
solution_path = solve_puzzle(initial_state)
for step, state in enumerate(solution_path):
    print(f"Step {step}:")
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

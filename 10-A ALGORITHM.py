import heapq

def a_star(grid, start, goal):
    open_set, closed_set = [], set()
    heapq.heappush(open_set, (0, start, None))
    parent = {}
    while open_set:
        f, current, prev = heapq.heappop(open_set)
        if current in closed_set:
            continue
        closed_set.add(current)
        parent[current] = prev
        if current == goal:
            path, node = [], current
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1]
        neighbors = [(current[0] + dx, current[1] + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
        for neighbor in neighbors:
            if 0 <= neighbor[0] < len(grid[0]) and 0 <= neighbor[1] < len(grid) and grid[neighbor[1]][neighbor[0]] == 0:
                heapq.heappush(open_set, (f + 1 + abs(neighbor[0] - goal[0]) + abs(neighbor[1] - goal[1]), neighbor, current))

    return None

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (4, 4)

path = a_star(grid, start, goal)
print("Path:", path if path else "No path found")

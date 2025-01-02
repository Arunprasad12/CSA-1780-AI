% Define the graph using facts
connected(a, b, 1).
connected(a, c, 1).
connected(b, d, 1).
connected(b, e, 1).
connected(c, f, 1).
connected(c, g, 1).
connected(d, h, 1).
connected(e, i, 1).

% BFS implementation with path cost
bfs_cost(Start, Goal, Path) :-
    bfs_queue_cost([[Start]], Goal, PathRev),
    reverse(PathRev, Path).

% Base case: Goal node is reached
bfs_queue_cost([[Goal|Path]|_], Goal, [Goal|Path]).

% Recursive case: Explore neighboring nodes with cost
bfs_queue_cost([[Node|Path]|Paths], Goal, FinalPath) :-
    findall([Neighbor,Node|Path], (connected(Node, Neighbor, _), \+ member(Neighbor, [Node|Path])), NewPaths),
    append(Paths, NewPaths, UpdatedPaths),
    bfs_queue_cost(UpdatedPaths, Goal, FinalPath).

% Entry point for querying the BFS with path cost
find_bfs_path_cost(Start, Goal, Path) :-
    bfs_cost(Start, Goal, Path).

% Entry point for querying the BFS with path cost and returning the cost
find_bfs_path_cost_and_cost(Start, Goal, Path, Cost) :-
    bfs_cost(Start, Goal, Path),
    path_cost(Path, Cost).

% Calculate the cost of a path
path_cost(Path, Cost) :-
    length(Path, CostMinusOne),
    Cost is CostMinusOne - 1.

% Example usage
% Query: find_bfs_path_cost_and_cost(a, i, Path, Cost).
% This will return Path = [a, b, e, i], Cost = 3.
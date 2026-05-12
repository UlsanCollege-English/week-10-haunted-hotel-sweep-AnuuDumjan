# Week 10 Coding #8: Haunted Hotel Sweep

## Summary

This assignment uses a graph to represent different areas in a haunted hotel and the connections between them.

BFS (Breadth-First Search) explores nearby areas level by level using a queue.

DFS (Depth-First Search) explores as deep as possible before backtracking using a stack.

The `visited` set is important because it prevents revisiting the same area multiple times and avoids infinite loops in graphs with cycles.

---

## Approach

- Used `graph.get(area, [])` to safely return neighbors or an empty list.
- Used BFS logic with a queue to check whether a path exists between two areas.
- Used `collections.deque` for efficient queue operations in BFS.
- Used a stack for DFS traversal.
- Used a `visited` set in all traversal functions to prevent repeated visits and infinite loops.
- Reversed neighbor order in DFS so traversal follows the original graph order correctly.

---

## Complexity

### `get_neighbors`

- Time: O(1)
- Space: O(1)
- Why: Dictionary lookup is constant time.

### `has_path`

- Time: O(V + E)
- Space: O(V)
- Why: BFS may visit every vertex and edge once.

### `bfs_order`

- Time: O(V + E)
- Space: O(V)
- Why: BFS stores visited nodes and queue data.

### `dfs_order`

- Time: O(V + E)
- Space: O(V)
- Why: DFS may visit all vertices and store them in the stack.

### Stretch: `count_reachable_areas` if completed

- Time: O(V + E)
- Space: O(V)
- Why: Traverses all reachable areas while tracking visited nodes.

---

## Edge-Case Checklist

- [x] empty graph
- [x] missing start area
- [x] missing target area
- [x] `start == target`
- [x] graph with a cycle
- [x] disconnected graph
- [x] area with no neighbors

Notes:
Using the `visited` set carefully was important to avoid repeated visits in cyclic graphs.

---

## Tests Added

- Tested missing areas
- Tested graph traversal order
- Tested reachable and unreachable paths

---

## Known Limitations

No known limitations.

---

## Assistance & Sources

AI used? Y

If yes, explain what it helped with:

- explanations
- debugging
- syntax reminders

Other sources used:

- Python documentation
- Class notes
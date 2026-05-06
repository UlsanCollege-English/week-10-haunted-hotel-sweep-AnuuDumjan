# Week 10 Coding #8: Haunted Hotel Sweep

**Topic:** Graphs, adjacency lists, BFS/DFS, visited sets  
**Due:** Sunday, 2026-05-10, 23:59 KST  
**Language:** Python 3.11+  
**Libraries:** Standard library only  
**Graded files:** `.py` files + `pytest` tests  
**Notebooks:** Allowed for practice only, not graded

---

## Story

A night security guard is checking a haunted hotel after strange sensor alerts.

The hotel is represented as a graph:

- **areas** are nodes
- **hallways / stairs / doors** are edges
- some areas form loops
- some wings may be unreachable because doors are locked

Your job is to write graph helper functions so the guard can understand which areas are connected and how to sweep the hotel safely.

---

## Graph Format

The graph will be an **unweighted, undirected adjacency list**.

Example:

```python
hotel = {
    "Lobby": ["Hallway", "Dining Room"],
    "Hallway": ["Lobby", "Library", "Stairs"],
    "Dining Room": ["Lobby"],
    "Library": ["Hallway"],
    "Stairs": ["Hallway", "Tower"],
    "Tower": ["Stairs"],
}
```

Each key is an area.
Each value is a list of neighboring areas.

For this assignment, assume the graph is already built for you.
You do **not** need to write an `add_edge` function.

---

## Traversal Order Rule

Use the neighbor order exactly as given in the graph.

Do **not** sort neighbors unless the instructions specifically say to sort.

For stack-based DFS, loop through neighbors in reversed order so DFS follows the original neighbor order when possible.

---

## Required Functions

Write these functions in `src/challenges.py`.

### 1. `get_neighbors`

```python
def get_neighbors(graph: dict[str, list[str]], area: str) -> list[str]:
    """Return neighboring areas, or [] if the area is missing."""
```

Return the list of neighbors for `area`.
If `area` is not in the graph, return an empty list.

---

### 2. `has_path`

```python
def has_path(graph: dict[str, list[str]], start: str, target: str) -> bool:
    """Return True if target is reachable from start."""
```

Return `True` if there is a path from `start` to `target`.
Return `False` if either area is missing or if the target cannot be reached.

If `start == target` and the area exists in the graph, return `True`.

---

### 3. `bfs_order`

```python
def bfs_order(graph: dict[str, list[str]], start: str) -> list[str]:
    """Return areas in breadth-first sweep order."""
```

Use BFS with a queue.
Return the order in which areas are visited.

If `start` is missing, return an empty list.

---

### 4. `dfs_order`

```python
def dfs_order(graph: dict[str, list[str]], start: str) -> list[str]:
    """Return areas in depth-first sweep order."""
```

Use DFS with a stack.
Return the order in which areas are visited.

If `start` is missing, return an empty list.

---

## Stretch Function

This function is optional.

### 5. `count_reachable_areas`

```python
def count_reachable_areas(graph: dict[str, list[str]], start: str) -> int:
    """Return how many unique areas are reachable from start."""
```

Return the number of unique areas reachable from `start`.
If `start` is missing, return `0`.

---

## Required Edge Cases

Your code should handle:

- empty graph
- missing start area
- missing target area
- `start == target`
- graph with a cycle
- disconnected graph
- area with no neighbors

---

## Complexity Expectations

In your README, explain the time and space complexity for each required function.

Expected targets:

```text
get_neighbors:
Time: O(1) average
Space: O(1)

has_path:
Time: O(V + E)
Space: O(V)

bfs_order:
Time: O(V + E)
Space: O(V)

dfs_order:
Time: O(V + E)
Space: O(V)
```

Where:

- `V` = number of areas / nodes
- `E` = number of hallways / edges

---

## Submission Checklist

Before submitting, confirm:

- [ ] `pytest -q` passes
- [ ] all required functions are implemented
- [ ] no external libraries are used
- [ ] README is completed
- [ ] README includes complexity explanations
- [ ] README includes edge cases
- [ ] README includes Assistance & Sources
- [ ] code uses clear names and type hints

---

## Reminder

The `visited` set is not optional.

A haunted hotel with looping hallways and no visited set is how your robot gets trapped forever near the vending machine. Do not do that to the robot.

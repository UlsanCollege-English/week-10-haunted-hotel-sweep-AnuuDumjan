from collections import deque


Graph = dict[str, list[str]]


def get_neighbors(graph: Graph, area: str) -> list[str]:
    """Return neighboring areas, or [] if the area is missing."""

    return graph.get(area, [])


def has_path(graph: Graph, start: str, target: str) -> bool:
    """Return True if target is reachable from start."""

    if start not in graph or target not in graph:
        return False

    if start == target:
        return True

    visited = set()
    queue = deque([start])

    while queue:
        current = queue.popleft()

        if current == target:
            return True

        if current not in visited:
            visited.add(current)

            for neighbor in graph[current]:
                queue.append(neighbor)

    return False


def bfs_order(graph: Graph, start: str) -> list[str]:
    """Return areas in breadth-first sweep order."""

    if start not in graph:
        return []

    visited = set()
    queue = deque([start])
    order = []

    while queue:
        current = queue.popleft()

        if current not in visited:
            visited.add(current)
            order.append(current)

            for neighbor in graph[current]:
                queue.append(neighbor)

    return order


def dfs_order(graph: Graph, start: str) -> list[str]:
    """Return areas in depth-first sweep order."""

    if start not in graph:
        return []

    visited = set()
    stack = [start]
    order = []

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.add(current)
            order.append(current)

            for neighbor in reversed(graph[current]):
                stack.append(neighbor)

    return order


def count_reachable_areas(graph: Graph, start: str) -> int:
    """Return how many unique areas are reachable from start."""

    if start not in graph:
        return 0

    visited = set()
    queue = deque([start])

    while queue:
        current = queue.popleft()

        if current not in visited:
            visited.add(current)

            for neighbor in graph[current]:
                queue.append(neighbor)

    return len(visited)
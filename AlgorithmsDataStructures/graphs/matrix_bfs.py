from collections import deque

# Shortest path from top left to bottom right
def bfs(grid):
    # Taking the dimensions of the grid 
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    queue = deque()
    queue.append((0, 0))
    # visit to ensure we don't end up in a infinite loop
    visit.add((0, 0))

    length = 0
    while queue:
        # snapshot of the length of the queue
        for i in range(len(queue)):
            # grab co-ordinates of the position
            r, c = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return length

            # looks complex, but relatively easy 
            # enumerate all four possible directions at which we can move
            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbors:
                if (min(r + dr, c + dc) < 0 or
                    r + dr == ROWS or c + dc == COLS or
                    (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                    continue
                queue.append((r + dr, c + dc))
                # we add to the visit hashset as soon as we add to the queue
                # ensures we run in O(n*m) complexity -> Never visit the same position twice
                visit.add((r + dr, c + dc))
        # not adding individual nodes, but we're adding the entire level
        length += 1


# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

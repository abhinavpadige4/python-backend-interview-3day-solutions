"""
LeetCode Problem 200: Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are all surrounded by water.

Time Complexity: O(m * n) - Each cell visited once
Space Complexity: O(min(m, n)) - For BFS queue or DFS recursion stack (worst case)
"""

from typing import List
from collections import deque

def num_islands(grid: List[List[str]]) -> int:
    """
    Count the number of islands in a 2D grid.
    
    Args:
        grid: 2D list of '1's (land) and '0's (water)
        
    Returns:
        Number of islands
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    num_islands = 0
    
    def bfs(r: int, c: int) -> None:
        """Breadth-first search to mark all connected land as visited."""
        queue = deque([(r, c)])
        grid[r][c] = '0'  # Mark as visited
        
        while queue:
            row, col = queue.popleft()
            # Check all 4 directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = row + dr, col + dc
                if (0 <= nr < rows and 0 <= nc < cols and 
                    grid[nr][nc] == '1'):
                    grid[nr][nc] = '0'  # Mark as visited
                    queue.append((nr, nc))
    
    def dfs(r: int, c: int) -> None:
        """Depth-first search to mark all connected land as visited."""
        # Base case: out of bounds or water
        if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0'):
            return
        
        # Mark current cell as visited
        grid[r][c] = '0'
        
        # Recursively visit all 4 directions
        dfs(r - 1, c)  # up
        dfs(r + 1, c)  # down
        dfs(r, c - 1)  # left
        dfs(r, c + 1)  # right
    
    # Iterate through all cells
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                num_islands += 1
                # Use BFS or DFS to mark all connected land
                bfs(r, c)  # or dfs(r, c)
    
    return num_islands

# Test cases
if __name__ == "__main__":
    # Test case 1
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(f"Input: grid =")
    for row in grid1:
        print(f"  {row}")
    print(f"Output: {num_islands([row[:] for row in grid1])}")  # Expected: 1
    print()
    
    # Test case 2
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(f"Input: grid =")
    for row in grid2:
        print(f"  {row}")
    print(f"Output: {num_islands([row[:] for row in grid2])}")  # Expected: 3
    print()
    
    # Test case 3 - All water
    grid3 = [
        ["0","0","0","0"],
        ["0","0","0","0"],
        ["0","0","0","0"]
    ]
    print(f"Input: grid =")
    for row in grid3:
        print(f"  {row}")
    print(f"Output: {num_islands([row[:] for row in grid3])}")  # Expected: 0
    print()
    
    # Test case 4 - All land
    grid4 = [
        ["1","1"],
        ["1","1"]
    ]
    print(f"Input: grid =")
    for row in grid4:
        print(f"  {row}")
    print(f"Output: {num_islands([row[:] for row in grid4])}")  # Expected: 1
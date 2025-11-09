"""
Author: Wahuuuuu
Date:   8/11/2025

This program traverse in dfs a matrix[int] which contains a certain amount of obstacles, reverse it's value, and prints the result.
Furthermore, it's used for practice depth-first-searching/traversing and closure capture
"""
from typing import Any
from typing import TypeAlias
Matrix: TypeAlias = list[list[Any]]
Row: TypeAlias = list[Any]


def traverse(m: Matrix) -> Matrix:
    """
    This function receives a Matix contains some obstacles, returns a Matrix
    with it's value reversed without modify any obstacle.
    Parameter: m: Matrix
    Return: m: Matrix
    """
    visited: Matrix = [[False for i in row] for row in m]
    y: Row = 0
    x: int = 0
    dir: tuple[tuple[Row, int]] = ((0, 1), (-1, 0), (0, -1), (1, 0))
    
    def dfs(y: int, x: int, m: Matrix) -> None:
        """
        This method receives coordinates y, x in matrix m, 
        reverse the value m[y][x], 
        search every neighbour value visitables and visit them by calling this method itself
        ---
        Parameters:
            m: Matrix modifiable
            x, y: coordinates in m, which m[y][x] is not reversed yet
        """
        m[y][x] *= -1
        visited[y][x] = True

        for j, i in dir:
            in_bound = (0 <= (y + j) < len(m)) and (0 <= (x + i) < len(m[y + j]))

            if in_bound: 
                not_visited = not visited[y+j][x+i]
                is_number = type(m[j][i]) == int
                
                if not_visited and is_number:
                    dfs(y+j, x+i, m)
    
    dfs(0, 0, m)
            
    return m


o: str = "o"
m: Matrix = [
    [1, 4, 3, 3, 2, 2, 3], 
    [1, 0, 0, 8, o, 6, o],
    [0, 5, 1, 2, o, 1, 3],
    [-1, -3, -1, -4],
    [o, 1, 1, 4, 5, 1, 4]                 
]

traverse(m)

for row in m:
    for element in row:
        print(element, end=" ")
    print()


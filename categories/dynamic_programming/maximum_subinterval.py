"""
Author:  Wahuuuuu
Date: 15/11/2025
"""
from typing import Any
from typing import Final

def solve(W: Final[list[int]], n: int) -> list[int]:
    """
    给定一个长度为 n 的数组 w
    选出其中连续且非空的一段，使得这段和最大。
    Given an array w, whose length is n
    Print an non-empty, continuous subarray, which the sum of it's value is the maxim in w.

    状态: 
    若当前位于 i, 状态为 w[i] 或 sum(w[start:i]) + w[i]

    状态转移: 
    : sum = w[i]                  if i == 0
    : sum = w[start:i] + w[i]     if i >  0

    思路：
    \  0     1    2   3  -> j/start
    0: 0
    1: 01    1
    2: 01+2  1+2  2
    3: 012+3 12+3 2+3 3
    i <-
    ...
    memory = [None] * n
    for i in range(W):
        for j in range(i):
            memory[j] += w[i]
            if memory[j] > max:
                max = memory[j]
                max_position = (j, i + 1)
    
    return 
    """
    if (len(W) == 0): raise ValueError("The list has 0 values!!")
    memory: list[Any] = [0] * n

    max: int = W[0]
    max_pos: list[int, int] = [0, 1]

    for i in range(n):
        for j in range(i+1):
            memory[j] += W[i]

            if memory[j] > max:
                max = memory[j]
                max_pos = [j, i+1]
        print(memory)
    
    return W[max_pos[0]:max_pos[1]]


l = [10086, -4, 3, +114, -10086, -4, 3]
print(solve(l, len(l)))



    









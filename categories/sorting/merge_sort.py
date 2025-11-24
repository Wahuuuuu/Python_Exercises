"""
Author: Wahuuuuu
Date:  12/11/2025
"""

def main() -> None:
    a: list[int] = [-7, 0, 10086, 3, 9, 9, -4, 5]

    s = merge_sort(a, 0, len(a) - 1)

    print(s)



def merge_sort(a: list[int], left: int, right: int) -> list[int]:
    if left == right:
        return [a[left]]

    mid = (left + right) // 2
    l1: list[int] = merge_sort(a, left, mid)
    l2: list[int] = merge_sort(a, mid + 1, right)

    return sort(l1, l2)

def sort(l1: list[int], l2: list[int]) -> list[int]:
    """
    Parameters:
    l1: an increasingly sorted list
    l2: an increasingly sorted list
    ---
    Return:
    an increasingly sorted list, whose elements comes from l1 and l2
    """

    i, j = 0, 0
    aux: list[int] = []
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]: 
            aux.append(l1[i])
            i += 1
        else:
            aux.append(l2[j])
            j += 1
    
    if i == len(l1):
        for j in range(j, len(l2)):
            aux.append(l2[j])
    
    if j == len(l2):
        for i in range(i, len(l1)):
            aux.append(l1[i])

    return aux


main()






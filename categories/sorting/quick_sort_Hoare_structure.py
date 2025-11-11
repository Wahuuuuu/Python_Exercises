"""
Author: Wahuuuuu
Date: 11/11/2025
"""
from random import randint


def main() -> None:
    a: list[int] = [7, 9, 2, 5, 10, -3, -7, 10086]

    quick_sort(a, 0, len(a)-1)

    print(a)


def quick_sort(a: list[int], left: int, right: int) -> None:
    if left >= right:
        return a
    
    pivot = partition(a, left, right)
    quick_sort(a, left, pivot)
    quick_sort(a, pivot + 1, right)


def partition(a: list[int], left: int, right: int) -> int:
    pivot = a[randint(left, right)]
    i, j = left - 1, right + 1

    while True:
        i += 1
        while a[i] < pivot: i += 1
        j -= 1
        while a[j] > pivot: j -= 1
        if i >= j: 
            return j
        a[i], a[j] = a[j], a[i]


main()
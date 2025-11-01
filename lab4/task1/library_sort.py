from typing import List, TypeVar
from math import ceil
from task1.Comparison import Comparison

T = TypeVar("T", bound=Comparison)


def library_sort(arr: List[T], epsilon: float = 1.0) -> List[T]:
    n = len(arr)
    if n <= 1:
        return arr.copy()

    size = ceil(n * (1 + epsilon))
    table: List[T | None] = [None] * size
    occupied_positions: List[int] = []

    mid = size // 2
    table[mid] = arr[0]
    occupied_positions.append(mid)

    def binary_search(x: T) -> int:
        left, right = 0, len(occupied_positions)
        while left < right:
            middle = (left + right) // 2
            if table[occupied_positions[middle]] < x:
                left = middle + 1
            else:
                right = middle
        return left

    def rebalance(
        table: List[T | None], positions: List[int]
    ) -> tuple[int, List[T | None], List[int]]:
        copy_of_elements = [table[p] for p in positions]
        copy_of_elements.sort()
        m = len(copy_of_elements)
        new_size = max(len(table), ceil(m * (1 + epsilon)))
        new_table: List[T | None] = [None] * new_size
        new_positions: List[int] = []

        step = new_size / (m + 1)
        for i, v in enumerate(copy_of_elements):
            pos = int((i + 1) * step)
            if pos >= new_size:
                pos = new_size - 1
            new_table[pos] = v
            new_positions.append(pos)
        return new_size, new_table, new_positions

    def find_slot(
        table: List[T | None], positions: List[int], index: int, size: int
    ) -> int:
        left = positions[index - 1] if index > 0 else -1
        right = positions[index] if index < len(positions) else size
        low = left + 1
        high = right - 1
        if low > high:
            return -1

        center_of_interval = (low + high) // 2
        if table[center_of_interval] is None:
            return center_of_interval
        for d in range(low, high + 1):
            if table[d] is None:
                return d
        return -1

    for x in arr[1:]:
        index = binary_search(x)
        slot = find_slot(table, occupied_positions, index, size)
        if slot == -1:
            size, table, occupied_positions = rebalance(table, occupied_positions)
            index = binary_search(x)
            slot = find_slot(table, occupied_positions, index, size)
            if slot == -1:
                for p in range(size):
                    if table[p] is None:
                        slot = p
                        break
        table[slot] = x
        occupied_positions.insert(index, slot)

    return [table[p] for p in occupied_positions]

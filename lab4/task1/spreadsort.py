from typing import List, TypeVar
from task1.Comparison import Comparison

T = TypeVar("T", bound=Comparison)


def spreadsort(arr: List[T], bucket_count: int | None = None) -> List[T]:
    n = len(arr)
    if n <= 1:
        return arr.copy()

    if bucket_count is None:
        bucket_count = max(5, n // 5)

    buckets: List[List[T]] = [[] for _ in range(bucket_count)]

    for x in arr:
        count = 0
        for y in arr:
            if y < x:
                count += 1
        index = int(count / (n - 1) * (bucket_count - 1)) if n > 1 else 0
        buckets[index].append(x)

    result: List[T] = []
    for b in buckets:
        b.sort()
        result.extend(b)

    return result

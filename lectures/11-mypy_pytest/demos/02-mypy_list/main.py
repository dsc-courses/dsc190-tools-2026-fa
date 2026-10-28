from collections.abc import Collection

def average(numbers: Collection[float]) -> float:
    return sum(numbers) / len(numbers)

average({1, 2, 3})

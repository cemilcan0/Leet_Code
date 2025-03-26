class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat = [val for row in grid for val in row]
        mod_base = flat[0]

        if any((val - mod_base) % x != 0 for val in flat):
            return -1

        flat = [(val - mod_base) // x for val in flat]
        flat.sort()
        median = flat[len(flat) // 2]

        return sum(abs(val - median) for val in flat)

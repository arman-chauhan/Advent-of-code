#
# Day 6: Wait For It
#
from math import floor, ceil, sqrt
from functools import reduce


class Solution:
    @staticmethod
    def count_solutions(t, d):
        """
        Calculate the number of integer solutions (x, y) such that:
        -> x + y = ts
        -> x * y > d
        """
        # Compute the potential bounds for the product
        discriminant = sqrt(t ** 2 - 4 * d)
        upper_bound = (t + discriminant) / 2
        lower_bound = (t - discriminant) / 2

        # Adjust to exclude unnecessary values
        upper_bound = upper_bound - 1 if upper_bound.is_integer() else floor(upper_bound)
        lower_bound = lower_bound + 1 if lower_bound.is_integer() else ceil(lower_bound)

        # Then return number of integers in the interval
        return upper_bound - lower_bound + 1

    def part_one(self, data):
        time, distance = [
            [*map(int, line.split(":")[1].split())] for line in data.split("\n")
        ]

        ways = [self.count_solutions(t, d) for t, d in zip(time, distance)]
        # ways = map(lambda t, d: self.count_solutions(t, d), time, duration)

        return int(reduce(lambda x, y: x * y, ways))

    def part_two(self, data):
        time, duration = [
            int("".join(line.split(":")[1].split())) for line in data.split("\n")
        ]
        return self.count_solutions(time, duration)

    def solve(self):
        with open("input.txt", "r") as f:
            data = f.read()
            print(f"{self.part_one(data)=}")
            print(f"{self.part_two(data)=}")


solver = Solution()
solver.solve()

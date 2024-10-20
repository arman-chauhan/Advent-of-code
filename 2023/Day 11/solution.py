"""
Day 11: Cosmic Expansion

New Concepts Learned:

"""
from copy import deepcopy


class Solution:
    def solve(self):
        with open("input.txt", "r") as f:
            data = f.read()
            data = self.parse(data)
            print(f"{self.part_one(deepcopy(data))=}")
            print(f"{self.part_two(deepcopy(data))=}")

    def part_one(self, universe):
        universe = self.expand(universe)
        galaxies = self.get_galaxies(universe)
        total_sum = 0
        for i, galaxy in enumerate(galaxies):
            for nextGalaxy in galaxies[i:]:
                total_sum += self.manhattan_distance(galaxy, nextGalaxy)

        return total_sum

    def part_two(self, universe):
        weighted_row = list()
        weighted_col = list()
        weight = 0
        for i, row in enumerate(universe):
            weighted_row.append(weight)
            if "#" not in row:
                weight += 1000000
            else:
                weight += 1

        t_universe = list(zip(*universe))  # transpose
        weight = 0
        for i, col in enumerate(t_universe):
            weighted_col.append(weight)
            if "#" not in col:
                weight += 1000000
            else:
                weight += 1

        indices = list()
        for i, row in enumerate(universe):
            for j, obj in enumerate(row):
                if obj == '#':
                    indices.append((weighted_row[i], weighted_col[j]))
        total_sum = 0
        for i, galaxy in enumerate(indices):
            for nextGalaxy in indices[i:]:
                total_sum += self.manhattan_distance(galaxy, nextGalaxy)
        return total_sum

    @staticmethod
    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    @staticmethod
    def get_galaxies(universe):
        indices = list()
        for i, row in enumerate(universe):
            for j, obj in enumerate(row):
                if obj == '#':
                    indices.append((i, j))
        return indices

    @staticmethod
    def expand(universe):
        temp_universe = []

        # Expand rows
        for row in universe:
            temp_universe.append(row)
            if "#" not in row:
                temp_universe.append(row)

        transposed_universe = list(zip(*temp_universe))

        expanded_universe = []
        # Expand columns
        for col in transposed_universe:
            expanded_universe.append(col)
            if "#" not in col:
                expanded_universe.append(col)

        expanded_universe = list(zip(*expanded_universe))

        expanded_universe = [list(row) for row in expanded_universe]
        return expanded_universe

    @staticmethod
    def parse(data):
        data = [list(line) for line in data.splitlines()]
        return data


solver = Solution()
solver.solve()

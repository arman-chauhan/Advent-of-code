"""
Day 10: Pipe Maze

New Concepts Learned:
 - Shoelace Theorem: Used to calculate the area of a polygon based on its ordered vertices and edges.
 - Pick's Theorem: Calculates the area of a simple polygon on a grid using the number of interior and boundary points.
"""

from collections import deque


class Solution:
    def __init__(self):
        self.rows, self.cols = None, None
        self.pipe_map = {
            'S': [(1, 0), (-1, 0), (0, 1), (0, -1)],
            '|': [(1, 0), (-1, 0)],
            '-': [(0, 1), (0, -1)],
            'L': [(-1, 0), (0, 1)],
            'J': [(-1, 0), (0, -1)],
            '7': [(1, 0), (0, -1)],
            'F': [(1, 0), (0, 1)],
        }
        self.corner_pipes = 'LF7JS'

    def solve(self):
        with open("input.txt", "r") as f:
            data = f.read().splitlines()
            self.rows = len(data)
            self.cols = len(data[0])
            print(f"{self.part_one(data)=}")
            print(f"{self.part_two(data)=}")

    def part_one(self, data) -> int:
        start = ('S', self.get_starting(data))
        pipes = self._dfs(data, start)
        return len(pipes) // 2

    def part_two(self, data):
        start = ('S', self.get_starting(data))
        edges = self._dfs(data, start)
        area = self.shoelace(edges)
        return self.picks(len(edges), area)

    def _dfs(self, data, start) -> list:
        steps = 0
        visited_pipes = set()
        visited_ordered = list()
        stack = deque([start])
        while stack:
            pipe = stack.pop()
            if pipe in visited_pipes:
                continue

            steps += 1
            visited_ordered.append(pipe)
            visited_pipes.add(pipe)
            stack.extend(self.get_connections(data, *pipe))

        return [v[1] for v in visited_ordered]

    def get_connections(self, data, pipe, idx):
        offsets = self.pipe_map[pipe]
        connections = []
        for offset in offsets:
            n_idx = (offset[0] + idx[0], offset[1] + idx[1])
            if not (0 <= n_idx[0] < self.rows and 0 <= n_idx[1] < self.cols):
                continue

            n_pipe = (data[n_idx[0]][n_idx[1]], n_idx)
            if tuple(-i for i in offset) in self.pipe_map.get(n_pipe[0], []):
                connections.append(n_pipe)
        return connections

    @staticmethod
    def shoelace(edges) -> float:
        sum1 = 0
        sum2 = 0
        n = len(edges)
        for i in range(n - 1):
            sum1 += edges[i][0] * edges[i + 1][1]
            sum2 += edges[i][1] * edges[i + 1][0]

        sum1 += edges[n - 1][0] * edges[0][1]
        sum2 += edges[n - 1][1] * edges[0][0]

        area = (sum1 - sum2) // 2
        return abs(area)

    @staticmethod
    def picks(b_points, area):
        i_points = area - (b_points // 2) + 1
        return i_points

    @staticmethod
    def get_starting(data) -> tuple[int, int]:
        for i, line in enumerate(data):
            j = line.find('S')
            if j != -1:
                return i, j


solver = Solution()
solver.solve()

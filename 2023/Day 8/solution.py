#
# Day 8: Haunted Wasteland
#
from math import lcm


class Solution:
    def solve(self):
        with open('input.txt', 'r') as f:
            data = f.read()
            print(f"{self.part_one(data)=}")
            print(f"{self.part_two(data)=}")

    def part_one(self, data, start='AAA'):
        instructions, graph = self.parse_input(data)
        return self.count_steps(graph, start, instructions)

    def part_two(self, data):
        instructions, graph = self.parse_input(data)
        starts = [node for node in graph.keys() if node.endswith('A')]

        return self.lcm_based(graph, starts, instructions)

    @staticmethod
    def parse_input(data):
        instructions, graph = data.split('\n\n')
        graph = [g.split('=') for g in graph.split('\n')]
        graph = {edge[0].strip(): [
            child.strip() for child in edge[1].strip('( )').split(',')
        ]
            for edge in graph
        }
        return instructions, graph

    @staticmethod
    def count_steps(graph, cur, directions):
        steps = 0
        direction_index = {'L': 0, 'R': 1}

        while not cur.endswith('Z'):
            d_index = steps % len(directions)
            instruction = direction_index[directions[d_index]]
            cur = graph[cur][instruction]
            steps += 1
        return steps

    @staticmethod
    def brute_force(graph: dict, starts: list[str], directions: str):
        steps = 0
        direction_index = {'L': 0, 'R': 1}
        curs = starts
        visited = set()

        while True:
            for index, direction in enumerate(directions):
                state = (tuple(curs), direction, index)
                if state in visited:
                    return None

                steps += 1
                visited.add(state)
                next_curs = [graph[cur][direction_index[direction]] for cur in curs]

                if all(cur.endswith('Z') for cur in next_curs):
                    return steps
                curs = next_curs

    def lcm_based(self, graph, starts, instructions):
        return lcm(*[self.count_steps(graph, cur, instructions) for cur in starts])


solver = Solution()
solver.solve()

#
# Day 5: If You Give A Seed A Fertilizer
#
#

class Solution:
    @staticmethod
    def part_one(maps):
        seed_to_location = {seed: seed for seed in map(int, maps[0].split(':')[1].strip().split())}

        for mapping in maps[1:]:
            mapping = mapping.split(':')[1].strip()
            mapping = [list(map(int, line.split())) for line in mapping.split('\n')]

            for seed, value in seed_to_location.items():
                for r in mapping:
                    des, src, length = r
                    if value in range(src, src + length):
                        seed_to_location[seed] = des + (value - src)
        return min(seed_to_location.values())

    @staticmethod
    def part_two(data):
        maps = [list(map(lambda rn: list(map(int, rn.split())), section.split('\n')[1:])) for section in data[1:]]

        seeds = list(map(int, data[0].split(':')[1].strip().split()))
        seed_paris = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]
        location = []

        for pair in seed_paris:
            remain = [pair]
            result = []

            for _map in maps:
                while remain:
                    cur = remain.pop()
                    for des, src, rng in _map:
                        if cur[1] < src or cur[0] >= src + rng:  # x-y-a-b or  a-b-x-y
                            continue
                        elif src <= cur[0] <= cur[1] < src + rng:  # a-x-y-b
                            result.append((des + cur[0] - src, des + cur[0] - src + cur[1] - cur[0]))
                            break
                        elif cur[0] < src <= src + rng <= cur[1]:  # x-a-b-y
                            result.append((des, des + rng - 1))
                            remain.append((cur[0], src - 1))
                            remain.append((src + rng, cur[1]))
                            break
                        elif cur[0] < src <= cur[1] < src + rng:  # x-a-y-b
                            result.append((des, des + cur[1] - src))
                            remain.append((cur[0], src - 1))
                            break
                        elif src < cur[0] <= src + rng <= cur[1]:  # a-x-b-y
                            result.append((des + cur[0] - src, des + rng - 1))
                            remain.append((src + rng, cur[1]))
                            break
                    else:
                        result.append(cur)
                remain = result
                result = []

            location.extend(remain)
        return min([i[0] for i in location])

    def solve(self):
        with open('input.txt', 'r') as f:
            data = f.read()
            maps = data.split('\n\n')
            print(f"{self.part_one(maps)=}")
            print(f"{self.part_two(maps)=}")


solver = Solution()
solver.solve()

class Solution:

    @staticmethod
    def part_one(lines: list[str]):
        points = 0
        for line in lines:
            winning, yours = line.split(':')[1].split('|')
            winning = set(winning.split())
            yours = set(yours.split())

            """
            using maps: 
            winning, yours = map(set, map(str.split, line.split(':')[1].split('|')))
                                    OR   
            winning, yours = map(lambda n: set(n.split()), line.split(':')[1].split('|'))
            """

            points += int(2 ** (len(winning & yours) - 1))
        return points

    @staticmethod
    def part_two(lines: list[str]):
        cards = [1] * len(lines)

        for i, line in enumerate(lines):
            winning, yours = map(set, map(str.split, line.split(':')[1].split('|')))
            matching = len(winning & yours)

            for j in range(1, matching + 1):
                # Add the number of previous card to the cards below to count for all instances
                cards[i + j] += cards[i]
        return sum(cards)

    def solve(self):
        with open('input.txt', 'r') as f:
            data = f.read().split('\n')
            print(f"Part one solution = {self.part_one(data)}")
            print(f"Part two solution = {self.part_two(data)}")


solver = Solution()
solver.solve()

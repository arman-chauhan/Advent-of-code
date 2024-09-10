#
#  Day 9: Mirage Maintenance
#


class Solution:
    def solve(self):
        with open("input.txt", "r") as f:
            data = f.read()
            data = self.parse_data(data)
            print(f"{self.part_one(data)=}")
            print(f"{self.part_two(data)=}")

    def part_one(self, data):
        values_sum = 0
        for history in data:
            sub_sequences = self.find_sub_seqs(history)
            values_sum += self.predict(sub_sequences, -1)
        return values_sum

    def part_two(self, data):
        values_sum = 0
        for history in data:
            sub_seqs = self.find_sub_seqs(history)
            first_value = self.predict(sub_seqs, 0)
            values_sum += first_value
        return values_sum

    @staticmethod
    def find_sub_seqs(sequence: list[int]) -> list[list[int]]:
        values: list[list[int]] = [sequence]
        while True:
            differences = [j - i for i, j in zip(sequence, sequence[1::])]
            sequence = differences
            values.append(sequence)
            if all(diff == 0 for diff in differences):
                break
        return values

    @staticmethod
    def predict(sub_seqs, idx):
        v = 0
        for sub_seq in sub_seqs[::-1]:
            v = sub_seq[idx] + v * (-1) ** (idx + 1)
        return v

    @staticmethod
    def parse_data(data):
        data = data.strip().split("\n")
        data = [[int(value) for value in line.split()] for line in data]
        return data


solver = Solution()
solver.solve()

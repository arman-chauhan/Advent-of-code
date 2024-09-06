#
# Day 7: Camel Cards
#


class Solution:

    def part_one(self, data):
        hands = [line.split() for line in data.split('\n')]
        hands = [(self.label(hand[0]), int(hand[1]), self.hand_type(hand[0])) for hand in hands]
        hands = sorted(hands, key=lambda h: (h[2], h[0]))

        return sum([hand[1] * (i + 1) for i, hand in enumerate(hands)])

    def part_two(self, data):
        hands = [line.split() for line in data.split('\n')]
        hands = [
            (self.label(hand[0], wildcard=True), int(hand[1]), self.hand_type(hand[0], wildcard=True))
            for hand in hands
        ]
        hands = sorted(hands, key=lambda h: (h[2], h[0]))

        return sum([hand[1] * (i + 1) for i, hand in enumerate(hands)])

    @staticmethod
    def label(hand, wildcard=False):
        to_num = {
            'T': 10,
            'J': 1 if wildcard else 11,
            'Q': 12,
            'K': 13,
            'A': 14
        }
        return [int(to_num.get(i, i)) for i in hand]

    @staticmethod
    def hand_type(hand: str, wildcard=False):
        types = {
            50: "Five of a kind",
            41: "Four of a kind",
            32: "Full house",
            31: "Three of a kind",
            22: "Two pair",
            21: "One pair",
            11: "High card"
        }

        jokers = 0
        if wildcard:
            jokers = hand.count('J')
            hand = [card for card in hand if card != 'J']

        counter = {}
        for card in hand:
            counter[card] = hand.count(card)
        f, s = (sorted(counter.values(), reverse=True) + [0] * 5)[0:2]
        score = (int(f) + jokers) * 10 + int(s)
        return score

    def solve(self):
        with open('input.txt', 'r') as f:
            data = f.read()
            print(f"{self.part_one(data)=}")
            print(f"{self.part_two(data)=}")


solver = Solution()
solver.solve()

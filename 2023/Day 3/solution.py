#
# Day 3: Gear Ratios
#

# Solution assumes a number must fit into a line, it should not overflow into other at the edge

cum = 0  # Sum is reserved so cum

gear: dict[tuple, list] = {}
gear_sum = 0


def main():
    with open('input.txt') as file:
        schema = file.read()
        lines = schema.split('\n')

        for i, line in enumerate(lines):
            j = 0
            while j < len(line):
                if line[j].isdigit():
                    number = consume_number(line, j)
                    check_symbol(lines, i, j, number)
                    j += len(number)
                    continue
                j += 1


def consume_number(line, j):
    number = ''

    while line[j].isdigit():
        number += line[j]
        j += 1
        if j >= len(line):
            break
    return number


# Scan all the elements around the number
def check_symbol(lines, row, col, number):
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 1 + len(number)):
            if (i < 0 or i >= len(lines)) or (j < 0 or j >= len(lines[i])):
                continue

            if lines[i][j] == '*':
                if (i, j) not in gear:
                    gear[(i, j)] = []
                gear[(i, j)].append(int(number))

            if not lines[i][j].isdigit() and not lines[i][j] == '.':
                global cum
                cum += int(number)
                continue


if __name__ == '__main__':
    main()

    gear_sum = 0
    for gear, nums in gear.items():
        if len(nums) == 2:
            gear_ratio = nums[0] * nums[1]
            gear_sum += gear_ratio

    print(cum)
    print(gear_sum)

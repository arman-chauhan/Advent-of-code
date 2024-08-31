def main():
    sol = 0
    with open('input.txt', 'r') as file:
        for line in file:
            cur = []
            for i, c in enumerate(line):
                if c.isdigit():
                    cur.append(c)
                for j, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                    if line[i:].startswith(val):
                        cur.append(str(j + 1))

            sol += int(cur[0] + cur[-1])
    print(sol)


# Solutions
# part 1 : 54951
# part 2 : 55218

if __name__ == '__main__':
    main()

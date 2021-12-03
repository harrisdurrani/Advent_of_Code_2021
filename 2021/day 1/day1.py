def part_one():
    tally = 0
    with open("input.txt") as input:
        read_data = input.read().split("\n")
        for i, j in zip(read_data, read_data[1:]):
            if int(j) > int(i):
                tally += 1
    print(tally)


def part_two():
    tally = 0
    with open("input.txt") as input:
        read_data = input.read().split("\n")
        for i, j in zip(read_data, read_data[3:]):
            if int(j) > int(i):
                tally += 1
    print(tally)
part_two()
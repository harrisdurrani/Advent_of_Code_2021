def part_one():
    forward = 0
    dept = 0
    with open("input.txt", "r") as input:
        read_data = input.read().split("\n")
    
    for i in read_data:
        cords = i.split()
        if cords[0] == "forward":
            forward += int(cords[1])
        elif cords[0] == "down":
            dept += int(cords[1])
        elif cords[0] == "up":
            dept -= int(cords[1])
    print(forward * dept)

def part_two():
    forward = 0
    dept = 0
    aim = 0
    with open("input.txt", "r") as input:
        read_data = input.read().split("\n")
    
    for i in read_data:
        cords = i.split()
        if cords[0] == "forward":
            forward += int(cords[1])
            dept += aim * int(cords[1])
        elif cords[0] == "down":
            aim += int(cords[1])
        elif cords[0] == "up":
            aim -= int(cords[1])
    print(forward * dept)

part_two()

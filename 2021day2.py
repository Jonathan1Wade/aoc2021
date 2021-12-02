#part1
with open("2021day2.txt") as f:
    lines = f.readlines()

depth = 0
forward = 0

for line in lines:
    key, value = line.split(" ")

    if key == "up":
        depth -= int(value) 
    elif key == "down":
        depth += int(value)
    elif key == "forward":
        forward += int(value)
print(depth, forward)
print(depth * forward)


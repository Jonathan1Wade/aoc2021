#part 2
with open("2021day2.txt") as f:
    lines = f.readlines()
    #print(lines)

depth = 0
forward = 0
aim = 0

for line in lines:
    key, value = line.split(" ")
    #print(key, value)

    if key == "up":
        #depth -= int(value)
        aim -= int(value)
    elif key == "down":
        #depth += int(value)
        aim += int(value)
    elif key == "forward":
        forward += int(value)
        depth += (int(value) * aim)

print(depth * forward)

    
      
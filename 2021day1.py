print('solution 1\n')
with open("2021day1.txt") as f:
    input = [int(l) for l in f.readlines()]
    #print(input)

changes = 0 

for (a, b) in zip(input[:-1], input[1:]):
    if a < b: 
        changes += 1
print(changes)


def sliding_window(elements, window_size):
    if len(elements) == window_size:
        return elements
    for i in range(len(elements) - window_size + 1):
        print(elements[i:i+window_size])
sliding_window(input, 3)





 


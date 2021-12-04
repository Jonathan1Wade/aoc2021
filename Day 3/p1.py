with open('input.txt') as f:             # open file
    content = f.read().splitlines()         # read file and split lines 

gamma = ""                                  # empty string. We will use this to disply the result, it needs to start empty "".
ep = ""                                     # empty string

for index, item in enumerate(content[0]):   # enumerate is a function that returns a tuple containing a count (index) and the value of the item.  We need to know the length so we can loop through eqach digit. 
    g = 0                                   # set g to 0. We need these to count how many times a digit appears in the string.
    h = 0                                   # set h to 0
    for line in content:                    # loop through each line in the file
        value = list(line)[index]           # get the value of the character at index. This loop allows us to start at postion 0 and go to the end of the string for every line (line in content). Again ot e we read right to left so we start at postion 0 and keep going, this is the length of the index we defined.  
        if (value=="1"):          
            g+=1
        else:
            h+=1
    if (g>h):
        gamma+="1"
        ep+="0"       
    else:
        gamma+="0"
        ep+="1" 
        
print("gamma", gamma, int(gamma,2))         # print the binary string and the integer value
print("epsilon", ep, int(ep,2))          
print("power =", int(gamma,2)*int(ep,2))    # print the product of the two binary strings

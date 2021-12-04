with open('2021day3.txt') as f:   # open file
  content = f.read().splitlines()            # read file

gamma=""
ep=""

for index in range(len(content[0])):  
    g=0
    h=0
    for index in content:
        value = list(line)[index]
        if (value=="1"):
            g+=1
        else:
            h+=1
    if (g>h): 
        gamma+="1"
    else:
        gamma+="0"

print(gamma)         

#for index in range(len(lines[0])):
#    ones = 0
#    zeros = 0
#    for line in lines: 
#        value = list(line)[index]
 #       if (value=="1"):
  #          ones+=1
  #      else:
  #          zeros+=1
   # if (ones>zeros):
   #     gamma+="1"
   #     epsilon+="0"
    #else:
    #    gamma+="0" 
    #    epsilon+="1"




    #num =[(1 if x == '1' else -1) for x in list]
    #for i,b in enumerate(num):
      # range[i] += b

#gamma = ['0' if x < 0 else '1' for x in range]  # convert the list to a string of 0s and 1s
#epsil = ['0' if x > 0 else '1' for x in range]    # convert the list to a string of 0s and 1s

#gamma = int(''.join(gamma), 2) # convert the string to an integer
#epsil = int(''.join(epsil), 2) # convert the string to an integer

#print(gamma * epsil)   # print the integers
    

#g = [0] * 12    # g is a list of 12 zeros
#for entry in updatedList:   # for each entry in the list
    #num = [(1 if x == '1' else -1) for x in entry]  # convert the string to a list of 1s and -1s


      # for each number in the list
       # g[i] += b   # add the number to the corresponding index in g
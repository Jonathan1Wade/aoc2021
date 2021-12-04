with open('input.txt') as f:             
    content = f.read().splitlines()         

gamma = ""                                  
ep = ""                                     

for index, item in enumerate(content[0]):   
    g = 0
    g_list =[]                              
    h = 0
    h_list = []                                  
    for line in content:                    
        value = list(line)[index]             
        if (value=="1"):          
            g+=1
            g_list.append(line)
        else:
            h+=1
            h_list.append(line)
    if (g>h):
        gamma+="1"
        ep+="0"       
    else:
        gamma+="0"
        ep+="1" 
        
print(h_list)
#print("gamma", gamma, int(gamma,2))         
#print("epsilon", ep, int(ep,2))          
#print("power =", int(gamma,2)*int(ep,2))    

import random

dcount = input(str("Enter Die count and number: "))

n = dcount.split("d")

def dice(l:list)-> int:
    z = 0
    for x in range(1,int(l[0])+1):
        #print(x)
        y = random.randrange(1,int(l[1])+1)
        #print (y)
        z += y
    return "You rolled "+str(l[0])+" dice with "+str(l[1])+ " sides and the sum is "+str(z)
print(dice(n))
        

n =[0,1,0,3,12]
for i in n:
    if i == 0:
        n.remove(i)
        n.append(i)
    
print(n)
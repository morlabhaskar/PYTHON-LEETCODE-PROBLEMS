n1 = [1,2,3,0,0,0]
m = 3
n2 = [2,5,6]
n = 3

l =[]
l1 =[]
c1 = len(n1)
c2 = len(n2)
for i in n1:
    if i == 0:
        continue
    else:
        l.append(i)

for j in n2:
    if j == 0:
        continue
    else:
        l1.append(j)
b = l + l1
b.sort()
print(b)
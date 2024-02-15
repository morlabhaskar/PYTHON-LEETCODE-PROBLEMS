digits = [1,2,3,4]
x = 0
for i in range(len(digits)):
    x = x * 10 + digits[i]
x = x + 1
a = str(x)
        
n = []
for j in range(len(a)):
    l = x % 10
    x = x // 10
    n.append(l)
            
m = []
for k in range(-1,-len(n)-1,-1):
    m.append(n[k])
print(m)              
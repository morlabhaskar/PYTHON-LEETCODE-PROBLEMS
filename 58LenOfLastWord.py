s = "bhaskar is a good boy"
a = 0
b = 0
for i in range(len(s)-1,-1,-1):
    if s[i] != ' ' and (i == 0 or s[i-1] == ' '):
        a = i
        print(a)
        break

for i in range(len(s)-1,-1,-1):
    if s[i] != ' ':
        b = i
        print(b)
        break
                
print(b - a+1)               
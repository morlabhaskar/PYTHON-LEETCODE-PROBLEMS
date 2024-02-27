s = "Let's take LeetCode contest"
x = s.split(" ")
a = list(x)
l = ""
for i in a:
    r = i[::-1] + " "
    l = l + r
l = l.strip()
print(l)
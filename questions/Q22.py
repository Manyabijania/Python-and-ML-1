n = int(input("how many elements do you want to enter?"))
l = []
for i in range(0, n):
    x = int(input("enter the element:"))
    l.append(x)
m = l[0]
n = l[0]
for x in l:
    if m < x:
        m = x
for x in l:
    if n > x:
        n = x
print("max no=", m)
print("min no=", n)


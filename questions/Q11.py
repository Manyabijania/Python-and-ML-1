n = int(input("Enter the number of terms:"))
x = 0
y = 1
nextnumber = y
count = 1

while count <= n:
    print(nextnumber, end=" ")
    count += 1
    x, y = y, nextnumber
    nextnumber = x + y
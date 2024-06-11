lines = []
line = ''
while True:
    line = str(input("Enter line:"))
    if line:
        lines.append(line)
    else:
        break
for i in lines:
    print(i)

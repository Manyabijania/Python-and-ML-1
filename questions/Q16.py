s=str(input("Enter a string:"))
s1=''
for y in s:
    if y not in s1:
        s1 += y
for x in s1:
    count=0
    for i in range(0, len(s)):
        if x == s[i]:
            count += 1
    print("the frequency of", x, "is:", count)

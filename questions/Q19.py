s = str(input("enter  a string:"))
s1=''
for i in s:
    if 65<= ord(i) <= 90 or 97<= ord(i) <= 122 or i==" ":
        s1+=i
    else:
        s1+=" "
print(s1)
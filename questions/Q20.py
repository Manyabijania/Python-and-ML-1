s=str(input("Enter the numbers with spaces:"))
l=list(s.split(" "))
sum=0
for i in l:
    sum+=int(i)
print("the sum  is :",sum)
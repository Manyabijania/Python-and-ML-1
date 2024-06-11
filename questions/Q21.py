n=int(input("how many elements do you want to enter?"))
l=[]
for i in range(0,n):
    x=str(input("enter the element:"))
    l.append(x)
n1=str(input("enter the element whose frequency of occurrence you want:"))
print("The frequency of", n1, "is:", l.count(n1))
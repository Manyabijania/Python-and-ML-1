print("1:Celsius to Fahrenheit\n2:Fahrenheit to Celsius")
n=int(input("from the menu enter the number as per the conversion you want:"))
if n==1:
    c=float(input("enter temp in celsius:"))
    f=c*(9/5)+32
    print("Temp in fahrenheit is:",f)
elif n==2:
    f = float(input("enter temp in fahrenheit:"))
    c=(f-32)*5/9
    print("Temp in celsius is:", c)
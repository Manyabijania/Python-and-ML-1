a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
n=str(input("enter the operator from (+,-,*,/):"))
if n == '+':
    print("the sum is:",a+b)
elif n == '-':
    print("the subtraction is:",a-b)
elif n == '*':
    print("the multiplication is:",a*b)
elif n == '/':
    print("The division is:",a/b)
else:
    print("wrong operator entered")

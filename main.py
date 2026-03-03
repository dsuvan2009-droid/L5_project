a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
if a>b and a>c:
    print("The suitable temperature for wearing light clothes is: ",a)
elif b>a and b>c:
    print("The suitable temperature for wearing light clothes is: ",b)
else:
    print("The suitable temperature for wearing light clothes is: ",c)
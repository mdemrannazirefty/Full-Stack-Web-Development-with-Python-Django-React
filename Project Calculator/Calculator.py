# Calculator Project
x=int(input("Enter YOur First Number: "))
operator=input("Operation: ")
y=int(input("Enter Your Second Number: "))

if operator=='+':
    result=(x+y)
    print("Ans is: ",result,)
elif operator=='-':
    result=(x-y)
    print("Ans is: ",result,)
elif operator=='/':
    if y!=0:
        result=(x/y)
        print("Ans is: ",result,)
    else:
        print("error")      
elif operator=='*':
    result=(x*y)
    print("Ans is: ",result,)
else:
    print("Invalid input")



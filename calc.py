
    
def addition(num1,num2):
    return num1 +  num2
def subtraction(num1,num2):
    return num1- num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    if num2!=0:
        return num1/num2
    else:
        print("ERROR!!!")
def remainder(num1,num2):
    return num1%num2
def exponential(num1,num2):
    return num1**num2 
def floordivivsion(num1,num2):
    return num1//num2
print("Enter a Math Function")
print("a.Addition")
print("b.Subration")
print("c.Multiplication")
print("d.Division")
print("e.Remainder")
print("f.Exponential")
print("g.Floor remainder")
oprt=input("Choose (a/b/c/d/e/f/g)")  
    
num1=int(input("Enter a number"))
num2=int(input("Enter another number"))

if oprt =='a':
    print("The sum is ", addition(num1,num2))
elif oprt =='b':
    print("The subtration is ", subtraction(num1,num2))
elif oprt =='c':
    print("The product is ", multiplication(num1,num2))
elif oprt =='d':
    print("The division is ", division(num1,num2))
elif oprt =='e':
    print("The remainder is ", remainder(num1,num2))        
elif oprt =='f':
    print("The Exponential is ", exponential(num1,num2))
elif oprt =='g':
    print("The floor division is ", floordivivsion(num1,num2))    
else:
    print("!!! Invalid !!! INVALID !!!")

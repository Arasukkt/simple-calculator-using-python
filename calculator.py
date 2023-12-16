num1=int(input("enter the num  : "))
num2=int(input("enter the another number : "))
operator=input("enter the operator :")
if operator !=('+','-','/','*'):
    print("enter the valid operator")
if (num1 and num2)==0:
    print("enter valid number : ")
def add():
    add1=num1+num2
    return add1
def sub():
    sub1=num1-num2
    return sub1
def multi():
    multi1=num1*num2
    return multi1
def div():
    div1=num1/num2
    return div1
if operator=='+':
    print("addition of these two value is : ",add())
elif operator=='-':
    print("subraction of these two value is : ",sub())
elif operator=='*':
    print(multi()) 
elif operator=='/':
    print(div())
else:
    print("enter valid operator")


num1=int(input("enter the num  : "))
num2=int(input("enter the another number : "))
operator=input("enter the operator :")
if operator !=('+','-','/','*'):
    print("enter the correct operator")
if (num1 and num2)==0:
    print("enter valid number : ")
def add():
    add1=num1+num2
    return add1
def sub():
    sub1=num1-num2
    return sub1
def multi():
    multi1=num1*num2
    return multi1
def div():
    div1=num1/num2
    return div1
if operator=='+':
    print("addition of these two value is : ",add())
elif operator=='-':
    print("subraction of these two value is : ",sub())
elif operator=='*':
    print(multi()) 
elif operator=='/':
    print(div())
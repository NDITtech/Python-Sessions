#Providing Function Definition
def sum(x, y):
    "Going to add x and y"
    result=x+y
    print ("Sum of two numbers is", result)
sum(10, 23)
sum(111, 845)





def sub(x,y):

    subtraction=x-y
    print(subtraction)

sub(6,3)


def addition(x, y):
    print(x + y)


a = 15
addition(15, 10) or addition(a, 10)


def mul(a,b):
    print(a*b)
mul(3,8)

def suma(a, b):
    "Function having two parameters"
    result=a+b
    print(result)
suma(88,4)


def msg(id, name, age=18):
    "Printing the passed value"
    print(id)
    print(name)
    print(age)
    return id,name,age




# Function call
msg(100,'ravff')

print('-------------------')
def msg(id, name, x=10, y=20):

    "Printing passed value"
    print(id)
    print(name)
    return msg

msg(10, 'raj')
msg(id=10, name='Raj')




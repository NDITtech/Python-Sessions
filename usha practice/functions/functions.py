#functions
#in functions two types are there
#1.Built in functions
#2.User defined functions
#here are user defined function
#for user defined functins we use def key word
#syntax is:def function_name(perameters)
def adding(x,y):
    z=x+y
    return z
n=adding(10,20)
print(n)
def calculate_tx(amount):
    return amount*0.18

tax_case1 = calculate_tx(10000)
print(tax_case1)

tax_ccase2 = calculate_tx(500000)
print(tax_ccase2)


def new_fun():
    x = 10
    y = 20
    z =x+y
    print(z)


new_fun()

print("---example2-------")

def add_numbers(a,b):
    result = a+b
    print(result)

add_numbers(10,50)

print("----return-------")
def add_numbers(a,b):
    result = a+b
    return result
x = add_numbers(23,66)
print(x)






print("---------------")

def average(a,b):
    return (a+b)/2
print(average(30,60))
x = average(30,60)
print(x)
print("or----------------")
print(average(30,60))


print("math ops-----")
def math_operations(x,y):#here x,y are perameters
    add = x+y
    sub = x-y
    mul = x*y
    return add, sub, mul

p,q,r = math_operations(10,5)#positional arguments
print(p,q,r)
print("---------------")

m = math_operations(10,5)
print(m)

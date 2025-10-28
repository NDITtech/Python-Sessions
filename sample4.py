print("sample4")

#user defined functions
'''
def calculate_tx(amount):
    return amount*0.18

tax_case1 = calculate_tx(10000)
print(tax_case1)

tax_ccase2 = calculate_tx(500000)
print(tax_ccase2)

def dep():
    a=1
    b=7
    r=a+b
    print(r)
dep()



print("math ops-----")
def math_operations(x,y):
    add = x+y
    sub = x-y
    mul = x*y
    return add, sub,mul

a,b,c = math_operations(10,5)
print(a,b,c)

m = math_operations(10,5)
print((m))
'''

'''
def add(a,b):
    add = a+b
    return add
a=2
b=4
#int[add] = (a+b)
c= add(2,4)
print((c))

#2nd method
def add(a,b):
    return a+b
print(add(3,4))

def greet():
    print('hello program')
greet()
#find the even numbers
def is_even(n):
    return n % 2 == 0
print(is_even(3))
print(is_even(6))
'''

def sum_of_list(numbers):
     total=0
     for n in numbers:
      total += n
     return total
x=sum_of_list([1,1,2,3])
#print(sum_of_list([2,3,6,7]))
print(x)




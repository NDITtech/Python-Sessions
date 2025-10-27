
'''
def display():
    def message():
        return "Hello "
    return message

fun=display()
print(fun())
   

l=lambda a,b:a+b
print(l(10,20))


def cube(n):
    return n**3

print(cube(2))


x=123

def display():
    x=678
    print(x)
    print(globals()['x'])

print(x)
z = display
z()


'''
from FUnctions.factorial import factorial


#Keyword  Arguments

def func(x,y, *args):
    print("positiional arguments", x)
    print("positiional arguments", y)
    print("keyword arguments : ", *args)
func(3,5,66,7,3,3,6,6,57,7,8,9,0)

print("------------------")

def find_sum(*args):
    print(args)
    return sum(args)
print(find_sum(55,77,3,3,3,9))

#**kwargs



def func(x, *args,**kwargs):
    print("positiional arguments", x)
    #print("positiional arguments", y)
    print("keyword arguments : ", *args)
    print("**kwargs",kwargs)
func(3,5,66,7,3,3,6,6,57,7,8,9,0,name="Naveen", id=45, sal=100)



print("------+00000000000000000000000000")

def fun(**kwargs):
    print(kwargs)

fun(name="naveen", sal=50)


print("recursive function")
#recursive function
#factorial of 3 = 3*2*1
# factorial of 3 = 3*facorial(2)  # 3*2*1
#factoral of 1 = 1 * factorail(0)
#factorial of 0 = 1

#factorial of 3 = 3*facorial(2)  # 3*2*1
#factorial of n = n*factorail(n-1)


def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print("this line executed")
print(factorial(5))  #5*4*3*2*1


def sum_numbers(n):
    if n==0:
        return 0
    else:
        return n+sum_numbers((n-1))

print(sum_numbers(5)) #1+2+3+4+5
print(sum_numbers(555))


#Debugging

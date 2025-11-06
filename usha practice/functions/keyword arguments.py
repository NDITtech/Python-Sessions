#in this we can pass many number of arguments these are also called named arguments
#*args
#**kwargs
def fun(x, *args):  # *args will allow us 'n' number of positional arguments
    print(x)
    print(*args)
fun(10,25,35,66)

def find_sum(*args):
    print(args)
    return sum(args)
print(find_sum(55,77,3,3,3,9))


def func(x,y, *args):
    print("positiional arguments", x)
    print("positiional arguments", y)
    print("keyword arguments : ", *args)
func(3,5,66,7,3,3,6,6,57,7,8,9,0)

#**kwargs : keyword arguments: (Variable-Length Keyword Arguments (**kwargs))
#this is like key value pair
#Used when you don’t know the number of keyword arguments beforehand.

def func(x, *args,**kwargs):
    print("positiional arguments", x)
    #print("positiional arguments", y)
    print("keyword arguments : ", *args)
    print("**kwargs",kwargs)
func(3,5,66,7,3,3,6,6,57,7,8,9,0,name="Naveen", id=45, sal=100)



print("------+00000000000000000000000000")

def fun(**kwargs):
    print(kwargs)

fun(name="usha", sal=5000)


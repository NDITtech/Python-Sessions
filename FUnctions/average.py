def average_1(a,b):
    #print(a)
    #print(b)
    return (a+b)/2

print(average_1(1,5))
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result

print(factorial(7))
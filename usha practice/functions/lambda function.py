#lambda function
#A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression
a=23
b=90
c=78
d=76
e=4
sum=lambda a,b,c,d,e:a+b+c+d+e
print("total marks of a class",sum(a,b,c,d,e))

ages = [12, 18, 25, 7, 30]
adult_ages = list(filter(lambda age: age >= 18, ages))
print(adult_ages) # Output: [18, 25, 30]
#Python is dynamically typed, so no need to define the type of variable
'''
Variable Rules:
Must start with a letter or underscore (_)
Can contain letters, numbers, and underscores
Cannot start with a number
Case-sensitive (Apple and apple are different)
'''
x = 10
print(x)

x = 10 # intergers
y= "apple"  #string


name = "naveen"
_age = 30

#1sal = 1000 # wrong  #

#case sensitive
#name
#Name
#NAME


a = [1,2,3,4,5]
print(a)
b = a
print(b)

b.append(6)
print(b)


x = 5
print(x)
x = "ice"
print(x)


# multiple variables at once
x, y = 1,2
print(x)
print(y)

a,b,c,d = 4,7,9,4
print(c)

print("--------------")
#same value to multiple variables
a=b=c=d=5
print(d)


x, y, z = "how", "are", "you"
print(y)

x=y=z= "Hello"
print(x)




x = "are"
y = "you"
z = "   there"
print(x,y,z)


x = 10
y = 6
print(x+y)

x = 6
y = "Hello"
print(x,y)


#we do not use the keywords as variable names
#if= 10 #error

#while = "name"   #error
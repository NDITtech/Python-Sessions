#Numeric Data types

#integers - positive, negative, zero
x = 10
y = -20
z = 0

print(type(x))
print(type(z))

#float
x = 3.4555
print(type(x))

salary = -5.25343
print(type(salary))

#complex
z = 4+7j

print(type(z))






print("---------------------")
#2. Text type
#string
name = "python"
print(name)
print(type(name))

p = 'Hello'
print(type(p))

q = '''This is python'''

print(type(q))


print("----Boolean type-----")
#True
#False
True == 1
False == 0


a = 10
b = 20
result= a<b
print(result)

print(type(result))
print(bool(1))
print(bool(0))


print("---3. Sequence types----------")
#List
#Tuple
#range

#[] or list()

numbers = [1,3,4,5,6,7,8]
print(numbers)
print(type(numbers))

fruits = ["banana", "apple", " guava"]

mixed = [1,2,"Hello", 3.7, True]
print(type(mixed))

emp = []
print(type(emp))

let = list("abcd")
print(let)
intt = list((1,2,3,4,5))
print(intt)
print(type(intt))



numbers = [1,3,4,5,6,6,6,6,6,7,7,8]
print(numbers)


#mutable example
emp = ["naveen", 15, "Data enginner"]
print(emp)
emp[1] = 25
print(emp)


#Tuple
#()


p = (1,"apple", 6.9 )
print(type(p))

q = ()
print(type(q))
print("--------------")
r = (6)
print(r)
print(type(r))

m = (6,)
print(m)
print(type(m))

list_x = [1,2,3,45,5,6]
print("listvalues", list_x)


tuple_x = tuple(list_x)
print(tuple_x)
print(type(tuple_x))


#immutable example

emp = ("naveen", 15, "Data enginner")
print(emp)
#emp[1] = 25
print(emp)



print("---range--------")
#range

p = range(6)
print(p)
print(list(p))

#range([start],stop,[step])
for i in range(2,15,3):
    print(i)


#set data types
#set - unique, mutable
#frozen set - unique, immutable


languages = {"python", "java"}
print(languages)
print(type(languages))

languages.add("scala")
print(languages)

languages.remove("python")
print(languages)

num = set([1,2,3,45,6,7,8,8,8,7,8,6,6,6])
print(num)
print(type(num))




print("----------frozen-------")
languages1 = frozenset(["python", "java"])
print(languages1)
print(type(languages1))

#languages1.add("scala")  #error






print("--------------------------")

print("---line11")

print("-------------")
'''datatypes
int
float
string
complex
boolean'''
#Datastructures
'''list[]
tuple()
set{}
dictionary{}key value pair'''
#CRUD OPERATIONS ON DATATYPES AND DATASTRUCTURES
#APPEND
x=[1,2,3,4,5,6,7]
y=["chethan"]
print(x)
x.append(y)
print(x)
#extend
x=[1,2,3,4,5,6]
y=["chethan","Divyansh"]
x.extend(y)
print(x)
#clear
x=[1,2,3,4,5]
x.clear()
print(x)
#count
#it will count how many times the given value is repeated
x=[1,2,3,4,5,1,1,1,2,3,4,4]
print(x.count(4))
print(x.count(1))
x="sadhjsjdkjd"
print("count of",x.count("d"))
#copy
x=[1,23,3,4,2,3,4,2,3,346,565,656,6,5,6]
#y=x#shallow copy
y=x.copy()
print(y)
#index it will get index of give text or number
x=[1,2,3,4,5,6,4,4,3,5,6]
print(x.index(2))
print(x.index(3))
x=["s","dosa","sd"]
print("index of string",x.index("dosa"))
#insert will insert values based on index value
x=[1,2,3,4,5,6,7]
x.insert(6,"usha")
print(x)
#pop it will removes value based on index value
x=[1,2,3,4,5,6,7,8,9,10,11,12]
x.pop((10))
print(x)
#remove here we can remove the number that is only first number given
#by using loops we can remove repeating values
x = [1,3,4,5,6,7,8,1,1,1,2,3,4,4,4,4]
#    0 1 2 3 4 5 6 7 8 9 10
x.remove(1)
print("removing values",x)
print("pop:",x)

#remove
x = [1,3,4,5,6,"dev",7,8,1,1,1,2,3,4,"dev",4,4,4,2]
j=[]
for i in x:
    print(i)
    if i == "dev":
        continue
    elif i == 4:
        continue
    else:
        j.append(i)
print("remove:", j)

y = x
y.remove(7)

#x = [1,3,4,5,6,"dev",7,8,1,1,1,2,3,4,"dev",4,4,4,2]

#reverse
x = [1,3,4,5,6,"dev",7,8,1,1,1,2,3,4,"dev",4,4,4,2]
x.reverse()
print("reverse:",x)

#sort
x = [1,3,4,5,6,7,8,1,1,1,2,3,4,4,4,4,2]
x.sort()
print("sort:",x)
x=4
y=2
print("Adding two variables: ", x+y)

print("Substracting two variables: ", x-y)
print("Multification of two variables: ", x*y)
print("dividing of two variables: ", x/y)
print("modulus of two variables: ", x%y)
print("floor division of two variables: ", x//y)
print("spuare of two numbers",x**y) # 11*11
print(x==y)
print(x!=y)
print(x>=y)
print(x<=y)
print(x>10 and y>10)
print(x>10 or y>10)
print(not(x>10 or y>10))

print(x is y)

print(y in x)
print(y not in x)
#deep copy
a = [1, 2,3]
b = a.copy()
a.append(4)
print("deep copy",a)#[1, 2, 3, 4]
print("deep copy",b)#[1, 2, 3]

#swallow copy
# by using b= a
a = [1, 2, 3]
b = a
a.append(4)
print("swallow copy:",a)  # [1, 2, 3, 4]  #see the difference here by using b= a
print("swallow copy:",b)  # [1, 2, 3, 4]'''

'''
d = (1,2,3,4,5,6,7)
print("tuple:", d)


#count
d = (1,2,3,4,5,6,7,1,1)
print("count:", d.count(1))

#index
d = (2,3,4,5,6,7,1,1)
#    0 1 2 3 4 5 6 7
print("index num:", d.index(1))'''

'''
x = [1,3,4,5,6,7,8,1,1,1,2,3,4,4,4,4,2]

print(set(x))

d = {1,2,3,6,7}

#add
d.add(10)
d.add("naveen")
print("adding value to set:", d)'''

'''
#update
d = {1,"dev",2,3,6,7}
d.update([1,4,6,"dev","nav"])
print("updating the set:", d)

#remove
n = {1,"dev",2,3,6,7}
n.remove(3)
print("removing the value", n)

#union
d = {1,2,3,4}
n = {4,5,6,7}

print(d.union(n)) # 1,2,3,4,5
print(d.intersection(n)) #3, 4
print(d.difference(n))#1,2, 3
print(n.difference(d))#5,6,7
'''

d = {1:"dev",2:"naveen",3:"hari",4:"usha",5:"ashok",6:"dev"}

print(d.keys)
print(d.values())
print(d.get(3))
print(d.items())
d.popitem()
d.update({6:"nd it"})
s = d.pop(6)
print(s)
#print(d)
d.clear()
print(d)


y=98
print(y)

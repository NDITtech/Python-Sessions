'''
Variable Rules:
Must start with a letter or underscore (_)
Can contain letters, numbers, and underscores
Cannot start with a number
Case-sensitive (Apple and apple are different)
'''
#integr
a=10
print("a")
print(type(a))
print("----------")
#float
b=2.4
print(b)
print(type(b))
print( "----------")
#string
c="hello"
print(c)
print(type(c))
print("----------")
#Boolean
d=20
e=30
result=d>e
print(result)
print(type(result))
print("----------")
#list[]
#tuple()
#set{}
#dictionary{  } it stores key value pair
#we use these to store multiple value with single data type or multiple datatypes
# differences
#ordered
#11111
#list is ordered: in list position of data is fixed [1,2,3,4]the position of values are not changed
#tuple is also ordered
#set is not ordered
#dictionary is ordered
#22222222
#changable
#list is mutalbe: we can change values in list that is we can change 1 st value or second value and we can add or remove values
#tuple is immutable:we can not change values
#set is mutable :that we can only add or remove values in set and we can not change previously given values
#dictionary is mutalbe like set
#333333333
#indexed
#if anything is ordered it indexed alo
#set is indexed
#tuple is indexed
#set is not indexed
#dictionary is indexed
#4444444444
#allows Duplicates
#list allows duplicates
#tuple allows duplicates
#set not allows duplicates
#Dictionary not allows duplicates
print("example of lit ----------")
l=[1,2,3,4,5]
print(l)
print(type(l))
print("----------")
m=[1,2.1,"usha"]
print(m)
print("getting index of given value")
print(m.index(2.1))
print("----------")
print("changing value based on index ")
m[1]=6.5
print(m)
print("-----------")
print("adding value to list ")
m=[1,2.1,"usha"]
print("to add values to list we use apped function ")
m[1]=6.5
print(m)
m.append(6.5)
print(m)
print("--------------------")
print("by using list key word")
l=list((1,2,"usha",3.2))
print(l)
print(type(l))
print("-----------")
# allows duplicates
print("allow duplicates")
r=[1,2,2,2,2,3,1,4,3,3]
print(r)
# frozen set
# it wont allow any changes
print("frozen set")
j=frozenset([1,2,2,3,4,5,5,8])
print(j)
 #j.append(10)
print(j)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx")
#tuple
print("example of TUPLE---------")
t=(1,2,3,4)
print(t)
print(type(t))
print("-----------")
s=tuple(range(10))
print(s)
print(type(s))
print("-----------")
print("immutabl we can not change values")
#t(2)=6
#t.append(3)
print(t)
print("--------")
print("allow duplicates")
r=[1,2,2,2,2,3,1,4,3,3]
d=(1,1,2,3,3,3,34,4,34,2,23,23)

print("immutabl we can not change values")
print(t)
print(d)
print("indexed")
print("it will give first matched value index")
print(d.index(34))
print("changing list to tuple")
k=[1,2,3.4,4.2,5]
x=tuple(k)
print(x)
print(type(x))
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("example of set")
s={1,2,3,3.3,"usha"}
print(s)
print(type(s))
print("-----------")
#print(s.index("usha"))
# here it is not giving any index value
print("-----------")
print("adding values to set we use 'add' function")
s.add("kala")
print(s)
print("it wont allow duplicates")
s={1,2,2,2,2,3,4,4,5,5,5,6}
print(s)
print("in result it show only 1,2,3,,4,5,6")
#dictionary
print("dictionary")
x={"name":"usha","id":3,"salary":100000}
print(x)
print(type(x))
print("-----------")
print("not allow duplicates")
#z={"name":"usha","name"="raj"}
print("adding values to dictionary")
x["company"]="xxxxx"
print(x)
s=x.keys()
g=x.values()
print(x.keys())
print(x.values())
print(x.items())
print("getting keys using index value")
q=list(x.keys())
print(q[1])

#multiple variables
x,y=1,2
print(x)
print(y)
a,b,c,d="sreekanth","usha","chethan","divyansh"
print(a)
print(b)
print(c)
print(d)
x="how"
y="are"
z="you"
print(x,y,z)
x=23
y=67
print(x+y)
#we should not use key words as variables if we want to use keep _before key word
#if=12
   # print(if)
#it is showing error
#variable name start with_ or a small letters
_if=56
#comments
#single line comment with"#"symbol
'''multiline comment with
3 single quots'''
#or
"""multi line comment with 
3 double quotes"""
#python is case sensitive
#noneed to give datatype for variables
#datatypes
#integers

x=1
print(x)
#float
y=0.978
print(y)
z=-2
print(z)
print(type(x))
a=4+6j
print (type(a))
print(a)
#text type
#string
name="usha"
print(type(name))
#Boolean type
#true
#false
a=12
b=90
result=a>b
print(result)
print(type(result))
print(bool(1))
print(bool(0))
#sequence types
#[] or List
#[] or Tuple
#{}or Set
#Dictionary
#list
#it allows multiple and different values and it allows changes in values it is called as mutable
num=[1,2,3,4]
print(num)
print(type(num))
mixedvalues=[1,"usha",0.1,-27,True]
print(type(mixedvalues))
emp=[]
print(type(emp))
#converting string to list
let=list("fghhj")
print(let)
#converting tuple to list when we use brases it will automatically
#assumes list ,tuple,stringbased onntype of brases we used
u=list((1,2,3,4,5,6))
print(u)
#repeating values example
numbers=[1,2,3,4,5,2,2,4,3,5,6,6,7]
print(numbers)
#mutable example it allows to change values
emp=["usha",27,"dataengineer"]
print(emp)
emp[1]=36
print(emp)
#tuple()
#it allows multiples of different vlues and it dont allows changes in pre defined values is called immutable
stu=("chethan",7,2,"school")
print(stu)
print(type(stu))
p=()
print(type(p))
#even we give it like in braces it wont allow it as tuple if we give, after the value in braces it will take it as tuple
q=()
q=(6)
print(q)
print(type(q))
aj=[1,2,3,4,"usha"]
print("list values",aj)
aj.add(4)
print(aj)
pl=tuple(aj)
print(pl)
print(type(pl))
#immutable concept
employ=("chethan",25,"dataengineeer")
print(employ)
#employ(1)=56
print(employ)
#Range
p=range(6)
print(p)
print(list(p))
#range([start],stop,[step])
for i in range(2,15,3):#this is like skip count strat from 2 upto 15 skip 3
    print(i)
    #set datatypes
    #set is unique and mutable
    #frozen set is unique and immutable
    lang={"pythan","java","scala"}
    print(lang)
    print(type(lang))
    lang.add("c#")
    print(lang)
    num=set([1,2,3,4,5,6])
    print(num)
    print(type(num))











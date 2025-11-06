a=10
b=34
print(a,b)
print(a,b,sep="\n" )#for next line
print(a,b,sep="\t")#for tab space
print(a,b,sep=",")
print(a,b,sep="@ ")
x='usha'
y='rani'
print(x,end="    ")#to give space and print in same line
print(y)
print(x)
print(x,end="@  ")
print(y)
print(x,end=" EXTENSION   ")
print(y)
print(x,end="we can write anything here   ")
print(y)
x="usha"+"rani"#we call this as string cancatination
print(x)
print("------------------------")
x=[1,2,3,4,3,5,6,1,1,2,2,3]
def duplicate_remove(x):
    c=[]
    for i in x:
        if i not in c:
            c.append(i)
    return c
print(duplicate_remove(x))
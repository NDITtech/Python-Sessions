#loops
#for loop - ierate over the sequence - list, tuple, string, dictionary, range

#for variable in sequence:
    #code

fruits=  ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

x = (1,2,3,4,5,5,6,6,7,7,7,7)
for y in x:
    print(y)
p = "apple"
for q in p:
    print(q)
print("-range-----")
#range
for x in range(6):
    print(x)


for x in range(3,6):
    print(x)



#while loop
print("--while loop------")

count = 0
while count <=5:
    print(count)
    count += 1
print("----------")
y = 1
while(y<=20):
    print(y)
    y = y+5
print("------------")
#to find the odd number
x = 9
y = 25

i = x
if i%2==0:i=x+1
while i<=y:
    print(i)
    i+=2 #i = i+2


print("nested loop")


for i in range(1,4):  #1,2,3
    for j in range(1,3): #1,2
        print("i=",i, "j=", j)
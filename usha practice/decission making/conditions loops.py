
#if condition
a=20
if a==20:
    print("Yes")
#if,else condition
a=10
b=70
if a > b:
    print("false")
else :
    print("true")
#elif conditoin
age=19
if age==18:
    print("you are elizable for vote")
elif age==17:
    print(" wait 1 year to vote")
else:
    print("you are elizable for vote")
user_logged_in = True
user_role = "employee"
#nested if else condition
if user_logged_in:
    if user_role=="admin":
        print(" welcome admin, you have the full access")
    else:
        print("welcome user, you have limited access")
else:
    print("please login to continue")
print("-----------------")
validation_score = 69
error_percentage = 25

if validation_score>=90 and error_percentage<= 5:
    print("Data quality acceptable")
elif validation_score>=80 and error_percentage<=15:
    print("partial quality-required review")
else:
    print("data quality failed")
#loops
#for loop,while
print("LOOPS")
#loops
#for loop - ierate over the sequence - list, tuple, string, dictionary, range

#for variable in sequence:
    #code
print("forlooooooooooooooooooop")

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

print ("tart from 3 ,end at 6")
for x in range(3,6):
    print(x)
    print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
#while loop
print("--while loop------")
count = 0
while count <=5:
    print(count)
    count += 1
print("----------")
y = 0
while(y<=20):
    print(y)
    y = y+5
print("------------")
#to find the odd number
x = 9
y = 25

i = x
if i%2==0:
    i=x+1
while i<=y:
    print(i)
    i+=2
    #i = i+2


print("nested loop")


for i in range(1,4):  #1,2,3
    for j in range(1,3): #1,2
        print("i=",i, "j=", j)
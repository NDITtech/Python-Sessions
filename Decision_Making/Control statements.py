#break
for i in range(15):  #0,1,2,3,4,5,6,7,8,9,10,11,12,13,14
    if i==5:
        break
    print(i)

print("-------------")
lst = [2,4,6,8,9,14,56]
for i in lst:
    if(i==9):
        break
    print(i)


#continue
for i in range(15):  #0,1,2,3,4,5,6,7,8,9,10,11,12,13,14
    if i==8:
        continue
    print(i)

print("-pass------")
#pass
for i in range(10):
    pass



#decision making - if, if-else,if-elif-else, nested if
#loops - for loop, while loop
#control statements - break, continue , pass
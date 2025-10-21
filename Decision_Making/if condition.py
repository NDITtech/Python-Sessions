#Decision Making
# #if statement
x = 10
if x > 15:
    print("this is the correct value")
else:
    print("executed else statement")

print("---elif---------")

#elif

age = 17
if age>= 18:
    print("you can vote")
elif age == 17:
    print("wait for a year")
else:
    print(" not eligible for vote")

#Nested if


user_logged_in = True
user_role = "employee"

if user_logged_in:
    if user_role=="admin":
        print(" welcome admin, you have the full access")
    else:
        print("welcome user, you have limited access")
else:
    print("please login to continue")



print("-------")

validation_score = 69
error_percentage = 25

if validation_score>=90 and error_percentage<= 5:
    print("Data quality acceptable")
elif validation_score>=80 and error_percentage<=15:
    print("partial quality-required review")
else:
    print("data quality failed")

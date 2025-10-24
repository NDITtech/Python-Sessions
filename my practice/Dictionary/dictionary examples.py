#Dictionary
#it contains key value pair
emp={"name":"usha","age":36}
print(emp)
print(type(emp))
emp1=dict(name="usha",age=36)
print(emp1)
#adding more variables
emp['city']="banglore"
print(emp)
emp["sal"]=23456
print(emp)
print(emp.values())
print(emp.keys())
#OR
y=emp.keys()
z=emp.values()
print(y)
print(z)
x=emp.items()
print(x)
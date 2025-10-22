#Dictionary
#key : value


#[]
#()
#{}


emp = {"name": "Devendran", "sal": 1000 }
print(emp)

emp1 = dict(name="Devendran", age=29)
print(emp1)

emp['city'] = "Bangalore"
print(emp)

emp['sal']= 1500
print(emp)
print("--------------")
print(emp["name"])


emp2 = {
    "id" : 12345,
    "name" : "Deven",
    "role": "Data Engineer",
    "skills": ["python", "Databricks", " Azure", "SQL"]


}
print(emp2)

y = emp2.keys()
print(y)
z = emp2.values()
print(z)
print("-----------")

x = emp2.items()
print(x)





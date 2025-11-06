#oops is object oriented programming
#class is blueprint of an object
#object is a instance of class
class Student:
    marks = 100
    def __init__(self,name, id):
        self.name = name
        self.id  = id
    def show_details(self):
        print(self.name)
        print(self.id)
    def show_marks(cls):
        print(cls.marks)

    def add1(id, name):
        return id + name
    print(add1("one ", "dev"))

s1 = Student("anusha", 1)
s2 = Student("usha", 2)
s3 = Student("ashok", 3)

print(s1.show_details())
print(s2.show_details())
print(s3.show_details())
print(s1.show_marks())
class Car:
    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year
    def show_details(self):
        return self.model

d = Car("Wolkswagen","ev",2025)
s = Car("Honda","petrol",2024)
g = Car("Suzuki","diesel",2023)
l = Car("Nissan","ev",2022)

print(d.show_details(),s.show_details(),g.show_details())
#print(s.show_details())
#print(g.show_details())
#print(l.show_details())'''

#features of oops concept:
#1. Abstraction
#2. Encapsulation
#3. Inheritance
#4. Polymorphism

#1. Abstraction:
#It will hide irrevalant information like implemetation and give only necessory information like functionlities.
'''
def hiding(func):
    def wrapper(a,b):
        if b==0:
            print("it is not divisible by 0")
            return None
        return func(a, b)
    return wrapper

@hiding
def div(a,b):
    return a/b
print("division two numbers:", div(1,0))


#2. Encapsulation
#wrapping of attributes and methods in one entity
class Car:
    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year
    def show_details(self):
        return self.model

class Bike:
    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year
    def show_details(self):
        return self.name

d = Car("Wolkswagen","ev",2025)
s = Bike("Wolkswagen","ev",2025)

print(d.show_details())
print(s.show_details())'''

#3. inheritance
# getting the properties from one class to another class
#1. single inheritance
#2. multi level inheritance
#3. multiple inheritance
#4. hierarcheal inheritance
#5. hybrid inheritance

#1. single inheritance
class Employee:
    def __init__(self,name,emp_id,base_salary):
        self.name=name
        self.emp_id= emp_id
        self.base_salary=base_salary

class Developer(Employee):
    def __init__(self,name,emp_id,base_salary, tech_stack):
        super().__init__(name,emp_id,base_salary)
        self.tech_stack = tech_stack

    def show_details(self):
        return self.name, self.emp_id, self.base_salary, self.tech_stack


d = Developer("Ashok",1,100000,"python")
print("Developer details:",d.show_details())

#2. multi level inheritance
class Manager:
    def __init__(self,name,emp_id,base_salary):
        self.name=name
        self.emp_id= emp_id
        self.base_salary=base_salary

class TeamLead(Manager):
    def __init__(self,name,emp_id,base_salary, tech_stack):
        super().__init__(name,emp_id,base_salary)
        self.tech_stack = tech_stack

class Developer(TeamLead):
    def __init__(self, name, emp_id, base_salary, tech_stack, team_size):
        super().__init__(name, emp_id, base_salary, tech_stack)
        self.team_size = team_size
    def show_details(self):
        return self.name, self.emp_id, self.base_salary, self.tech_stack,self.team_size


d = Developer("Ashok",1,100000,"python",10)
print("Developer details:",d.show_details())

#3. multiple inheritance
class Manager:
    def __init__(self,name,emp_id,base_salary):
        self.name=name
        self.emp_id= emp_id
        self.base_salary=base_salary

    def show_details(self):
        return self.name, self.emp_id, self.base_salary

class Teamlead:
    def conduct_training(self):
        return "Conducting technical training session"

class Developer(Manager,Teamlead):
    def manage_team(self):
        return "Managing team and conducting trainings"

d = Developer("Ashok",1,100000)
print("Developer show_details:",d.show_details())
print("Developer conduct_training:",d.conduct_training())
print("Developer manage_team:",d.manage_team())

#4. hierarcheal inheritance
class Manager:
    def __init__(self,name,emp_id,base_salary):
        self.name=name
        self.emp_id= emp_id
        self.base_salary=base_salary

    def show_details(self):
        return self.name, self.emp_id, self.base_salary

class Tester(Manager):
    def run_tests(self):
        return "Running regression test cases."

class Developer(Manager):
    def process_payroll(self):
        return "Processing monthly payroll."

t = Tester("Ramesh", 104, 70000)
h = Developer("Priya", 105, 90000)

print("The tester is :", t.show_details())
print("The Developer is:",h.show_details())

#5. hybrid inheritance
class Employee:
    def __init__(self,name,emp_id,base_salary):
        self.name=name
        self.emp_id= emp_id
        self.base_salary=base_salary

    def show_details(self):
        return self.name, self.emp_id, self.base_salary
class HR:
    def __init__(self,name,emp_id,base_salary):
        self.name=name
        self.emp_id= emp_id
        self.base_salary=base_salary

    def show_details(self):
        return self.name, self.emp_id, self.base_salary
class Intern(Employee):
    def __init__(self, name, emp_id, base_salary, mentor):
        super().__init__(name, emp_id, base_salary)
        self.mentor = mentor

    def show_details(self):
        return f"{super().show_details()}, Mentor: {self.mentor}"

class Mentor(Developer, HR):
    def guide_intern(self):
        return "Guiding interns in both technical and HR-related aspects."

class InternMentor(Mentor, Intern):
    pass
q = Mentor("Ramesh", 104, 70000)

print(q.show_details())
print(q.guide_intern())

#Polymorphism
#Object behaves as many forms
#1 compile time polymorphism  - method overloading
class BonusCalculator:
    def calculate_bonus(self, base=10000, performance=None):
        if performance is None:
            return base * 0.10  # default bonus
        elif performance == 'A':
            return base * 0.25
        elif performance == 'B':
            return base * 0.15
        else:
            return base * 0.10

calc = BonusCalculator()
print(calc.calculate_bonus())
print("Salary with performance is None:",calc.calculate_bonus(100000))       # default
print("Salary with performance is A:",calc.calculate_bonus(100000, 'A'))  # performance-based
print("Salary with performance is B:",calc.calculate_bonus(100000, 'B'))

#2 run time polymorphism  - method overriding
class Manager:
    def calculate_salary(self):
        return "Base Employee Salary Calculated"

class Developer(Manager):
    def calculate_salary(self):
        return "Manager Salary includes base + bonus"

class Tester(Developer):
    def calculate_salary(self):
        return "Developer Salary includes base + project allowance"

for emp in [Manager(), Developer(), Tester()]:
    print(emp.calculate_salary())


class Students:     #Class name should start in caps
    marks = 100
    def __init__(self, name, id, sal, age, town, mobi=None):       #init : constructor
        self.name = name
        self.id = id
        self.sal = sal
        self.age = age
        self.town = town
        self.mobi = mobi
    def show_details(self):     #we are passing output  here
        print(self.name)
        print(self.id)
        print(self.mobi)

    def show_marks(self):
        print(self.age)

    def show_sal(self):         #self & cls is a class variable
        print(self.sal)

    def details(self):
        print(self.name)
        print(self.age)
        print(self.town)
        print(self.id)
s1= Students("kala", 1, 10, 5, "atp", ) #s1 is a object

print(s1.show_details())

print(s1.show_marks())
print(s1.show_sal())

print("######-------")

s2 = Students("ashok", 8, 10,15, "atp", mobi=None)

print(s2.show_details())
print(s2.details())
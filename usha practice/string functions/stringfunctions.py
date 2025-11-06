#String method
print("converting string to lower case")
x="HELLO WORLD"
print(x.lower())
print("converting string to upper case")
print(x.upper())
print("removing spaces  at bigining and at the end of the  string")
y="      hello    "
a=y.strip()
print("hello",y,"world")
print("hello",a,"split")
#replace
print("replace")
d = "I like eating"
print(d)
print(d.replace("eating", "playing"))
#split
print("splitting given values how ever we want")
j= "apple, banana,orange,guava"

print(j.split(","))
#join
print("joining two seperate strings")
x = ["python", "programming"]
print(" ".join(x))
#capitalise
print("to capitalise given string")
n = "hello world"
print(n.capitalize())
print("---------")
#title
print("this is also capitalise the string")
print(n.title())
print("---------")
#count
z = "b","a","n","a","n","a"
print(z.count("n"))

print("---------")
print("hello".isalpha())
print("123".isdigit())
print(" ".isspace())






#string functions
#lower case
x= "HELLO WORLD"
print(x.lower())
#CONVERTS ALL LETTERS IN A STRING TO LOWER
#UPPER
#converts all lower case letters to upper
y="hello world"
print(y.upper())
#strip
#it will removes spaces
s="     hello       world"
print(s)
#replace
#it will replaces the existing value
x="i like playing"
print(x)
print(x.replace("playing","eating"))
#split
x="apple,orange,banana,guavava"
print(x.split(","))
#join
x=["java","python","c#"]
print("".join(x))
#capitalise
#it will capitalize first letter
y="hello world"
print(y.capitalize())
#title
#capitalize and title is similar
z="banana"
print(z.title())
#count
l="chethan"
print(l.count("h"))
print("hello".isalpha())
print("123".isdigit())
print("  ".isspace())
text = "Python is fun to learn"
words = text.split()
print(words)
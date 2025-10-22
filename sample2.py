let = list("abcd")  # Here converting string into list. "abcd" is a string

print(let)  # ['a', 'b', 'c', 'd']

print(type(let))  # <class 'list'>

print('------------------')

intt = list((1, 2, 3, 4, 5))  # Here trying to convert a tuple of integers into a list.

print(intt)  # [1,2,3,4,5]

print(type(intt))  # <class 'list'>


# (1, 2, 3, 4, 5) itself is the tuple, and you need parentheses to define it

# The outer parentheses belong to list()

# The inner parentheses define the tuple (1, 2, 3, 4, 5).

print('------------------')

'''
Here, will
get
more
clarity:
'''
numbers = (10, 20, 30, 40)

x = list(numbers)

intt = list((1, 2, 3, 4, 5))

print(x)  # [10, 20, 30, 40]

print(type(x))  # <class 'list'>
print('------------------')
numbers = (10, 20, 30, 40, 'ash')

print(numbers)

print(type(numbers))  # <class 'tuple'>

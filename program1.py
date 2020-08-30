#4.1
'''pizzas = ['dominos', 'pizza hut', 'off beat']
for pizza in pizzas:
    print()
    print(pizza)
    print('i like peporoni pizza')
print()
print('i really love pizza')
'''

# 4.2
'''
animals  = ['tiger', 'lion', 'tortouis']
for name in animals:
    print(name)
    print('a dog is a great pet')
print()
print('any of these animals would make a great pet\n')
'''

# range of function
for numbers in range(1,10):
    print(numbers)

# list of numbers using range function
print()
numbers = list(range(1,10))
print(numbers)

# even numbers using range()
print()
even_numbers = list(range(2,11,2))
print(even_numbers)

# odd numbers using range ()
print()
odd_numbers = list(range(1, 11, 2))
print(odd_numbers)

# square
squares = []
for numbers in range(1,10):
    square = numbers**2
    squares.append(square)
print(squares)
"""Functions"""

# Non-parameterized:
def my_function():
    print("This is the function")

print("Before Function")

my_function()

# Parameterized

name = input("Enter your name: ")

def my_function2(n):
    print("Hello "+n)

my_function2(name)

# Returning a Value

num = input("Enter a number: ")
print("The square of "+num+" is:")

def my_function3(n):
    return n**2


print(my_function3(int(num)))

# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
#Define these functions in main.py:
''' greet: takes a name and returns a string in the format:
Hello, Bob! '''

def greet(name) :
    return f'Hello, {name}!'

print(greet('Bob'))

'''add: takes three numbers (integers or floats) and returns their sum. Example:
'''

def add(a,b,c):
    return a+b+c
print(add(5,3,2))

'''positive: takes a number (integer or float) and returns whether or not it is positive in the form of a boolean. You do not have to handle the case where the argument is not an int or a float. Examples:
'''
def positive(x):
    return x>0
positive(50)
positive(-50)
positive(0)



'''negative: takes a number (integer or float) and returns whether or not it is negative in the form of a boolean. You do not have to handle the case where the argument is not an int or float. Examples:
'''
def negative(x):
    return x<0

negative(50)

negative(-50)

negative(0)

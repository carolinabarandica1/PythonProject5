from tkinter.font import names
from types import new_class


def greet():
    print("hello!")

"""
simple function that just prints hello
:return: None
"""
print("hello!")

def greet2(name):
    """
       simple function that greets a person
       :param name: the name of a person
       :return: None
       """

print(f"hello,{names}")

greet2("jane")
greet2("mary")

def special_op(a,b):

    """
    special op is 10xa+b
    :param a: first number
    :param b: second number
    :return: value, 10a+b
    """

    result = 10*a + b
    return result

print(special_op(10,2))
print(special_op(2,10))

result = special_op(8,9)
print(f'the special op for 8 and 9 is: {result}')
print(special_op(8,9))

print(special_op())
print(special_op(9))

def bond_greet(name):
    print(f'the name is: {name}')

def bondise_name (first_name, last_name):
    return f'{last_name}, {first_name}{last_name}'

print(bondise_name('john', 'doe'))
bond_greet(bondise_name(first_name='john', last_name='doe'))
bond_greet(bondise_name())


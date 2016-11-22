from collections import OrderedDict

numerals ={
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

def roman_to_numerical(number):
    result = 0
    previous_value = None
    for letter in reversed(number):
        value = numerals[letter]
        if (previous_value is None) or (previous_value <= value):
            result += value
        else:
            result -= value
        previous_value = value
    #print result
    return result

num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
def numerical_to_roman(number):
    roman = ''
    while number > 0:
        for i, r in num_map:
            while number >= i:
                roman += r
                number -= i

    return roman
def add(x, y):
   """This function adds two numbers"""
   return x + y

def subtract(x, y):
   """This function subtracts two numbers"""
   print abs(x-y)
   return abs(x - y)

def multiply(x, y):
   """This function multiplies two numbers"""
   return x * y

def divide(x, y):
   """This function divides two numbers"""
   return x / y

def operator_map():
    return {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
    }

# take input from the user
def calculation(number1,number2,choice):
    number1 = roman_to_numerical(number1)
    number2 = roman_to_numerical(number2)
    operator_mapping = operator_map()

    operation = operator_mapping.get(choice)
    print "operation/....", operation
    if not operation:
        result = "Invalid Operand"
        return result
    result = operation(number1, number2)

    final_result = numerical_to_roman(result)
    return final_result

def main():
    number1 = raw_input("Enter first roman number:")
    number2 = raw_input("Enter second roman number:")
    choice = raw_input("Enter Operator:")
    print calculation(number1, number2, choice)

if __name__ == "__main__":
    main()

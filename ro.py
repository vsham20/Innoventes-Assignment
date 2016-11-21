from collections import OrderedDict

numerals = [
        {'letter': 'M', 'value': 1000},
        {'letter': 'D', 'value': 500},
        {'letter': 'C', 'value': 100},
        {'letter': 'L', 'value': 50},
        {'letter': 'X', 'value': 10},
        {'letter': 'V', 'value': 5},
        {'letter': 'I', 'value': 1},
    ]

def roman_to_numerical(number):
    index_by_letter = {}
    for index in range(len(numerals)):
        index_by_letter[numerals[index]['letter']] = index

    result = 0
    previous_value = None
    for letter in reversed(number):
        index = index_by_letter[letter]
        value = numerals[index]['value']
        if (previous_value is None) or (previous_value <= value):
            result += value
        else:
            result -= value
        previous_value = value
    #print result
    return result

def numerical_to_roman(number):
    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(number):
        for r in roman.keys():
            x, y = divmod(number, r)
            yield roman[r] * x
            number -= (r * x)
            if number > 0:
                roman_num(number)
            else:
                break

    return "".join([a for a in roman_num(number)])
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

# take input from the user

def calculation(number1,number2,choice):
    number1 = roman_to_numerical(number1)
    number2 = roman_to_numerical(number2)

    if choice == '+':
       result = add(number1,number2)

    elif choice == '-':
       result = subtract(number1,number2)

    elif choice == '*':
       result = multiply(number1,number2)

    elif choice == '/':
       result = divide(number1,number2)
    else:
       result = "Invalid input"
    final_result = numerical_to_roman(result)
    return final_result
number1 = raw_input("Enter number")
number2 = raw_input("Enter number 2")
choice = raw_input("Enter operator")
print calculation(number1,number2,choice)


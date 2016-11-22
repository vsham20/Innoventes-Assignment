from collections import OrderedDict

class rom_conversions():

    def roman_to_numerical(self,number):
        numerals ={
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
        }
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

    def numerical_to_roman(self,number):
        numerals_new = {100:'C',400:'CD',900:'CM',500:'D',1:'I',4:'IV',9:'IX',50:'L',1000:'M',5:'V',10:'X',90:'XC',40:'XL'}
        nextLowest  = lambda seq,x: min([(x-i,i) for i in seq if x>=i] or [(0,None)])[1]
        final_string = ""
        while number>1:
            b = nextLowest(numerals_new.keys(),number)
            x,y = divmod(number,b)
            temp_string = x*numerals_new.get(b) #map it back to character
            final_string = final_string + temp_string
            number = y
        return final_string
    def add(self,x, y):
       """This function adds two numbers"""
       return x + y

    def subtract(self,x, y):
       """This function subtracts two numbers"""
       print abs(x-y)
       return abs(x - y)

    def multiply(self,x, y):
       """This function multiplies two numbers"""
       return x * y

    def divide(self,x, y):
       """This function divides two numbers"""
       return x / y

    def operator_map(self):
        return {
        '+': self.add,
        '-': self.subtract,
        '*': self.multiply,
        '/': self.divide
        }

    # take input from the user
    def calculation(self):
        temp_list = get_input()
        number1 = self.roman_to_numerical(temp_list[0])
        number2 = self.roman_to_numerical(temp_list[1])
        operator_mapping = self.operator_map()

        operation = operator_mapping.get(temp_list[2])
        print "operation/....", operation
        if not operation:
            result = "Invalid Operand"
            return result
        result = operation(number1, number2)

        final_result = self.numerical_to_roman(result)
        return final_result
def get_input():
    number1 = raw_input("Enter first roman number:")
    number2 = raw_input("Enter second roman number:")
    choice = raw_input("Enter Operator:")
    return [number1, number2, choice]
        
def main():
    test_obj = rom_conversions()
    print test_obj.calculation()

if __name__ == "__main__":
    main()

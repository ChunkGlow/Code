
def int_to_roman(num):
    if num <= 0 or num >= 4000:
        return None
    
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    
    result = ""
    for i in range(len(values)):
        count = num // values[i]
        result += symbols[i] * count
        num -= values[i] * count
    return result

def roman_to_int(roman):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    total = 0
    prev_value = 0
    
    for char in reversed(roman.upper()):
        if char not in roman_values:
            return None
        
        value = roman_values[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total

class Integer:
    def __init__(self, integer):
        self.integer = integer

class Roman:
    def __init__(self, roman):
        self.roman = roman

choice = int(input("Integer>Roman Numeral:(1) Roman Numeral>Integer:(2) "))

if choice == 1:
    integer_input = int(input("Enter an integer: "))
    if 0 < integer_input < 4000:
        roman_result = int_to_roman(integer_input)
        print("Roman Numeral:", roman_result)
    else:
        print("Invalid input - must be between 1 and 3999")

elif choice == 2:
    roman_input = input("Enter a Roman Numeral: ").upper()
    integer_result = roman_to_int(roman_input)
    if integer_result is not None:
        print("Integer:", integer_result)
    else:
        print("Invalid Roman numeral")

else:
    print("Invalid choice")

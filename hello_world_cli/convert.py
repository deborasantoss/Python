import sys

def decimal_to_roman(m):
    number = int(m)

    number_to_symbol = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }

    roman = ""

    for value in sorted(number_to_symbol.keys(), reverse=True):
        while number >= value:
            roman += number_to_symbol[value]
            number -= value

    print(f"The Roman numeral for {m} is {roman}")

def roman_to_decimal(m):
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    current_number = 0
    prev_value = 0

    for roman in reversed(m):
        value = roman_numerals.get(roman, 0)  # Use .get() to handle invalid Roman numerals

        if value == 0:
            print(f"Invalid Roman numeral: {roman}")

        if value < prev_value:
            current_number -= value
        else:
            current_number += value
        prev_value = value

    print(f"The decimal value for {m} is {current_number}")

def convert():
    m = sys.argv[1]
    if m.isnumeric() == True:
        decimal_to_roman(m)
    else:
        roman_to_decimal(m)

if __name__ == '__main':
    convert()


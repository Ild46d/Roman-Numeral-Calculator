# Throbac Functional Program
# Author: Souhail Boukhari
# Date: November 14, 2025
# Project: Roman Numeral Calculator

# This program lets the user do math (+, -, *, /, ^)
# with Roman numerals between 1 and 3999.
roman_values = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

def is_valid_roman(roman):
    # Check if all characters are valid
    for ch in roman:
        if ch not in roman_values:
            return False
    # V, L, D can only appear once
    for ch in ['V', 'L', 'D']:
        if roman.count(ch) > 1:
            return False
    # I, X, C, M cannot appear 4+ times
    for ch in ['I', 'X', 'C', 'M']:
        if roman.count(ch * 4) > 0:
            return False
    return True

def roman_to_int(roman):
    # Convert Roman numeral to integer
    total = 0
    prev = 0
    for ch in reversed(roman):
        val = roman_values[ch]
        # Subtractive notation (IV = 4)
        if val < prev:
            total -= val
        else:
            total += val
        prev = val
    return total

def int_to_roman(num):
    # Convert integer to Roman numeral
    symbols = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
    roman = ""
    for value, symbol in symbols:
        while num >= value:
            roman += symbol
            num -= value
    return roman

def getRoman(prompt):
    # Get and validate Roman numeral input
    while True:
        roman = input(prompt).upper()

        # Easter egg for 2008
        if roman == "MMVIII":
            print("🎉You found it !🎉 2008 is my birth year!")
            return roman, True
        
        if not is_valid_roman(roman):
            print("Not a valid Roman numeral. Please try again.")
            continue

        value = roman_to_int(roman)
        if value < 1 or value > 3999:
            print("Value must be between 1 and 3999")
        else:
            return roman, False

def get_operator():
    # Get valid operator from user
    while True:
        op = input("Operator :")
        if op in ['+', '-', '*', '/', '^']:
            return op
        else:
            print("Invalid operator. Try again.")

def do_math(a, b, op):
    # Perform the mathematical operation
    if op == '+':
        return a + b, None
    elif op == '-':
        return a - b, None
    elif op == '*':
        return a * b, None
    elif op == '/':
        if b == 0:
            print("Error: cannot divide by zero.")
            return None, None
        return a // b, a % b
    elif op == '^':
        return a ** b, None
    
def show_result(result, remainder = None):
    # Display result in digital and Roman format
    if result is None:
        return
    if result < 1:
        print("Result is negative - Nih roman numeral for Ets!")
        return
    if result > 3999:
        print("Result too large for roman numerals! (Igo told Vou Thuod max is 3999)")
        return
    
    print(f"Digital result: {result}")
    print(f"Roman result: {int_to_roman(result)}")
    if remainder:
        print(f"Remainder: {int_to_roman(remainder)}")

def main():
    # Main program loop
    print("🐥 Welcome to Sousou's Roman Numeral Calculator!🐥\n")

    while True:
        # Get first number
        r1, is_2008_r1 = getRoman("Enter first Roman number: ")
        if not is_2008_r1:
            n1 = roman_to_int(r1)
            print(f"Value of {r1}: {n1}")
        else:
            n1 = 2008

        # Get second number
        r2, is_2008_r2 = getRoman("Enter second Roman number: ")
        if not is_2008_r2:
            n2 = roman_to_int(r2)
            print(f"Value of {r2}: {n2}")
        else:
            n2 = 2008

        op = get_operator()
        result, remainder = do_math(n1, n2, op)
        show_result(result, remainder)

        again = input("C)ontinue? (Y/N): ").upper()
        if again != 'Y':
            print("Goodbye, noble Roman! 🏛️")
            break

if __name__ == "__main__":
    main()
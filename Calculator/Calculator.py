# Calculator

from replit import clear
from Calculator_art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    number1 = True
    while number1:
        try:
            num1 = float(input("What's the first number?: "))
        except ValueError:
            print("Please only numbers!")
            continue
        number1 = False

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:

        operation_symbol = input("Pick an operation: ")
        if operation_symbol.isalpha() or operation_symbol.isnumeric():
            print('Please only symbols!')
            continue

        number2 = True
        while number2:
            try:
                num2 = float(input("What's the next number?: "))
            except ValueError:
                print("Please only numbers!")
                continue
            number2 = False

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()


calculator()

# operation_symbol = input("Pick an operation: ")
# num3 = int(input("What's the next number?: "))
#
# calculation_function = operations[operation_symbol]
#
# second_answer = calculation_function(calculation_function(num1, num2), num3)
#
# second_answer = calculation_function(first_answer, num3)


# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

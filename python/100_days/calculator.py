#!/usr/bin/python3
"""This module performs four basic math calculations"""

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def div(n1, n2):
    return n1 / n2
def mul(n1, n2):
    return n1 * n2


operations = {
    "+": add,
    "-": sub,
    "/": div,
    "*": mul,
}
from art import calc_logo
def calculator():
    print(calc_logo)
    num1 = float(input("Input your first number "))
    for operation in operations:
        print(operation)
    continue_calc = True

    while continue_calc:
        operation_symbol = input("pick operation ")
        num2 = Float(input("Input your second number "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        end_of_calc = input("press y to continue calculation with last answer or n to start a new one ").lower()
        if end_of_calc == "y":
            num1 = answer
        else:
            continue_calc = False
            calculator()
calculator()

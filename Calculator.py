import argparse

def parse():

    parser = argparse.ArgumentParser(description='IMI Taschenrechner')
    parser.add_argument('operation', help='addition, subtraction, division or multiplication', type=str)
    parser.add_argument('number1', type=int)
    parser.add_argument('number2', type=int)

    args = parser.parse_args()

    a = args.number1
    b = args.number2

    operationtyp = args.operation

def calculation():

    if operationtyp == "addition":
        return (a+b)
    if operationtyp == "subtraction":
        return (a-b)
    if operationtyp == "division":
        return (a/b)
    if operationtyp == "multiplication":
        return (a*b)

result = calculation()

def display():
    print("The result is: " + result)

parse()
calculation()
display()

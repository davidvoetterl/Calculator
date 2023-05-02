import argparse

#def welcome():
  #  print("Willkommen beim IMI Taschenrechner")
    #calcoperator = input("Bitte geben Sie eins der folgenden vier Zeichen ein, um die Rechenoperation zu bestimmen: + - / *\n")

#def addition(a,b):
  #  result =  a + b
    #return result

#def substraction(a,b):
  #  result =  a - b
    #return result

#def division(a,b):
  #  result =  a / b
   # return result

#def multiplication(a,b):
  #  result =  a * b
   # return result

def main():


    parser = argparse.ArgumentParser(description='IMI Taschenrechner')
    parser.add_argument('operation', help='addition, subtraction, division or multiplication')
    parser.add_argument('number1', type=int)
    parser.add_argument('number2', type=int)

    args = parser.parse_args()

    a = args.number1
    b = args.number2

    if args.operation == "addition":
        print (a+b)
    if args.operation == "subtraction":
        print (a-b)
    if args.operation == "division":
        print (a/b)
    if args.operation == "multiplication":
        print (a*b)

main()

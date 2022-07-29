"""
•	You have to take an integer type variable, and the input of the variable will define the length of the triangle.
•	You have to declare another Boolean variable.
•	When the value of Boolean is 1 i.e. True, the pattern will be printed as shown above.
•	But if the value of Boolean is 0 or false, then the triangle will be printed upside down.

"""

def TrueFunction(value):

    for i in range(1, value+1):
        for j in range (1,i+1):
            print("*",end="")
        print("")


def FalseFunction(value):

    for i in range(value,0, -1):
        for j in range (0,i):
            print("*",end="")
        print("")

def ParseValue(value):
    if value == 0:
        return False
    else:
        return True

def TakeInput():
    checker = False
    inputValue = input("Enter the Number of Rows : ")
    checker = inputValue.isdigit()
    if checker:
        return int(inputValue)
    else:
        print("\nYou have Entered an Invalid Number.\n Try Again Wisely\n\n")
        TakeInput()

def Direction():
    inputValue = input("Enter the Direction\n0: For Upside Down\n1: For Downside Up\nEnter your Choice : ")
    if inputValue == "0" or inputValue == "1":
        return ParseValue(int(inputValue))
    else:
        print("\nYou have Entered an Invalid Number.\n Try Again Wisely\n\n")
        Direction()


Rows = TakeInput()
Direction = Direction()

if Direction:
    TrueFunction(Rows)
else:
    FalseFunction(Rows)
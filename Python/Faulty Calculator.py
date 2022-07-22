"""
Scenario:
    Suppose that you are an invigilator in an exam. A calculator is not allowed for the exam.
    You discover somehow that students are planning to cheat in exams, using a calculator program in Python language.
    Somehow, you get your hands on the calculator program.
    Now you want to alter a few results in the calculator with your own provided results to catch the students trying to
    cheat using the calculator program.
The user will provide the following inputs:
    Operator
        The two numbers between which the operator is applied
    All the results will be correct, except for these few:
        45 * 3 = 555
        56+9 = 77
        56/6 = 4
"""

operator = input("Enter the Operation you want to perform (+, -, *, /) : ")
firstNumber = int(input("Enter the First Number : "))
secondNumber = int(input("Enter the Second Number : "))

if(operator == "+"):
    if(firstNumber == 56 and secondNumber == 9):
        print("56 + 9 = 77")
    else:
        print(str(firstNumber) ,"+",str(secondNumber) ,"=",str(firstNumber+secondNumber))
elif(operator == "-"):
    print(str(firstNumber), "-", str(secondNumber), "=", str(firstNumber - secondNumber))
elif(operator == "*"):
    if ((firstNumber == 45 and secondNumber == 3) or (firstNumber == 3 and secondNumber == 45)):
        print(str(firstNumber), "+", str(secondNumber), "=", "555")
    else:
        print(str(firstNumber), "*", str(secondNumber), "=", str(firstNumber * secondNumber))
elif(operator == "/"):
    if (firstNumber == 56 and secondNumber == 6):
        print("56 / 6 = 4")
    else:
        print(str(firstNumber), "/", str(secondNumber), "=", str(firstNumber / secondNumber))
else:
    print("Please Enter the Valid Operator")

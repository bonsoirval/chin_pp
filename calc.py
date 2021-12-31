"""
This is a command line calculator for basic arithmetic operations.
@dev Njoku Okechukwu Val    - bonsoirval@gmail.com
@dev Blessing Akinola       - mailto:akinolablessing25@gmail.com
"""
"""
User can see a display showing the current number entered or the result of the last operation.
 User can see an entry pad containing buttons for the digits 0-9, operations - '+', '-', '/', and '=', a 'C' button (for clear), and an 'AC' button (for clear all).
 User can enter numbers as sequences up to 8 digits long by clicking on digits in the entry pad. Entry of any digits more than 8 will be ignored.
 User can click on an operation button to display the result of that operation on:
the result of the preceding operation and the last number entered OR
the last two numbers entered OR
the last number entered
 User can click the 'C' button to clear the last number or the last operation. If the users last entry was an operation the display will be updated to the value that preceded it.
 User can click the 'AC' button to clear all internal work areas and to set the display to 0.
 User can see 'ERR' displayed if any operation would exceed the 8 digit maximum.
"""
print("""
##########################################
#Welcome To Chin_pp CLI Basic Calculator #
##########################################""")
operation = None
while operation not in ['q', 'Q', 'Quit', 'QUIT']:
    operation = input("""
Select Action
1. + [addition]
2. - [subtraction]
3. / [division]
4. * [multiplication]
5. Q [Quit]
""")
    if operation == '1':
        try:
            num1 = float(input("Enter num1 : "))
            num2 = float(input("Enter num2 : "))
            print(f"{num1} + {num2} = {round(num1 + num2, 2)}")
        except ValueError:
            print("Error: Texts not allowed. Enter only numbers:")
    elif operation == '2':
        try:
            num1 = float(input("Enter num1 : "))
            num2 = float(input("Enter num2 : "))
            print(f"{num1} + {num2} = {round(num1 - num2, 2)}")
        except ValueError:
            print("Error: Texts not allowed. Enter only numbers:")

    elif operation == '3':
        try:
            num1 = float(input("Enter num1 : "))
            num2 = float(input("Enter num2 : "))
            print(f"{num1} + {num2} = {round(num1 / num2, 2)}")
        except ValueError:
            print("Error: Texts not allowed. Enter only numbers:")
        print('/')
    elif operation == '4':
        try:
            num1 = float(input("Enter num1 : "))
            num2 = float(input("Enter num2 : "))
            print(f"{num1} + {num2} = {round(num1 * num2, 2)}")
        except ValueError:
            print("Error: Texts not allowed. Enter only numbers:")
    elif operation == '5':
        sure = input("Are you sure you want to quit 'y'/'yes'")
        if sure in ['yes', 'Yes', 'y', 'Y']:
            print("Good bye")
            quit("Exiting ... ")
        else: pass
        continue
    else:
        print("Invalid input")
        continue

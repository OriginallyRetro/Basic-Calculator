#IMPORTS

import os
#might wanna remove all else staments try and except covers it alr i think

def main_Menu_Cal():
    print(" _____________________________")
    print("|[1] Addition                 |")
    print("|[2] Subtraction              |")
    print("|[3] Multiplcation            |")
    print("|[4] Division                 |")
    print("|[5] Exponets                 |")
    print("|[6] How to use the Calculator|")
    print("|_____________________________|")
    option = input("Choose your operation: ")
    if option.lower().strip() == ('1'):
        addition_Cal()
    if option.lower().strip() == ('2'):
        subtraction_Cal()
    if option.lower().strip() == ('3'):
        multiplcation_Cal()
    if option.lower().strip() == ('4'):
        division_Cal()
    if option.lower().strip() == ('5'):
        exponets_cal()
    if option.lower().strip() == ('6'):
        tutorial()
    else:
        os.system("cls")
        main_Menu_Cal()
    
#-------------------------
#ADDITION CAL    
def addition_Cal()-> None:
    os.system("cls")
    option = input("Type 'c' to continue using the calculator or type 'm' to co to main menu: ")
    if option.lower().strip() == ('c'):
        try:
            first_Number = float(input("Pick your first number you want: "))
            second_Number = float(input("now pick your second number you want: "))
            print("Result: ", first_Number+second_Number)
            input("Press enter to continue")
            os.system("cls")
        except:
            print("Invalid")
            addition_Cal()
    if option.lower().strip() == ('m'):
        os.system("cls")
        main_Menu_Cal()
    


#-------------------------
#SUBTRACTION CAL
def subtraction_Cal()-> None:
    os.system("cls")
    option = input("Type c to continue using the calculator or type m to go to main menu.")
    if option.lower().strip() == ('c'):
        try:
            first_Number = float(input("Pick your first number you want: "))
            second_Number = float(input("now pick your second number you want: "))
            print("Result: ", first_Number-second_Number)
            input("Press enter to continue")
            os.system("cls")
        except:
            print("Invalid")
            subtraction_Cal()
    if option.lower().strip() == ('m'):
        os.system("cls")
        main_Menu_Cal()


#-------------------------
#MULTIPLCATION CAL
def multiplcation_Cal()-> None:
    os.system("cls")
    option = input("Type c to continue using the calculator or type m to go to main menu.")
    if option.lower().strip() == ('c'):
        try:
            first_Number = float(input("Pick your first number you want: "))
            second_Number = float(input("now pick your second number you want: "))
            print("Result: ", first_Number*second_Number)
            input("Press enter to continue")
            os.system("cls")
        except:
            print("Invalid")
            multiplcation_Cal()
    if option.lower().strip() == ('m'):
        os.system("cls")
        main_Menu_Cal()

#-------------------------
#DIVSION CAL
def division_Cal()-> None:
    os.system("cls")
    option = input("Type c to continue using the calculator or type m to go to main menu.")
    if option.lower().strip() == ('c'):
        try:
            first_Number = float(input("Pick your first number you want: "))
            second_Number = float(input("now pick your second number you want: "))
            print("Result: ", first_Number/second_Number)
            input("Press enter to continue")
            os.system("cls")
        except:
            print("Invalid")
            division_Cal()
    if option.lower().strip() == ('m'):
        os.system("cls")
        main_Menu_Cal()

#-------------------------
#EXPONETS CAL
def exponets_cal()-> None:
    os.system("cls")
    option = input("Type c to continue using the calculator or type m to go to main menu.")
    if option.lower().strip() == ('c'):
        try:
            first_Number = float(input("Pick your first number you want: "))
            second_Number = float(input("now pick your second number you want: "))
            print("Result: ", first_Number**second_Number)
            input("Press enter to continue")
            os.system("cls")
            main_Menu_Cal()
        except:
            print("Invalid")
            exponets_cal()
    if option.lower().strip() == ('m'):
        os.system("cls")
        main_Menu_Cal()

#-------------------------
#TUTORIAL
def tutorial()-> None:
    os.system("cls")
    option = input("Type c to continue open the tutorial or type m to go to main menu.")
    if option.lower().strip() == ('c'):
        input("How to use the calculator:\n\nThe first thing you do is pick the operation you would like to perform. Afterwards you pick your two numbers and depending on the operation you chose it will do the correspodning events. So if you want to do 5 + 5 pick Addition then put 5 press enter than 5 again and your result will be 10")
        os.system("cls")
        main_Menu_Cal()
    if option.lower().strip() ==('c'):
        os.system("cls")
        main_Menu_Cal()
    
main_Menu_Cal()



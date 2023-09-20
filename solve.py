##
# 2WF90 Algebra for Security -- Software Assignment 1 
# Integer and Modular Arithmetic
# solve.py
#
#
# Group number:18
# group_number 
#
# Author names and student IDs:
# Deniz Ozen (1734970) 
# Efsane Yildiz (1783777)
# Idil Misra Yilmaz (1801511)
# Kerem Gokce (1850407)
##

# Import built-in json library for handling input/output 
import json


def num_converter(n: int,radix: int):
    hex_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"][:radix]

    if n >= 0:
        if n == 0:
            return ""
        else:
            return num_converter(n // len(hex_chars),radix) + hex_chars[n % len(hex_chars)]
    else:
        return ""

def karatsuba(x: int,y: int):
    if (x<10) or (y<10):
        return x*y
    else:
        x = str(x)
        y = str(y)
        # print(x[:2])

        n = max(len(x),len(y))
        n2 =int(n/2)
        # print(n2)
        Xhi = int(x[:n2])
        Xlo = int(x[n2:])
        Yhi = int(y[:n2])
        Ylo = int(y[n2:])
        print(f'Xhigh: {Xhi} Xlow: {Xlo} Yhigh: {Yhi} Ylow: {Ylo}')
        Z = karatsuba(Xhi,Yhi)*(10**n) + (karatsuba(Xhi,Ylo) + karatsuba(Xlo,Yhi))*(10**n2) + karatsuba(Xlo,Ylo)

        return Z


def solve_exercise(exercise_location : str, answer_location : str):
    """
    solves an exercise specified in the file located at exercise_location and
    writes the answer to a file at answer_location. Note: the file at
    answer_location might not exist yet and, hence, might still need to be created.
    """
    
    # Open file at exercise_location for reading.
    with open(exercise_location, "r") as exercise_file:
        # Deserialize JSON exercise data present in exercise_file to corresponding Python exercise data 
        exercise = json.load(exercise_file)
        

    ### Parse and solve ###
    radix = exercise['radix']
    x = int(exercise['x'],radix)
    y = int(exercise['y'],radix)

    # Check type of exercise
    if exercise["type"] == "integer_arithmetic":
        # Check what operation within the integer arithmetic operations we need to solve
        if exercise["operation"] == "addition":
            answer = x + y
        elif exercise["operation"] == "subtraction":
            answer = x - y
        elif exercise["operation"] == "multiplication_primary":
            answer = x * y
        elif exercise["operation"] == "multiplication_karatsuba":
           if (x<10) or (y<10):
               answer = x * y

        elif exercise["operation"] == "extended_euclidean_algorithm":
            # Solve integer arithmetic subtraction exercise
            pass
    
    else: # exercise["type"] == "modular_arithmetic"
        # Check what operation within the modular arithmetic operations we need to solve
        if exercise["operation"] == "reduction":
            # Solve modular arithmetic reduction exercise
            pass
        elif exercise['operation'] == "addition":
            pass
        elif exercise["operation"] == "inversion":
            # Solve modular arithmetic reduction exercise
            pass
        elif exercise["operation"] == "subtraction": 
            pass
        
        elif exercise["operation"] == "multiplication":
            answer = x - y
   
   
    return num_converter(answer, radix)
   
    # Open file at answer_location for writing, creating the file if it does not exist yet
    # (and overwriting it if it does already exist).
    with open(answer_location, "w") as answer_file:
        # Serialize Python answer data (stored in answer) to JSON answer data and write it to answer_file
        json.dump(answer, answer_file, indent=4)




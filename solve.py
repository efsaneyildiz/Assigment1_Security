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
from integer_arithmetic import karatsuba
from integer_arithmetic import Ext_eucl
from integer_arithmetic import primary_mult
from number_converters import to_int
from number_converters import to_radix


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
    x = to_int(exercise['x'],radix)
    y = to_int(exercise['y'],radix)
    type = exercise['type']

    # Check type of exercise
    if type == "integer_arithmetic":
        # Check what operation within the integer arithmetic operations we need to solve
        if exercise["operation"] == "addition":
            answer = x + y
        elif exercise["operation"] == "subtraction":
            answer = x - y
        elif exercise["operation"] == "multiplication_primary":
            answer = primary_mult(str(x),str(y))
        elif exercise["operation"] == "multiplication_karatsuba":
               answer = karatsuba(x,y)

        elif exercise["operation"] == "extended_euclidean_algorithm":
            answer = Ext_eucl(x,y)
    
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
   
   
    return to_radix(answer, radix)
   
    # Open file at answer_location for writing, creating the file if it does not exist yet
    # (and overwriting it if it does already exist).
    with open(answer_location, "w") as answer_file:
        # Serialize Python answer data (stored in answer) to JSON answer data and write it to answer_file
        json.dump(answer, answer_file, indent=4)




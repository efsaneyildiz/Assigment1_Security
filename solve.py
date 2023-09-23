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
from number_converters import to_decimal
from number_converters import to_radix
from modular_arithmetic import mod_inversion
from modular_arithmetic import mod_reduction
from modular_arithmetic import mod_subtraction
from modular_arithmetic import mod_multiplication
from modular_arithmetic import mod_addition

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

    type = exercise['type']
    operation = exercise['operation']
    radix = exercise['radix']
    x = to_decimal(exercise['x'], radix)

    if type == 'modular_arithmetic':
        modulus = exercise['modulus']
        if (operation!='reduction') and (operation != 'inversion'):
            y = to_decimal(exercise['y'], radix)

    else:
        y = to_decimal(exercise['y'], radix)

    print(f'Operation: {operation}\ntype: {type}')

    # Check type of exercise
    if type == "integer_arithmetic":
        # Check what operation within the integer arithmetic operations we need to solve
        if exercise["operation"] == "addition":
            answer = int(x) + int(y)
            answer = {'answer': str(to_radix(answer, radix))}
        elif exercise["operation"] == "subtraction":
            answer = int(x) - int(y)
            answer = {'answer': str(to_radix(answer, radix))}

        elif exercise["operation"] == "multiplication_primary":
            result = primary_mult(str(x),str(y))
            answer = {'answer': str(to_radix(result, radix))}

        elif exercise["operation"] == "multiplication_karatsuba":
            answer = karatsuba(int(x),int(y))
            answer = {'answer': str(to_radix(answer, radix))}
        elif exercise["operation"] == "extended_euclidean_algorithm":
            a,b,gcd = Ext_eucl(int(x),int(y))
            a,b,gcd = to_radix(a,radix), to_radix(b, radix), to_radix(gcd, radix)
            answer ={
                'answer-a': str(a),
                'answer-b': str(b),
                'answer-gcd': str(gcd)
                    }

    else: # exercise["type"] == "modular_arithmetic"
        # Check what operation within the modular arithmetic operations we need to solve
        if exercise["operation"] == "reduction":
            # Solve modular arithmetic reduction exercise
            answer = mod_reduction(x, modulus)
            answer = {'answer': str(to_radix(answer, radix))}
        elif exercise['operation'] == "addition":
            answer = mod_addition(x, y, modulus)
            answer = {'answer': str(to_radix(answer, radix))}
        elif exercise["operation"] == "inversion":
            # Solve modular arithmetic reduction exercise
            answer = mod_inversion(x, modulus)
            answer = {'answer': str(to_radix(answer, radix))}
        elif exercise["operation"] == "subtraction":
            answer = mod_subtraction(x, y, modulus)
            answer = {'answer': str(to_radix(answer, radix))}
        
        elif exercise["operation"] == "multiplication":
            answer = mod_multiplication(x, y, modulus)
            answer = {'answer': str(to_radix(answer, radix))}
    # Open file at answer_location for writing, creating the file if it does not exist yet
    # (and overwriting it if it does already exist).

    with open(answer_location, "w") as answer_file:
        # os.makedirs(os.path.dirname(answer_location), exist_ok=True)
        json.dump(answer, answer_file, indent=4)

    # return answer


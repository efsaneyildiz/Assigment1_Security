# from solve import solve_exercise
# import json
#
#
# # type = 'Realistic'
# type = 'Simple'
#
#
# for i in range(0,14):
#     with open(f'Examples/{type}/Answers/answer{i}.json', "r") as answer_file:
#         answer_set = json.load(answer_file)
#     answer = answer_set
#
#     print(f'Exercise {i} started')
#     ex_path = f'Examples/{type}/Exercises/exercise{i}.json'
#     sol_path = f'Examples/OurSolutions/{type}/answer{i}.json'
#
#     solve_exercise(ex_path, sol_path)
#     with open(sol_path, "r") as answer_file:
#         solution = json.load(answer_file)
#     # solution = solution['answer']
#
#     print(f'The answer {i} is: {answer} \nYour Solution is: {solution}')
#     print(f'Exercise{i} completed\n')

import json
from solve import solve_exercise


def main():
    # Specify the exercise type (e.g., 'Simple' or 'Realistic')
    exercise_type = 'Simple'

    for i in range(0, 14):
        # Define file paths
        exercise_path = f'Examples/{exercise_type}/Exercises/exercise{i}.json'
        answer_path = f'Examples/{exercise_type}/Answers/answer{i}.json'
        our_solution_path = f'Examples/OurSolutions/{exercise_type}/answer{i}.json'

        try:
            # Load the answer
            with open(answer_path, "r") as answer_file:
                answer = json.load(answer_file)

            print(f'Exercise {i} started')

            # Solve the exercise and save the solution
            solve_exercise(exercise_path, our_solution_path)

            # Load the solution
            with open(our_solution_path, "r") as solution_file:
                solution = json.load(solution_file)

            print(f'The answer {i} is: {answer}\nYour Solution is: {solution}')
            print(f'Exercise {i} completed\n')

        except FileNotFoundError:
            print(f'Exercise {i} not found. Skipping...\n')
        except Exception as e:
            print(f'Error while processing Exercise {i}: {str(e)}\n')


if __name__ == "__main__":
    main()

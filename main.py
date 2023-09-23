from solve import solve_exercise
import json


# type = 'Realistic'
type = 'Simple'


for i in range(0,14):
    with open(f'Examples/{type}/Answers/answer{i}.json', "r") as answer_file:
        answer_set = json.load(answer_file)
    answer = answer_set

    print(f'exercise{i} started')
    ex_path = f'Examples/{type}/Exercises/exercise{i}.json'
    sol_path = f'Examples/OurSolutions/{type}/answer{i}.json'

    solve_exercise(ex_path, sol_path)
    with open(sol_path, "r") as answer_file:
        solution = json.load(answer_file)
    # solution = solution['answer']

    print(f'The answer {i} is: {answer} \nYour Solution is: {solution}')
    print(f'Exercise{i} completed\n')
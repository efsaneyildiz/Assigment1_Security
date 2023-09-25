import json
from solve import solve_exercise
import time


def main():
    # Specify the exercise type ('Simple' or 'Realistic')
    exercise_type = 'Realistic'

    # Initialize counters for correct and incorrect answers
    correct_count = 0
    incorrect_count = 0

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

            # Check if the answer is correct
            if answer == solution:
                print(f'The answer {i} is CORRECT: {answer}')
                correct_count += 1
            else:
                print(f'The answer {i} is INCORRECT. \nExpected: {answer}, \nYour Solution: {solution}')
                incorrect_count += 1

            print(f'Exercise {i} completed\n')

        except FileNotFoundError:
            print(f'Exercise {i} not found. Skipping...\n')
        except Exception as e:
            print(f'Error while processing Exercise {i}: {str(e)}\n')

    # Print the total counts
    print(f'Total Correct Answers: {correct_count}')
    print(f'Total Incorrect Answers: {incorrect_count}')
    print(f'Total Error: {i+1-(correct_count+incorrect_count)}')


if __name__ == "__main__":

    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'\nTotal Run Time: {elapsed_time}')

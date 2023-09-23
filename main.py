from solve import solve_exercise

# type = 'Realistic'
type = 'Simple'

for i in range(0,14):
    print(f'exercise{i} started')
    ex_path = f'Examples/{type}/Exercises/exercise{i}.json'
    ans_path = f'Examples/OurSolutions/{type}/answer{i}.json'

    solve_exercise(ex_path,ans_path)
    print(f'Exercise{i} completed')
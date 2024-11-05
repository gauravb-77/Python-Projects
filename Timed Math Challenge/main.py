import random, time

operators = ['+', '-', '*']

min_operand = 2

max_operand = 11

total_problems = 10

def generate_problem():

    operator = random.choice(operators)

    left_operand = random.randint(min_operand, max_operand)

    right_operand = random.randint(min_operand, max_operand)

    expr = str(left_operand) + ' ' + operator + ' ' + str(right_operand)

    answer = eval(expr)

    return expr, answer

wrong = 0

input("Press enter to start!")

print("-----------------------")

start_time = time.time()

for index in range(total_problems):
    
    expr, answer = generate_problem()

    while True:
        
        guess = input(f"Problem #{index + 1}: {expr} = ")

        if guess == str(answer):

            break 

        wrong += 1

end_time = time.time()

total_time = end_time - start_time

print("-----------------------")

print("Nice work! You finished in", round(total_time, 2), "seconds with", wrong, "wrong answers.")

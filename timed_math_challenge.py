
import random
import time

OPERATORS = ['+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_QUESTIONS = 5

def generate_question():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


wrong_answer = 0
print("Welcome to the Timed Math Challenge!")
input("Press Enter to start...")
print("---------------------------")

start_time = time.time()


for i in range(TOTAL_QUESTIONS):
    expr, answer = generate_question()
    
    while True:
        user_answer = input(f"Question {i + 1}: {expr} = ")
        if user_answer == str(answer):
            print("Correct!")
            break
        else:
            print("Incorrect. Try again.")
            wrong_answer += 1

end_time = time.time()

print("---------------------------")
print(f"Total Questions: {TOTAL_QUESTIONS}")
print(f"Wrong Answers: {wrong_answer}")
print(f"Time Taken: {end_time - start_time:.2f} seconds")
print("Thanks for playing!")

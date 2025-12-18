# Add error handling and pytest compatibility
# also record time and score in a file

'''
A function that generates a question.
A function that runs the quiz.
A function that formats the time message.
A function that writes results to a file.
'''

import random
import time


def generate_a_question():
    numbers = [i for i in range(1, 11)]
    # values_list = []
    # count = 0
    random_number1 = random.choice(numbers)
    random_number2 = random.choice(numbers)
    expected = random_number1 * random_number2
    result_tuple = (random_number1, random_number2, expected)
    # values_list.append(result_tuple)
    return values_list



def run_quizz(iters):
    start_time = time.perf_counter()
    for i in range(iters):
        generate_a_question()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time


def time_format():
    if elapsed_time < 60:
        return f"Test completed in {elapsed_time} seconds!"
    else:
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        return f"Test completed in {minutes} minute(s) and {seconds} seconds"


def write_to_file():
    with open('staar_results.txt', 'a') as file:
        file.write(time_format())


if __name__ == "__main__":

    name = input("Enter your name: ").strip().title()
    numbers = [i for i in range(2, 10)]
    random.seed(1)

    start_time = time.perf_counter()
    points = 0
    questions = 0
    for i in range(10):
        questions += 1
        random_number1 = random.choice(numbers)
        random_number2 = random.choice(numbers)
        expected = random_number1 * random_number2
        while True:
            try:
                response = input(
                    f"Question #{i + 1}: {random_number1} x {random_number2} = ")
                if int(response) == expected:
                    points += 1
                    print("Correct!\n")
                else:
                    print(f"Incorrect! The answer was {expected}\n")
                break
            except ValueError:
                print("Make sure to enter digits only, Try again.")

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    if elapsed_time <= 60:
        print(f"Hey {name}, you completed the test in {elapsed_time:.2f} seconds, and you got a total of {points} out of {questions}!")
    else:
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        if elapsed_time < 120:
            print(f"Hey {name}, you completed the test in {minutes:.0f} minute and {seconds:.2f} seconds, and you got a total of {points} out of {questions}!")
        else:
            print(f"Hey {name}, you completed the test in {minutes:.0f} minutes and {seconds:.2f} seconds, and you got a total of {points} out of {questions}!")


'''
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
'''

# Hey Caca Maia, you completed the test in 1 minute and 8.67 seconds, and you got a total of 8 out of 10!0
# Hey Veronica, you completed the test in 59.73 seconds, and you got a total of 9 out of 10!

'''
def generate_questions(iter = 5): 
    numbers = [i for i in range(1, 11)] 
    values_list = [] 
    count = 0 
    for i in range(iter): 
        count += 1 
        random_number1 = random.choice(numbers) 
        random_number2 = random.choice(numbers) 
        expected = random_number1 * random_number2 
        result_tuple = (random_number1, random_number2, expected) 
        values_list.append(result_tuple) 
    return values_list
'''
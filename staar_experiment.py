'''
A function that generates a question.
A function that runs the quiz.
A function that formats the time message.
A function that writes results to a file.
'''

import random
import time

# Best practice: the module should define functions; running the program should be separate from importing it.

'''
1/ Pure functions: generate questions, evaluate answers, format time, record results
2/ Interactive wrapper (under __main__): prompts the user, starts the timer, loops through questions, stops the timer, prints results, optionally writes to a file

'''


# question generation
def generate_a_question():
    numbers = [i for i in range(1, 11)]
    random_number1 = random.choice(numbers)
    random_number2 = random.choice(numbers)
    expected = random_number1 * random_number2
    result_tuple = (random_number1, random_number2, expected)
    return result_tuple



# orchestration / repetition
def run_quizz(iters):
    values_list = []
    for i in range(iters):
        result_tuple = generate_a_question()
        values_list.append(result_tuple)
    return values_list



# time formatting
def measure_time():
    start_time = time.perf_counter()
    run_quizz(1000)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    if elapsed_time <= 60:
        return f"Test completed in {elapsed_time:.2f} seconds.\n"
    else:
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        return "Test completed in {minutes:.0f} minute(s) and {seconds:.2f} seconds.\n"
    

        
# record the results

def write_to_file():
    with open("text.txt", "a") as file:
        file.write(measure_time())
    # print("Text added to file")

write_to_file()

if __name__ == "__main__":
    print(generate_a_question())
    print(run_quizz(5))
    print(measure_time())
    write_to_file()


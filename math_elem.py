import random
import time

# shifted your tests toward property-based assertions
# Make sure there are no similar questions: eg 8 * 1 or 1 * 8 in the same batch
# Write to a file with name, data, topic, points out of questions, with one line per result

'''
A while True must have at least one of these inside it:
- a break (exit condition),
- a return (exit function),
- a change to the condition/state that will eventually lead to a break.
'''

def generate_question_mult():

    range_down = 1
    range_up = 10
    number1 = random.randint(range_down, range_up)
    number2 = random.randint(range_down, range_up)
    expected = number1 * number2
    return number1, number2, expected

def max_iters_mult():
    range_down = 1
    range_up = 10
    n = range_up+1 - range_down
    max_iter = int(n * (n+1) / 2)
    return range_down, range_up, max_iter

def generate_question_add():

    range_down = 1
    range_up = 100
    number1 = random.randint(range_down, range_up)
    number2 = random.randint(range_down, range_up)
    expected = number1 + number2
    return number1, number2, expected

def max_iters_add():
    range_down = 1
    range_up = 100
    max_iter = int((range_up * (range_up + 1) / 2))
    return range_down, range_up, max_iter

def build_set_mult():
    mi = 1
    ma = 10
    my_set = set()
    while len(my_set) < int((ma * (ma + 1) / 2)):
        n1 = random.randint(mi, ma)
        n2 = random.randint(mi, ma)
        key = (min(n1, n2), max(n1, n2))

        if key in my_set:
            continue
        
        my_set.add(key)
    return my_set, len(my_set)

def build_set_add():
    mi = 1
    ma = 100
    my_set = set()
    while len(my_set) < int((ma * (ma + 1) / 2)):
        n1 = random.randint(mi, ma)
        n2 = random.randint(mi, ma)
        key = (min(n1, n2), max(n1, n2))

        if key in my_set:
            continue
        
        my_set.add(key)
    return my_set, len(my_set)





def main():
    
    while True:
        topic = input("Welcome to our math test! Enter 'm' for multiplication, 'a' for addition, or 'q' to stop the program: " )
        topic = topic.strip().lower()
        if topic == "m" or topic == "a":
            points = 0
            operator_symbol = "x" if topic == "m" else "+"
            while True:
                iterations = input("How many questions do you want to work on? (min = 1 and max = 55 to get questions. 0 to end the program): ").strip()
                try:
                    iterations = int(iterations)
                    range_down, range_up, max_iter = max_iters_mult()
                    if (topic == "m" and iterations <= max_iter) or (topic == "a"):
                        start_time = time.perf_counter()
                        answers_so_far = 0
                        if iterations == 0:
                            print("We are ending this program. Bye!")
                            return
                        my_set = set()
                        for i in range(iterations):
                            number1, number2, expected = generate_question_mult() if topic == "m" else generate_question_add()
                            

                            while True:  
                                key = (min(number1, number2), max(number1, number2))
                                if (topic == "m") and (key in my_set):
                                    continue
                                elif (topic == "m") and (key not in my_set) or (topic == "a"):
                                    my_set.add(key)  
                                    your_answer = input(f"Question # {i+1}: How much is {number1} {operator_symbol} {number2}? \n") 
                                    your_answer = your_answer.strip()
                                    if your_answer.lower() == "q": # Command before parsing
                                        print("We are ending this program. Goodbye!")
                                        return
                                    try:
                                        your_answer = int(your_answer)

                                        answers_so_far += 1
                                        if your_answer == expected:
                                            points += 1
                                            print(f"Correct!\nNumber of points: {points} / {answers_so_far}\n")
                                        else:
                                            print(f"Incorrect! The correct answer was {expected}\nNumber of points: {points} / {answers_so_far}\n")
                                        break 
                                    except ValueError:
                                        print("Make sure to enter a number only (integer).\n")
                        end_time = time.perf_counter()
                        elapsed_time = end_time - start_time
                    else:
                        print("Enter 0 to quit, or a number from 1 to 55. Try again.")  
                        continue

                        

                    print(f"Congrats! You earned {points} {'point' if points == 1 else 'points'} out of {iterations}!\nIt took you {elapsed_time:.2f} seconds to complete the test.")
                    break
                except ValueError:
                    print("Enter a number only.")            
                        
            
                
        elif topic == "q":
            return
        else:
            print("Enter only 'm' for multiplication, 'a' for addition, or 'q' to stop the program.")
            

        
# make the file usable as a script as well as an importable module, because the code that parses the command line only runs if the module is executed as the “main” file    
        
if __name__ == "__main__":     
    main()






'''
import itertools

my_list = ['dog', 'cat', 'fish']
# Generate all unique unordered pairs of length 2
unordered_pairs = list(itertools.combinations(my_list, 2))

print(unordered_pairs)

'''
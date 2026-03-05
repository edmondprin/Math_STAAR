'''
LAYER 1 - PURE LOGIC (TESTABLE)
No loops/retry - No side effects (no print/input/file/time) - Returns values
Examples:   generate_question(studied_number)
            check_answer(user_answer, expected)
			build_question_pool(studied_number, count)
			max_iters_mult()
			
LAYER 2 - ORCHESTRATION (APP FLOW)
Calls pure functions (from layer 1), build questions, control loops, manages scoring, returns results
This can still avoid direct input() and print() if designed well
Example:    run_quizz_engine(studied_number, count)

LAYER 3 - INTERFACE LAYER (I/O)
input() - print() - formatting messages
This is what main() should handle
Example: run_quiz_cli(): calls engine and handles input/print.



Make run_quiz() fully parameterized

Meaning:
	•	It should not call input() to determine quiz size.
	•	It should accept studied_number + number_of_questions

Then:
	•	main() gathers user input
	•	run_quiz() just runs logic

'''

import random


# LAYER 1

class UnsupportedTopicError(Exception):
     pass

# Function 1: Converts to int, enforces range, returns int or raises ValueError
def validate_studied_number(studied_number , low=2, high=9):
    studied_number  = int(studied_number )
    if low <= studied_number  <= high:
        return studied_number 
    else: 
        raise ValueError(f"Number must be between {low} and {high}")
    

# Function 2: converts to int, enforces min/max (eg 1-55 for mult unique), returns int or raises ValueError
def validate_iterations(raw, min_n=1, max_n=None):
     raw = int(raw)
     if raw < min_n:
          if max_n is None:
               raise ValueError(f"Number should be at least {min_n}")
          else:
               raise ValueError(f"Number should be between {min_n} and {max_n}")
     elif max_n is not None and raw > max_n:
          raise ValueError(f"Number should be between {min_n} and {max_n}")
     return raw

# Function 3: returns (min(a, b), max(a, b)), pure helper used for commutative uniqueness
def canonical_pair(a, b):
     return (min(a, b), max(a, b))

# Function 4: returns max unique unordered pairs with repetition: n(n+1)/2 where n = high-low+1, used to cap iterations for unique commutative topics
def max_unique_pairs(low, high):
     n = high - low + 1
     max_unique = n * (n + 1) // 2
     return max_unique

# Function 5: returns (a, b) based on topic rules, for multiplication trainer: one operand can be studied_number
def generate_operands(topic, studied_number=None): # ranges=None
    if topic == "mult":
      if studied_number is None:
           raise ValueError("A studied_number is mandatory when working on multiplications")
      else:
          a, b = random.randint(1, 10), studied_number 
          return a, b
    elif topic == "add":
         a, b = random.randint(1, 100), random.randint(1, 100)
         return a, b
    else:
         raise UnsupportedTopicError("Please select 'mult' or 'add' only.")


# Function 6: returns a question tuple (eg (a, b, expected) or a small dict). Expected computed based on topic


def make_question(topic, a, b):
     if topic == "mult":
          return (a, b, a * b, "*")
     elif topic == "add":
          return (a, b, a + b, "+")
     else:
          raise UnsupportedTopicError("Please select 'mult' or 'add' only.")


# Fucntion 7 (optional but useful): returns a list of questions, if uniqueness is on for commutative topics, enforces canonical uniqueness. No retries during the quiz loop.

def build_question_pool(topic, count, studied_number=None, unique=False):
    if topic not in ("mult", "add"):
        raise UnsupportedTopicError("Please select 'mult' or 'add' only")

    if topic == "mult":
        if studied_number is None:
            raise ValueError("A studied_number is mandatory when working on multiplications")

        studied_number = validate_studied_number(studied_number, low=2, high=9)

        if unique and count > 10:
            raise ValueError("It is not possible to have more than 10 unique multiplications with a random operand from 1 to 10.")

    questions = []
    seen = set()

    for _ in range(count):

        if topic == "mult" and unique:
            while True:
                a, b = generate_operands(topic, studied_number)
                if a not in seen:
                    seen.add(a)
                    break
        else:
            a, b = generate_operands(topic, studied_number)

        question = make_question(topic, a, b)
        questions.append(question)

    return questions

# LAYER 2

def run_quiz():
	pass

def main():
    studied_number = input("Enter a number you want to work on: ")
    print(validate_studied_number(studied_number ))


if __name__ == "__main__": 
      main()







'''
class OutOfRangeError(Exception):
     pass


def validate_studied_number(number):
    try:
         number = int(number)
         if 1 < number < 10:
            return number
         else: # Invalid range
              raise OutOfRangeError("Number must be between 2 and 9")
    except ValueError: # Invalid type
         raise ValueError("Enter an integer")
    
'''
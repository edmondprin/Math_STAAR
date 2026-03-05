import random


def validate_studied_number():
    while True:
        try:
            studied_number = int(input(
                "What is the number from 2 to 9 that you want to work on with multiplications? "))
            if studied_number < 2 or studied_number > 9:
                print("Please make sure to select a number between 2 and 9")
                continue
            return studied_number

        except ValueError:
            print("Please make sure to select a number (integer) between 2 and 9")
            continue


def run_quiz():
    studied_number = validate_studied_number()
    correct_answer = 0
    total_answers = 44
    for i in range(total_answers):
        random_number = random.randint(2, 10)
        expected = random_number * studied_number
        while True:
            your_answer = input(
                f"Question #{i+1}: {random_number} * {studied_number}: ")
            try:
                your_answer = int(your_answer)
                if your_answer == expected:
                    print("Great, this is correct!")
                    correct_answer += 1
                    break
                else:
                    print(f"Incorrect, the result was {expected}")
                    break
            except ValueError:
                print(
                    "Make sure to enter an number, not a letter or special character.")

    print(f"{correct_answer} out of {total_answers}")


def main():
    run_quiz()


if __name__ == "__main__":
    main()

'''

while True to get studied_number:
  if studied_number is ok:
    start for loop (*44)
      while True with input and int parsing
  
OR

while True to get studied_number:
  if studied_number is ok:
    start for loop (*44)
      input
      while True with int parsing
        input asked again if non-digit answer

'''


'''
Configurability: total_answers = 5 is hardcoded. Fine for now; later you may want to pass it as an argument or ask the user.
Quit option: currently the only way out mid-quiz is Ctrl+C. If you want "q" to quit, your structure already supports adding that check before parsing.

Pattern A (what you have — good)
run_quizz() calls validate_questions_number()
Clear top-down flow
Easy to read, test, and extend

Pattern B (both called by a third function)
A main() function calls:
validation
then quiz
This becomes useful when your program grows

Pattern C (validation returns data, quiz stays pure)
Validation gathers inputs
Quiz accepts parameters
No input() inside quiz logic
(This is the most testable architecture, but not required yet.)

'''

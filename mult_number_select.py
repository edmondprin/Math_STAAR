import random

while True:
    try:
        studied_number = int(input(
            "What is the number from 2 to 9 that you want to work on with multiplications? "))
        if studied_number < 2 or studied_number > 9:
            print("Please make sure to select a number between 2 and 9")
            continue
        else:
            correct_answer = 0
            total_answers = 5
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

        print(f"{correct_answer} / {total_answers}")
        break

    except ValueError:
        print("Please make sure to select a number (integer) between 2 and 9")
        continue

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

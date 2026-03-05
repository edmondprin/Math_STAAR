import random


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
    return list(my_set)

# print(build_set_mult())


while True:
    try:
        iterations = input("How many operations do you want to work on? ")
        list_of_numbers = build_set_mult()
        ori_len = len(list_of_numbers)
        round = 0
        correct_answer = 0
        for i in range(int(iterations)):
            while True:
                round += 1
                tuple_selected = random.choice(list_of_numbers)
                number1, number2 = tuple_selected
                expected = number1 * number2
                your_answer = input(f"How much is {number1} x {number2}? ")
                list_of_numbers.remove(tuple_selected)
                try:
                    your_answer = int(your_answer)
                    if your_answer == expected:
                        correct_answer += 1
                        print("Great, good answer!")
                    else:
                        print(f"Incorrect. The correct answer was {expected}")
                    break
                except ValueError:
                    print("Make sure to enter number!")
                    continue
        print(f"Correct: {correct_answer} | Questions: {round}")
        percentage_correct = correct_answer / round
        print(f"{percentage_correct * 100:.0f}%")
        if round >= 10:
            if percentage_correct >= 0.70:
                print(
                    f"Fantastic job! You got {correct_answer} out of {round}!")
            elif 0.5 < percentage_correct < 0.70:
                print(
                    f"This is not too bad: You got {correct_answer} out of {round}!")
            else:
                print(
                    f"You only got {correct_answer} out of {round}. Please try to focus a bit more next time!")
        print(f"{ori_len} - {round} = {len(list_of_numbers)}")
        break

    except ValueError:
        print("Enter number only!")
        continue

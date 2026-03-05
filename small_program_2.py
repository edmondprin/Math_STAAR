
'''

2) “Best of N” multiplication trainer (no uniqueness)

Goal: pick a studied number (2–9), ask 10 random questions, score at end.
Skills: nested loops + counters
Stretch: print “Correct/Incorrect” + final accuracy.
'''

import random
studied_number = random.randint(2, 9)
score = 0
count = 0
count_total = 10
quit_flag = False
halfway_shown = False
genius_flag = False
for _ in range(count_total):
    a, b = random.randint(1, 10), studied_number
    
    while True:
        if count == count_total//2 and not halfway_shown:
            print("Did you know? You can always press 'q' to exit the test")
            halfway_shown = True
            

        answer = input(f"{a} * {b} = ")
        if answer.strip().lower() == "q":
            quit_flag = True
            break
    
        try:
            answer = int(answer)
            if answer == a * b:
                print("Correct")
                score += 1
                count += 1
                break
            else:
                print("Incorrect")
                count += 1
                break
        except ValueError:
            print("Enter numbers only")
            continue
    if quit_flag:
        break
if count >= 8 and score / count_total >= 0.9:
    genius_flag = True
message = ", great job genius!" if genius_flag else ""
print(f"{score} out of {count}{message}")

    

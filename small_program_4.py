

'''
4) “Flashcard deck” from a list

Goal: store a list of 10 fixed Q/A pairs, quiz user, count score.
Skills: list of tuples + iteration
Stretch: shuffle order.
'''
import random

list_quizz = [("France", "Paris"), ("Spain", "Madrid"), ("Italy", "Rome"), ("Portugal", "Lisbonne"), ("England", "Londres"), ('Germany', "Berlin"), ("Netherlands", "Amsterdam"), ("Austria", "Vienna"), ("Finland", "Reykavick"), ("Norway", "Oslo")]
random.shuffle(list_quizz)
genius_flag = False
print(len(list_quizz))
score = 0
total = len(list_quizz)
for index, item in enumerate(list_quizz):
    this_question = list_quizz[index]
    answer = input(f"Question {index + 1}/{total}: What is the capital of {this_question[0]} ? ")
    if answer.strip().capitalize() == this_question[1]:
        print("Correct")
        score += 1
    else:
        print(f"Incorrect. The answer was {this_question[1]}")

    # list_quizz.remove(this_question)  
if score / total >= 0.9:
    genius_flag = True
print(f"{score} / {total}{", genius!" if genius_flag else ""}")

# for index, item in enumerate(list_list):
    # print(f"Index: {index}, Item: {item}")
'''
Iterate over a copy: Use for index, item in enumerate(list_quizz[:]): to iterate over a "snapshot" of the list while you safely modify the original.

Shuffle first: Use random.shuffle(list_quizz) before the loop, then simply iterate through it without needing to remove() anything or use random.choice() inside the loop.
'''

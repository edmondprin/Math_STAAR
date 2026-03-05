

'''
5) “Results logger” (append to file)

Goal: after quiz, append ONE line to a file: date, name, topic, score, duration.
Skills: file append + string formatting
Stretch: include studied number.
'''
import random 
from datetime import datetime

admin = False

def log_file():
    now = datetime.now()
    formatted_date = now.strftime("%B %d, %Y")
    
    name = input("What is your first name? ")
    if not name:
        name = "Anonymous"
    name = "-".join(name.split()).title()
    global admin
    if name == "Edmond":
        admin = True
    topic_list = ["Europe", "Americas", "Asia", "Africa", "Oceania"]
    # difficulty_coef = 0
    points = 0
    print("Welcome to our super mega chilly quiz about capitals!")
    for index, subject in enumerate(topic_list, start=1):
        print(f"{index}: {subject}")
    while True:
        index_picked = input("Pick one topic for a quiz by typing a number from 1 to 5: ")
        try: 
            index_picked = int(index_picked)
            if not 1 <= index_picked <= 5:        
                print("Enter a number from 1 to 5. Try again.")
                continue
            topic_picked = topic_list[index_picked - 1] 
            print(topic_picked)
            break
        except ValueError:
            print("Enter a number from 1 to 5, Try again.")
            continue
    
    europe_list = [("France", "Paris"), ("Spain", "Madrid"), ("Italy", "Rome"), ("Portugal", "Lisbon"), ("England", "London"), ('Germany', "Berlin"), ("Netherlands", "Amsterdam"), ("Austria", "Vienna"), ("Finland", "Helsinki"), ("Norway", "Oslo")]
    americas_list = [("USA", "Washington"), ("Canada", "Ottawa"), ("El Salvador", "San Salvador"), ("Argentina", "Buenos Aires"), ("Paraguay", "Asunción", "Asuncion"), ("Chile", "Santiago De Chile"), ("Venezuela", "Caracas"), ("Guatemala", "Guatemala City"), ("Mexico", "Mexico City"), ("Peru", "Lima")]
    asia_list = [("Russia", "Moscow"), ("China", "Beijing"), ("India", "New Delhi"), ("Kazakhstan", "Astana"), ("Saudi Arabia", "Riyadh"), ("Indonesia", "Jakarta"), ("Iran", "Tehran"), ("Mongolia", "Ulaanbaatar", "Ulan Bator"), ("Pakistan", "Islamabad"), ("Turkey", "Ankara")]
    africa_list = [("Nigeria", "Abuja"), ("Kenya", "Nairobi"), ("Egypt", "Cairo"), ("South Africa", "Pretoria"), ("Ghana", "Accra"), ("Ethiopia", "Addis Ababa"), ("Morocco", "Rabat"), ("Democratic Republic of the Congo", "Kinshasa"), ("Senegal", "Dakar"), ("Angola", "Luanda")]
    oceania_list = [("Australia", "Canberra"), ("New Zealand", "Wellington"), ("Fiji", "Suva"), ("Vanuatu", "Port Vila"), ("Samoa", "Apia"), ("Tonga", "Nukuʻalofa"), ("Micronesia", "Palikir"), ("Kiribati", "South Tarawa"), ("Solomon Islands", "Honiara"), ("Papua New Guinea", "Port Moresby")]

    topic_map = {
        "Europe": europe_list,
        "Americas": americas_list,
        "Asia": asia_list,
        "Africa": africa_list,
        "Oceania": oceania_list
    }

    set_for_quizz = topic_map[topic_picked]
    random.shuffle(set_for_quizz)
    # print(set_for_quizz)



    for i in set_for_quizz:
        country, *capitals = i
        user_input = input(f"What is the capital of {country}? ")
        user_input_clean = " ".join(user_input.split()).title()
        if user_input_clean in capitals:
            print("Correct!")
            points += 1
        else:
            print(f"Wrong! The capital is {capitals[0]}.")

    coef_map = {
        "Europe": 1.1,
        "Americas": 1,
        "Asia": 1.2,
        "Africa": 1.3,
        "Oceania": 1.6
    }

    points_coef = round(points * coef_map[topic_picked], 1)
    # print(points)



    with open("capitals_test.txt", "a") as f:
        f.write(f"{formatted_date} | {name} | {topic_picked} | {points}/{len(set_for_quizz)} | Total points: {points_coef} | Difficulty: {coef_map[topic_picked]} \n")

log_file()



def reset_log():
    with open("capitals_test.txt", "w") as file:
        pass
if admin:
    reset_action = input("Press 'R' to reset the logs, or a different key to keep the logs: ").lower()
    if reset_action == "r":
        reset_log()

'''
    # Data structure
question = ("Mongolia", ("Ulaanbaatar", "Ulan Bator"))

# Logic
country, acceptable_answers = question
user_input = input(f"What is the capital of {country}? ")

if user_input.title() in acceptable_answers:
    print("Correct! +1 point.")

# Your data
correct_answers = ("Ulaanbaatar", "Ulan Bator")

# 1. Get input: "Ulan    Bator"
# 2. .split() turns it into ["Ulan", "Bator"]
# 3. " ".join() turns it into "Ulan Bator"
user_input = " ".join(input("Capital of Mongolia: ").split()).title()

if user_input in correct_answers:
        print("Correct! +1 point.")
'''


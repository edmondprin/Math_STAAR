def generate_question(): 
    number1 = 3 
    number2 = 5 
    expected = number1 + number2 
    return number1, number2, expected 

if __name__ == "__main__": 
    def main(): 
        points = 0 
        number1, number2, expected = generate_question() 
        your_answer = input(f" Hello, how much is {number1} + {number2}? ") 
        while not your_answer.isdigit(): 
            your_answer = input(f" Hello, how much is {number1} + {number2}? ") 
            if int(your_answer) == expected: 
                points += 1 
        return points 
    
    print(main())
'''
6 small programs you can finish in 30–60 minutes each

1) “Input validator” mini-app

Goal: repeatedly ask for a number until it’s valid, then print it once.
Skills: loop + try/except + .strip()
Stretch: allow negative numbers and q to quit.

'''

while True:
    number = input("Enter a number or 'q' to quit: ")
    if number.strip().lower() == "q":
        break
    
    try:
        number = int(number.strip())
        print(number)
        break
    except ValueError:
        print("Number only")
        continue



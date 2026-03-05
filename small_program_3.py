
    

'''
3) “Timed 10 questions” (just timing, no architecture)

Goal: start timer before Q1, stop after Q10, show total seconds.
Skills: time.perf_counter() + formatting
Stretch: show seconds per question average.
'''

import time

count = 10
start_time = time.perf_counter()
for _ in range(count):
    answer = input(f"Question {_+1}/{count}: Enter a word: ")
end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Time to answer 10 questions: {elapsed_time:.0f} seconds")


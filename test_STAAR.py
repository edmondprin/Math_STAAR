from staar_experiment import generate_a_question, run_quizz, measure_time, write_to_file

import random

'''
1/ Seed inside the test (so the test controls the RNG state explicitly).
2/ Test properties (length is 5, operands are between 1 and 10, expected equals product, etc.).
3/ Inject/mock randomness so the function is predictable without relying on global RNG state.
'''

def test_generate_a_question():
    random.seed(1)
    result = generate_a_question()
    assert result == (3, 10, 30)
    assert isinstance(result, tuple)

def test_run_quizz():
    random.seed(1)
    results = run_quizz(5)
    assert results == [(3, 10, 30), (2, 5, 10), (2, 8, 16), (8, 8, 64), (7, 4, 28)]
    assert len(results) != 0
    assert isinstance(results, list)

def test_measure_time():
    duration = measure_time()
    assert duration.startswith("Test")
    assert isinstance(duration, str)

def test_file_writing():
    # record = write_to_file()
    file_path = "./text.txt"
    with open (file_path, "r") as f:
        content = f.read()
        assert content.startswith("Test")

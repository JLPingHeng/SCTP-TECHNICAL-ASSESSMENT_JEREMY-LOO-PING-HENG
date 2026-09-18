"""
Question 8 — Python: Find and Fix the Bug  [Short Answer — Write Code]

The function below is SUPPOSED to count how many even numbers are in a list.
It runs without crashing, but it returns the wrong answer.

    def count_evens(numbers):
        count = 0
        for n in numbers:
            if n % 2 == 1:      # <-- something here is wrong
                count = count + 1
        return count

    # Expected: 4  (the evens are 2, 4, 6, 8)
    print(count_evens([1, 2, 3, 4, 5, 6, 8]))

------------------------------------------------------------------
Task
------------------------------------------------------------------

(a) What does the buggy version actually return for [1, 2, 3, 4, 5, 6, 8], and why?

    Answer: 3. The condition "if n % 2 == 1" checks for odd numbers rather than even ones. Since an add number divided by 2 gives a remainder of 1, the list [1, 2, 3, 4, 5, 6, 8] contains the odd numbers - 1, 3, and 5, so the loop increments count exactly 3 times.

(b) Fix the bug. Write the corrected function below.
    (A one-character change is enough, but you must understand why.)

    def count_evens(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:  # Changed 1 to 0 to check for even numbers
            count = count + 1
    return count

    Changing the code "n % 2 == 1" to "n % 2 == 0" ensures the function checks if a number is even. For when an even number is divided by 2, its remainder is 0.
"""

def count_evens(numbers):
    # your corrected code here
    count = 0
    for n in numbers:
        if n % 2 == 0:  # Changed 1 to 0 to check for even numbers
            count = count + 1
    return count
print(count_evens([1, 2, 3, 4, 5, 6, 8]))

"""
(c) In one sentence, explain in plain English what `n % 2 == 0` checks.

    Answer: Changing the code "n % 2 == 1" to "n % 2 == 0" ensures the function checks if a number is even. For when an even number is divided by 2, its remainder is 0.
"""

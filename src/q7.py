"""
Question 7 — Python: Read and Predict Output  [Short Answer — Write Code]

AI tools can write code for you. This question checks something more important:
can you READ code and work out what it does? Do NOT run the code first. Read
it and predict the output by hand. (You may run it afterwards to check.)

------------------------------------------------------------------
Snippet 1
------------------------------------------------------------------
"""
numbers = [3, 8, 1, 9, 4]
total = 0
for n in numbers:
    if n > 4:
        total = total + n
print(total)

"""
(a) What does this print? Write the exact value.

    Answer: 17

(b) In one sentence, describe in plain English what this loop computes.

    Answer: The loop calculates the sum of all numbers in the list that are strictly greater than 4.

------------------------------------------------------------------
Snippet 2
------------------------------------------------------------------
"""
def greet(name="world"):
    return "Hello, " + name + "!"

print(greet())
print(greet("Ada"))

""""
(c) Write the two lines this program prints, in order.

    Answer:
    Line 1: Hello, world!
    Line 2: Hello, Ada!
"""

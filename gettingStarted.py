# Example Question 1: Is the Earth flat? - Yes/No
answer1 = input("Is the Earth flat? (Yes/No): ")

if answer1.lower() == "yes":
    result1 = "Incorrect"
else:
    result1 = "Correct"

# Example Question 2: Is water boiling at 100°C? - Yes/No
answer2 = input("Is water boiling at 100°C? (Yes/No): ")

if answer2.lower() == "yes":
    result2 = "Correct"
else:
    result2 = "Incorrect"

# Example Question 3: How many hours are in a day? - Numeric Answer
answer3 = int(input("How many hours are in a day? (Number): "))

if answer3 == 24:
    result3 = True  # True if the answer is correct
else:
    result3 = False  # False if the answer is incorrect

# Example Question 4: What is 5 + 5? - Numeric Answer
answer4 = int(input("What is 5 + 5? (Number): "))

if answer4 == 10:
    result4 = "Correct"
else:
    result4 = "Incorrect"

# Printing out results
print(f"Question 1 Answer: {result1}")
print(f"Question 2 Answer: {result2}")
print(f"Question 3 Answer: {result3}")
print(f"Question 4 Answer: {result4}")


# Objective: Write a program that takes a list of numbers and prints out the sum, average, and largest number in the list.



# Problem 1: Write a program that takes a list of numbers and prints out the sum of all the numbers in the list.



# Problem 2: Write a program that takes a list of numbers and prints out the average of all the numbers in the list.



# Problem 3: Write a program that takes a list of numbers and prints out the largest number in the list.

def calculate_stats(numbers):
    if not numbers:
        print("There's no number")
        return
    
    total = sum(numbers)
    average = total / len(numbers)
    largest = max(numbers)

    print(f"sum : {total}")
    print(f"average : {average}")
    print(f"the largest: {largest}")


numbers = [1, 2, 3, 4, 5]
calculate_stats(numbers)
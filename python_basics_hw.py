import random

# Create a list of 100 random numbers from 0 to 1000
random_numbers = [random.randint(0, 1000) for _ in range(100)]

# Sort the list from min to max without using sort()
for i in range(len(random_numbers)):
    for j in range(i + 1, len(random_numbers)):
        if random_numbers[i] > random_numbers[j]:
            random_numbers[i], random_numbers[j] = random_numbers[j], random_numbers[i]

# Initialize variables to calculate averages
even_sum = 0
even_count = 0
odd_sum = 0
odd_count = 0

# Calculate sum and count for even and odd numbers
for number in random_numbers:
    if number % 2 == 0:
        even_sum += number
        even_count += 1
    else:
        odd_sum += number
        odd_count += 1

# Calculate averages for even and odd numbers
even_average = even_sum / even_count if even_count != 0 else 0
odd_average = odd_sum / odd_count if odd_count != 0 else 0

# Print both average results in the console
print(f"Average of even numbers: {even_average}")
print(f"Average of odd numbers: {odd_average}")

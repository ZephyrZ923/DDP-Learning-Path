"""
Fibonacci Sequence Calculator Function

Objective:
Write a function named 'fibonacci_sequence' to generate the Fibonacci sequence up to a given number using a while loop.

Function Parameter:
1. max_value (integer): Maximum value for the Fibonacci sequence.

Instructions:
- Use a while loop to generate the Fibonacci sequence up to 'max_value'.
- Return the sequence as a list.
- Handle edge cases for 0 and negative inputs.

Example Test Cases:
1. fibonacci_sequence(10) should return the Fibonacci sequence up to 10.
2. fibonacci_sequence(1) should return the Fibonacci sequence up to 1.
3. fibonacci_sequence(0) should return a sequence with 0.
4. fibonacci_sequence(-5) should handle negative input.
"""

# 每个数字是前两个数字之和，起始于0和1

def fibonacci_sequence(max_value):
    # Your code goes here
    # Implement the Fibonacci sequence calculation using a while loop
   
    if max_value < 0:
        return "Invalid input"
    elif max_value == 0:
        return [0]
    

    
    # Initialize the Fibonacci sequence with the first two numbers
    sequence = [0, 1]
    
    # Generate the Fibonacci sequence up to max_value using a while loop
    while sequence[-1] + sequence[-2] <= max_value:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    
    return sequence





# Test cases
print(fibonacci_sequence(10))  # Expected: [0, 1, 1, 2, 3, 5, 8]
print(fibonacci_sequence(1))   # Expected: [0, 1, 1]
print(fibonacci_sequence(0))   # Expected: [0]
print(fibonacci_sequence(-5))  # Expected: Error message for negative input






# Test cases
print(fibonacci_sequence(10))  # Expected output: [0, 1, 1, 2, 3, 5, 8]
print(fibonacci_sequence(1))  # Expected output: [0, 1, 1]
print(fibonacci_sequence(0))  # Expected output: [0]
print(fibonacci_sequence(-5))  # Expected: Empty list or error message

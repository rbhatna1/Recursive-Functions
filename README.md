# Recursive-Functions

## Overview
This Python program provides a menu-driven interface for performing various recursive functions and number operations. Users can calculate factorials, sums, powers, check for prime numbers, find the GCD, generate tables, reverse numbers, generate Fibonacci series, create patterns, convert numbers between different bases, and search for elements in a list.

## Functions

### `space()`
- **Description**: Prints a decorative separator to enhance the readability of the output.

### `fact(m, n)`
- **Description**: Calculates and prints the factorial of numbers in the range from `m` to `n`.
- **Parameters**:
  - `m` (int): The lower bound of the range.
  - `n` (int): The upper bound of the range.

### `sum(number)`
- **Description**: Recursively calculates the sum of the first `number` natural numbers.
- **Parameters**:
  - `number` (int): The number of natural numbers to sum.
- **Returns**: The sum of the first `number` natural numbers.

### `power(m, n)`
- **Description**: Recursively calculates `m` raised to the power of `n`.
- **Parameters**:
  - `m` (int): The base number.
  - `n` (int): The exponent.
- **Returns**: The result of `m` raised to the power of `n`.

### `prime(number, div=2)`
- **Description**: Recursively checks if a number is prime.
- **Parameters**:
  - `number` (int): The number to check.
  - `div` (int, optional): The current divisor (default is 2).

### `GCD(number1, number2)`
- **Description**: Recursively calculates the GCD of two numbers using Euclid's Algorithm.
- **Parameters**:
  - `number1` (int): The first number.
  - `number2` (int): The second number.
- **Returns**: The GCD of the two numbers.

### `tables1(number, times=1)`
- **Description**: Recursively prints the multiplication table for the given number up to 10 times.
- **Parameters**:
  - `number` (int): The number for which to print the table.
  - `times` (int, optional): The current multiplier (default is 1).

### `rev(a)`
- **Description**: Recursively reverses a string and prints it.
- **Parameters**:
  - `a` (str): The string to reverse.

### `palindrome(string)`
- **Description**: Recursively checks if a string is a palindrome.
- **Parameters**:
  - `string` (str): The string to check.

### `feb1(n)`
- **Description**: Generates the first `n` Fibonacci numbers.
- **Parameters**:
  - `n` (int): The number of Fibonacci numbers to generate.

### `pat1(n, x=1, z="*")`
- **Description**: Recursively prints a pattern of stars.
- **Parameters**:
  - `n` (int): The number of lines to print.
  - `x` (int, optional): The current line number (default is 1).
  - `z` (str, optional): The character to print (default is "*").

### `pat2(n)`
- **Description**: Prints a pattern of numbers.
- **Parameters**:
  - `n` (int): The number of lines to print.

### `pat3()`
- **Description**: Prints a pattern of numbers from 5 to 1.

### `dec_bin(n)`
- **Description**: Recursively converts a decimal number to binary and prints it.
- **Parameters**:
  - `n` (int): The decimal number to convert.

### `dec_oct(n)`
- **Description**: Recursively converts a decimal number to octal and prints it.
- **Parameters**:
  - `n` (int): The decimal number to convert.

### `dec_hex(dec)`
- **Description**: Recursively converts a decimal number to hexadecimal and prints it.
- **Parameters**:
  - `dec` (int): The decimal number to convert.

### `hex_dec(dec)`
- **Description**: Converts a hexadecimal number to decimal.
- **Parameters**:
  - `dec` (str): The hexadecimal number to convert.

### `bin_dec(x, s=0, c=0)`
- **Description**: Recursively converts a binary number to decimal.
- **Parameters**:
  - `x` (int): The binary number to convert.
  - `s` (int, optional): The current sum (default is 0).
  - `c` (int, optional): The current position (default is 0).
- **Returns**: The decimal equivalent of the binary number.

### `oct_dec(x, s=0, c=0)`
- **Description**: Recursively converts an octal number to decimal.
- **Parameters**:
  - `x` (int): The octal number to convert.
  - `s` (int, optional): The current sum (default is 0).
  - `c` (int, optional): The current position (default is 0).
- **Returns**: The decimal equivalent of the octal number.

### `bsearch(ar1, val, low, high)`
- **Description**: Recursively performs a binary search on a sorted list.
- **Parameters**:
  - `ar1` (list): The list to search.
  - `val` (int): The value to search for.
  - `low` (int): The lower bound of the search range.
  - `high` (int): The upper bound of the search range.
- **Returns**: The index of the value in the list, or None if not found.

### `linearsearch(list, val, x=0)`
- **Description**: Recursively performs a linear search on a list.
- **Parameters**:
  - `list` (list): The list to search.
  - `val` (int): The value to search for.
  - `x` (int, optional): The current index (default is 0).
- **Returns**: True if the value is found, False otherwise.

### `sumdigits(list, s=0, x=0)`
- **Description**: Recursively calculates the sum of digits in a list.
- **Parameters**:
  - `list` (list): The list of digits to sum.
  - `s` (int, optional): The current sum (default is 0).
  - `x` (int, optional): The current index (default is 0).
- **Returns**: The sum of the digits in the list.

## Menu Options

1. **Find the Factorial of a Number**:
   - Prompts the user to input a range and calculates the factorial of each number in the range.

2. **Find the Sum of the First `n` Natural Numbers**:
   - Prompts the user to input a number and calculates the sum of the first `n` natural numbers.

3. **Find the Power of a Number**:
   - Prompts the user to input a base number and an exponent, then calculates the result.

4. **Check if a Number is Prime**:
   - Prompts the user to input a number and checks if it is a prime number.

5. **Find the GCD of Two Numbers**:
   - Prompts the user to input two numbers and calculates their GCD.

6. **Generate the Multiplication Table for a Number**:
   - Prompts the user to input a number and prints its multiplication table up to 10.

7. **Reverse a String and Check if it is a Palindrome**:
   - Prompts the user to input a string, reverses it, and checks if it is a palindrome.

8. **Generate the Fibonacci Series**:
   - Prompts the user to input a number and generates the Fibonacci series up to that number.

9. **Generate the First Pattern**:
   - Prompts the user to input a number and generates a star pattern.

10. **Generate the Second Pattern**:
    - Prompts the user to input a number and generates a pattern of numbers.

11. **Generate the Third Pattern**:
    - Generates a pattern of numbers from 5 to 1.

12. **Convert Decimal to Binary**:
    - Prompts the user to input a decimal number and converts it to binary.

13. **Convert Decimal to Octal**:
    - Prompts the user to input a decimal number and converts it to octal.

14. **Convert Decimal to Hexadecimal**:
    - Prompts the user to input a decimal number and converts it to hexadecimal.

15. **Convert Binary to Decimal**:
    - Prompts the user to input a binary number and converts it to decimal.

16. **Convert Octal to Decimal**:
    - Prompts the user to input an octal number and converts it to decimal.

17. **Convert Hexadecimal to Decimal**:
    - Prompts the user to input a hexadecimal number and converts it to decimal.

18. **Perform a Linear Search**:
    - Prompts the user to input a list and a value, then performs a linear search to find the value.

19. **Perform a Binary Search**:
    - Prompts the user to input a sorted list and a value, then performs a binary search to find the value.

20. **Calculate the Sum of Digits in a List**:
    - Prompts the user to input a list of digits and calculates the sum.

21. **Exit the Program**:
    - Exits the program.

## How to Run the Program

1. Run the script.
2. Follow the on-screen menu options.
3. Enter your choice (1-21) and input the required values as prompted.
4. The program will continue to prompt for input until you choose to exit by entering 21.

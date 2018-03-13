"""
For each number below 100, this script returns the number
or 'Buzz' if the number is a multiple of 5
or 'Fizz' if the number is a multiple of 3
or 'FizzBuzz' if the number is a multiple of 3 and 5.
"""

for elt in range(1, 101):
    if (elt%3) == 0:
        if (elt%5) == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif (elt%5) == 0:
        print("Buzz")
    else:
        print(elt)

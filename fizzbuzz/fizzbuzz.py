"""Main FizzBuzz module"""

from .config import config

def play_fizzbuzz(start: int = 1, end: int = 20, divisors: dict = None) -> list:
    """Play the FizzBuzz Game

    Parameters:
        start (int): The integer to start counting from (default = 1)
        end (int): The integer to finish counting at (default = 20)
        divisors (dict): A dictionary of divisors and their replacement strings (default = None)

    Returns:
        final_output (list): A list of strings containing each number or it's replacement
    """

    # if no divisors are passed, use defaults from config
    # this prevents dangerous default parameters
    if divisors is None:
        divisors = config["divisors"]

    # Sanity checks
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError('start and end must be integers')
    if not isinstance(divisors, dict):
        raise TypeError('divisors must be a valid dictionary')
    if start <= 0:
        raise ValueError('start must be greater than 0')
    if end <= start:
        raise ValueError('end must be greater than start')
    if len(divisors.keys()) == 0:
        raise ValueError('divisors dict cannot be empty')

    # initialise the final output
    final_output = []

    # main loop
    for i in range(start, end + 1):
        # temp variable to hold the output of this loop
        loop_output = ''

        # check if i is divisible by each divisor in the dict
        # if yes, append the replacement string to the loop var
        for divisor in divisors:
            if i % divisor == 0:
                loop_output += divisors[divisor]

        # check if we have made any replacements
        # if no (loop_output is still empty), then append the string of i to the final_output list
        # if yes, then append the loop_output replacement string to the final_output list
        if loop_output == '':
            final_output.append(str(i))
        else:
            final_output.append(loop_output)

    return final_output

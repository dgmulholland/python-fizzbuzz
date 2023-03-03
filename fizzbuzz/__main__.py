"""Executed if the package is run directly"""

import argparse
from ast import literal_eval
from fizzbuzz import play_fizzbuzz

# create argument parser for the divisor dictionary
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--start', type=int, help='The number to start counting from', default=1)
parser.add_argument('-e','--end', type=int, help='The number to finish counting at', default=20)
parser.add_argument('-d', '--divisors', type=str, help='A string representation of the divisors dictionary', default='None')

args = parser.parse_args()

for item in play_fizzbuzz(start=args.start, end=args.end, divisors=literal_eval(args.divisors)):
    print(item)

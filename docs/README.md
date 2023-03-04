# FizzBuzz

This module implements the classic FizzBuzz problem in python.

## About

FizzBuzz is a game where players take turns to count in sequence from 1 to an arbitrary number. If the number is a multiple of 3, they say 'Fizz' and if it is a multiple of 5 they say 'Buzz'. If the number is a multiple of both 3 and 5 (eg. 15) they say 'FizzBuzz'.

## Usage

This module can be run directly, imported and accessed, or run as a docker container with the included Dockerfile.

When run directly it will play the FizzBuzz game with the default rules above, count from 1 to 20 and output each number on a new line. However the user can make use of the ```-s/--start```, ```-e/--end``` and ```-d/--divisors``` arguments to pass start value, end value and a dictionary of divisors to the game.

If the module is imported it can be called with specific arguments for the start & end count numbers, and a dictionary of divisors & string that should should replace numbers that are multiples of the divisor. When imported it will return a list containing the numbers as list elements.

If the module is run as a docker container it will function as if called directly and arguments can be passed on the command line. The divisors argument should be enclosed in quotes.

## Examples

Run directly:

```python
python3 -m fizzbuzz
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
```

or

```python
python3 -m fizzbuzz --start 10 --end 50 --divisors '{4: "Foo", 12: "Bar"}'
10
11
FooBar
13
14
15
Foo
17
18
19
Foo
21
22
23
FooBar
25
26
27
Foo
29
30
31
Foo
33
34
35
FooBar
37
38
39
Foo
41
42
43
Foo
45
46
47
FooBar
49
50
```

Imported:

```python
>>> import fizzbuzz
>>> fizzbuzz.play_fizzbuzz()
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz']
```

or

```python
>>> import fizzbuzz
>>> fizzbuzz.play_fizzbuzz(1, 20, {3: 'Foo', 5: 'Bar'})
['1', '2', 'Foo', '4', 'Bar', 'Foo', '7', '8', 'Foo', 'Bar', '11', 'Foo', '13', '14', 'FooBar', '16', '17', 'Foo', '19', 'Bar']
```

Docker:

```bash
docker build . -t fizzbuzz
docker run --rm fizzbuzz
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
```

or

```bash
docker build . -t fizzbuzz
docker run --rm fizzbuzz --start 5 --end 27 --divisors '{6: "Foo", 8: "Bar"}'
5
Foo
7
Bar
9
10
11
Foo
13
14
15
Bar
17
Foo
19
20
21
22
23
FooBar
25
26
27
```

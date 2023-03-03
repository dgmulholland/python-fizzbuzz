"""Test the FizzBuzz game"""

import pytest
import fizzbuzz

# test types
def test_fizzbuzz_types():
    """Test the expected errors when passing incorrect parameter types"""
    with pytest.raises(TypeError):
        fizzbuzz.play_fizzbuzz('fred', 20)
    with pytest.raises(TypeError):
        fizzbuzz.play_fizzbuzz(1, 20.5)
    with pytest.raises(TypeError):
        fizzbuzz.play_fizzbuzz(10, 20, 'not a dict')
    with pytest.raises(ValueError):
        fizzbuzz.play_fizzbuzz(0)
    with pytest.raises(ValueError):
        fizzbuzz.play_fizzbuzz(-10)
    with pytest.raises(ValueError):
        fizzbuzz.play_fizzbuzz(10, 5)
    with pytest.raises(ValueError):
        fizzbuzz.play_fizzbuzz(10, -10)
    with pytest.raises(ValueError):
        fizzbuzz.play_fizzbuzz(10, 20, {})


def test_fizzbuzz_defaults():
    """Test FizzBuzz works using the default parameters"""
    output = fizzbuzz.play_fizzbuzz()
    assert output == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz',
                    'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz']


def test_fizzbuzz_custom():
    """Test FizzBuzz gives coprrect output when passed custom parameters"""
    output = fizzbuzz.play_fizzbuzz(1, 20, {3: 'Foo', 5: 'Bar'})
    assert ['1', '2', 'Foo', '4', 'Bar', 'Foo', '7', '8', 'Foo', 'Bar',
            '11', 'Foo', '13', '14', 'FooBar', '16', '17', 'Foo', '19', 'Bar']

    output = fizzbuzz.play_fizzbuzz(25, 100)
    assert output[10 == 'Buzz']
    assert output[20] == 'FizzBuzz'
    assert output[49] == '74'

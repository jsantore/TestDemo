import math
import numbers
import sys


def simple_distance(x1:float, y1:float, x2:float, y2:float):
    delta_x = x1-x2
    delta_y = y1-y2
    return math.sqrt(delta_x**2 + delta_y*2) # oops I made a mistake


def add_interest(principle, rate):
    """
    Demo function that doesn't use typehints
    makes sure that no one is passting non numbers
        add a change to doc string
    :param principle: the principle balance of the account
    :param rate: The interest rate on the account
    :return: the new balance of the account
    """
    if not isinstance(principle, numbers.Number):
        raise TypeError("the principle should be a floating point value")
    # more error checking we want the interest rate as a real number from 0 to 1
    if rate < 0 or rate > 1:
        raise ValueError("The interest rate needs to be a real number from 0 to 1")
    new_balance = principle + principle*rate
    return new_balance


def show_output(initial_bal, rate):
    # this is hard to test

    balance = add_interest(initial_bal, rate)
    print(f"Your new balance is ${balance}")


def testable_show_output(initial_bal, rate, outfile):
    balance = add_interest(initial_bal, rate)
    if not outfile:
        outfile = sys.stdout
    print(f"Your new balance is ${balance}", file=outfile)


if __name__ == '__main__':
    # test the functions if running this as the main file
    print(add_interest(100, .05))
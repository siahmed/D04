#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    # looks like nothing is wrong
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    # difference between c and 'c' makes the function return the wrong result
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    # only responds to last letter in word, thus if all previous letters are lowercase and the function should return True, if the last letter is uppercase it will incorrectly return False
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    # works fine
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    # returns False for both an all-lowercase word and an all-uppercase word, which means it's not checking if any are lowercase but rather if all are lowercase
    for c in s:
        if not c.islower():
            return False
    return True


###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    # print("Hello World!")


if __name__ == '__main__':
    main()

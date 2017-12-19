""" hw1_9 """


def appendsums(lst):
    """ Repeatedly append the sum of the
    current last three elements of lst to lst. """
    lst.append(sum(lst[-3:]))


def main():
    """ Main """
    sum_three = [0, 1, 2]
    for _ in range(25):
        appendsums(sum_three)
    print sum_three[20]


main()

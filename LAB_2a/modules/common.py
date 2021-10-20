import datetime
import sys
import logging


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform


def filtr_number(filtr):
    numbers = range(0, 101)
    if filtr == "True":
        output = "Even number: "
    elif filtr == "False":
        output = "Odd number: "

    for num in numbers:
        if (filtr == "True") & (num % 2 == 0):
            output += str(num) + " "
        elif (filtr == "False") & (num % 2 != 0):
            output += str(num) + " "
    return output


def view_array():
    x = [1, 2, 3, 4]
    print("Масив X[]:", x)
    index = int(input("Enter number of element: "))
    try:
        print(f"X[{index}] = {x[index]}")
    except IndexError:
        logging.error("Out of range")
    else:
        logging.info("Correct!!!")

# All functions taken from "Python Numerical Methods", Kong, Siauw and Bayen 
# https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html
import pytest

def my_adder(a, b, c):
    """
    function to sum the 3 numbers
    Input: 3 numbers a, b, c
    Output: the sum of a, b, and c
    author:
    date:
    """
    
    # this is the summation
    out = a + b + c
    
    return out


def my_thermo_stat(temp, desired_temp):
    """
    Changes the status of the thermostat based on 
    temperature and desired temperature
    author
    date
    :type temp: Int
    :type desiredTemp: Int
    :rtype: String
    """
    if temp < desired_temp - 5:
        status = 'Heat'
    elif temp > desired_temp + 5:
        status = 'AC'
    else:
        status = 'off'
    return status
    
 
def have_digits(s):
    """
    Checks if a string has digits in it
    """
    
    out = 0
    
    # loop through the string
    for c in s:
        # check if the character is a digit
        if c.isdigit():
            out = 1
            break
            
    return out
    
 # define the area of a rectangle
def area_of_rectangle(width, height):
    """
    function to calculate the area of a rectangle
    Input: width and height of the rectangle
    Output: area of the rectangle
    """
        
        # this is the area
    out = width * height
    return out

# define the perimeter of a rectangle
def perimeter_of_rectangle(width, height):
    """
    function to calculate the perimeter of a rectangle
    Input: width and height of the rectangle
    Output: perimeter of the rectangle
    """
    
    # this is the perimeter
    out = 2 * (width + height)
    
    return out

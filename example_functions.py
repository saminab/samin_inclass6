# All functions taken from "Python Numerical Methods", Kong, Siauw and Bayen 
# https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html
import pytest

def my_adder(a:float, b:float, c:float) -> float:
    """
    function to sum the 3 numbers
    args: a, b, c
    return: the sum of a, b, and c
    author:Samin Ab
    date:2024-09-20
    """
    
    # this is the summation
    out = a + b + c
    
    return out


def my_thermo_stat(temp:int, desired_temp:int) -> str:
    """
    Changes the status of the thermostat based on 
    temperature and desired temperature
    args: temp, desired_temp
    return: status
    author: Samin Ab
    date: 2024-09-20
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
    args: s
    return: 1 if there are digits in s, 0 otherwise
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
def area_of_rectangle(width:int, height:int) -> int:
    """
    function to calculate the area of a rectangle
    args: width, height
    return: area of the rectangle
    
    """
        
        # this is the area
    out = width * height
    return out

# define the perimeter of a rectangle
def perimeter_of_rectangle(width:int, height:int) -> int:
    """
    function to calculate the perimeter of a rectangle
    args: width, height
    return: perimeter of the rectangle

    """
    
    # this is the perimeter
    out = 2 * (width + height)
    
    return out

"""Calculator testing"""
from calculator.main import Calculator

def test_calculator_result():
    """testing calculator result is 1"""
    calc = Calculator()
    assert calc.result == 1

def test_calculator_add():
    """Test the Addition function of the calculator"""
    #Arrange by instantiating the calc class
    calc = Calculator()
    #Act by calling the method to be tested
    calc.add_number(5)
    #Assert that the results are correct
    assert calc.result == 6

def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc = Calculator()
    assert calc.get_result() == 1

def test_calculator_subtract():
    """Test the subtraction method of the calculator"""
    calc = Calculator()
    calc.subtract_number(4)
    assert calc.get_result() == -3
def test_calculator_multiply():
    """ testing multiplication of two numbers"""
    calc = Calculator()
    result  = calc.multiply_numbers(2,2)
    assert result == 4
def test_calculator_divide():
    """ tests division of two numbers"""
    calc = Calculator()
    result = calc.divide_numbers(2,2)
    assert result == 1

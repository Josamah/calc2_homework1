""" This is the increment function"""
class Calculator:
    """ This is the Calculator class"""

    result = 1
    def get_result(self):
        """ Get Results of Calculation"""
        return self.result

    def add_number(self, value_a):
        """ adding number to result"""
        self.result = self.result + value_a
        return self.result
    def subtract_number(self, value_a):
        """ subtracting number from result"""
        self.result = self.result - value_a
        return self.result
    def multiply_numbers(self, value_a, value_b):
        """ multiplying two numbers and store the result"""
        self.result = value_a * value_b
        return self.result
    def divide_numbers(self, value_a, value_b):
        """dividing two numbers and store the results"""
        self.result = value_a / value_b
        return self.result

from src import oneclass, twoclass
from contracts import contract


class Super(oneclass.One, twoclass.Two):
    @contract(number_one='int,>0', number_two='int,>0')
    def __init__(self, number_one, number_two):
        self.number_one = number_one
        self.number_two = number_two

    @contract(returns='int,>0')
    def function_super(self):
        return self.number_one + self.number_two

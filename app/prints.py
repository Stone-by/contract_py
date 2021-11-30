from src import superclass, oneclass, twoclass


class Prints:
    def print_now(self):
        one = oneclass.One()
        one
        two = twoclass.Two()
        two
        point = superclass.Super(0, 1)
        point.function_super()



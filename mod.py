from contracts import contract


@contract(returns='int,>0')
def foo():
    return 0


if __name__ == '__main__':
    foo()

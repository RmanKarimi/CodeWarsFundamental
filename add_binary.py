"""
  function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.
 """


def add_binary(a, b):
    return bin(a + b)[2:]
    # return '{0:b}'.format(a + b)

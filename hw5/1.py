import math
def my_log(n):
    print([math.log(x) if x > 0 else None for x in n])
my_log([1, 3, 2.5, -1, 9, 0, 2.71])

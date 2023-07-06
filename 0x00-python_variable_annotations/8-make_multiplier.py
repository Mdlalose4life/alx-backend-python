#!/usr/bin/env python3


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Type-annotated function make_multiplier that
    takes a float multiplier as an argument and returns a
    function hat multiplies a float by multiplier.
    '''
    def multiplier_func(x: float) -> float:
        return x * multiplier

    return multiplier_func


# Annotating a variable as a callable (function) value
x:  Callable[[float], float] = make_multiplier(2.0)

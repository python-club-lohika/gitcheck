'''
Created on Nov 6, 2014

@author: avasilyev2
'''
import pytest
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
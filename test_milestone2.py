import pytest
from main.py import *
def test_load():
    load(21)
    assert acc == 21

test_load()
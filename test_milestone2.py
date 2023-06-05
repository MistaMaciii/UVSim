import pytest
import main
def test_load():
    main.load(21)
    assert main.acc == 21

test_load()

import pytest
import main
def test_load():
    global acc
    main.acc = "+0000"

    global mem
    main.mem = ['1000','1001','1002','1003','1004','1005','1006','1007','1008','1009','1010','1011']    #initializes the 
    main.load(6)
    assert main.acc == "1006"

test_load()

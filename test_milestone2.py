import pytest
import main
#You will also create a spreadsheet that lists the unit tests in row/column form.  
#Give each unit test a name, short description, the reference to the appropriate use case, inputs, 
#expected outputs, and how you know whether the test succeeded or failed.

def test_load_pass():
    main.acc = "+0000"
    main.mem = ['1000','1001','1002','1003','1004','1005','1006','1007','1008','1009','1010','1011']   
    main.load(6)
    assert main.acc == "1006"

def test_load_fail():
    global acc
    main.acc = "+0000"

    global mem
    main.mem = ['1000','1001','1002','1003','1004','1005','1006','1007','1008','1009','1010','1011']
    with pytest.raises(IndexError):
        main.load(13)
    assert main.acc == "+0000"

def test_store_pass():
    global acc
    main.acc = "+1345"

    global mem
    main.mem = ['1000','1001','1002','1003','1004','1005','1006','1007','1008','1009','1010','1011']
    main.store(6)
    assert main.mem[6] == "+1345"

def test_store_fail():
    global acc
    main.acc = "+1345"

    global mem
    main.mem = ['1000','1001','1002','1003','1004','1005','1006','1007','1008','1009','1010','1011']
    with pytest.raises(IndexError):
        main.store(-1)
    assert main.mem[6] == "1006"

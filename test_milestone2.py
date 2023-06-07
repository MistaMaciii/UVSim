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
    main.acc = "+0000"
    main.mem = ['1000','1001','1002','1003','1004','1005','1006','1007','1008','1009','1010','1011']
    with pytest.raises(IndexError):
        main.load(13)
    assert main.acc == "+0000"

def test_store_pass():
    main.acc = "+1345"
    main.mem = ['1000','1001','1002','1003','1004','1005','1006','1007','1008','1009','1010','1011']
    main.store(6)
    assert main.mem[6] == "+1345"

def test_store_fail():
    main.acc = "+1345"
    main.mem = ['1000','1001','1002','1003','1004','1005','1006','1007','1008','1009','1010','1011']
    with pytest.raises(TypeError):
        main.store("a")
    assert main.mem[6] == "1006"

def test_write_pass():
    main.mem = ['1000','1001','1002','1003','1004','1005','1006','1007','1008','1009','1010','1011']
    assert main.write(3) == "1003"

def test_write_fail():
    main.mem = ['1000','1001','1002','1003','1004','1005','1006','1007','1008','1009','1010','1011']
    with pytest.raises(IndexError):
        main.write(20)

def test_read_pass(monkeypatch):
    main.mem = ['1000','1001','1002','1003','1004','1005','1006','1007','1008','1009','1010','1011']
    monkeypatch.setattr('builtins.input', lambda _: "+1097")
    main.read(5)
    assert main.mem[5] == "+1097"

def test_read_fail(monkeypatch):
    main.mem = ['1000','1001','1002','1003','1004','1005','1006','1007','1008','1009','1010','1011']
    monkeypatch.setattr('builtins.input', lambda _: "+1097")
    with pytest.raises(IndexError):
        main.read(20)

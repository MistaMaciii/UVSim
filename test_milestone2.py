import pytest
import main
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
def test_addit_pass():
    main.acc = "-1234"
    main.mem = [+0000, +0000]  
    main.addit(1)
    assert main.acc == -1234
def test_addit_fail():
    main.acc = "40000"
    main.mem = [+0000, +1234]  
    main.addit(1)
    assert main.acc == +1234
def test_sub_pass():
    main.acc = "0000"
    main.mem = [+0000, -1234]  
    main.sub(1)
    assert main.acc == +1234
def test_sub_fail():
    main.acc = "-5678"
    main.mem = [+0000, +5678]  
    main.sub(1)
    assert main.acc == -1356
def test_div_pass():
    main.acc = "0000"
    main.mem = [+0000, +1000]  
    main.div(1)
    assert main.acc == 0
def test_div_fail():
    main.acc = "-1234"
    main.mem = [+0000, +0000]  
    with pytest.raises(ZeroDivisionError):
        main.div(1)
def test_mult_pass():
    main.acc = "+1234"
    main.mem = [+0000, +0000]  
    main.mult(1)
    assert main.acc == +0000
def test_mult_fail():
    main.acc = "4444"
    main.mem = [+0000, +4444]  
    main.mult(1)
    assert main.acc == +9136
def test_branch_pass():
    main.ip = 0
    main.acc = 0
    main.mem = ['1110','1109','1108','1107','1106','4006','1110', '-99999']
    main.branch(6)
    assert main.ip == 5
def test_branch_fail():
    main.ip = 0
    main.acc = 0
    main.mem = ['1110','1109','1108','1107','1106','4006','1110', '-99999']
    with pytest.raises(IndexError):
        main.branch(20)
def test_branch_neg_pass():
    main.ip = 0
    main.acc = -1745
    main.mem = ['1110','1109','1108','1107','4106','1106','1110','1110','1110','-99999']
    main.branch_neg(3)
    assert main.ip == 2
def test_branch_neg_fail():
    main.ip = 0
    main.acc = -9999
    main.mem = ['1110','1109','1108','1107','4106','1110','1110','1110','1110','-99999']
    with pytest.raises(IndexError):
        main.branch_neg(20)
def test_branch_zero_pass():
    main.ip = 0
    main.acc = 0
    main.mem = ['1110','4206','1108','1107','1106','1110','1110','1110','-99999']
    main.branch_zero(6)
    assert main.ip == 5
def test_branch_zero_fail():
    main.ip = 0
    main.acc= 0
    main.mem = ['1110','4206','1108','1107','1100','4206','1110','1110', '4007' '-99999']
    with pytest.raises(IndexError):
        main.branch_zero(20)
def test_halt_pass():
    main.ip = 0
    main.acc = 0
    main.mem = ['4300','4200','1108','1107','1106','1110','1110','1110','-99999']
    main.halt()
    assert main.halt_status == True
if __name__ == '__main__': pytest.main()
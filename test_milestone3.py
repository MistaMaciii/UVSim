import pytest
from Operations import Arithmetic_Operations
from Operations import Control_Operations
from Operations import IO_Operations
from Operations import LoadStore_Operations
import UVSim
def test_load_pass():
    uvSim = UVSim.UVSim()
    uvSim.acc = "+0000"
    uvSim.mem = ['1000','1001','1002','1003','1004','1005','1006','1007','1008','1009','1010','1011']   
    LoadStore_Operations.LoadStore_Operations.load(6, uvSim)
    assert uvSim.acc == "1006"
def test_load_fail():
    uvSim = UVSim.UVSim()
    uvSim.acc = "+0000"
    uvSim.mem = ['1000','1001','1002','1003','1004','1005','1006','1007','1008','1009','1010','1011']
    with pytest.raises(IndexError):
        LoadStore_Operations.LoadStore_Operations.load(13, uvSim)
    assert uvSim.acc == "+0000"
def test_store_pass():
    uvSim = UVSim.UVSim()
    uvSim.acc = "+1345"
    uvSim.mem = ['1000','1001','1002','1003','1004','1005','1006','1007','1008','1009','1010','1011']
    LoadStore_Operations.LoadStore_Operations.store(6, uvSim)
    assert uvSim.mem[6] == "+1345"
def test_store_fail():
    uvSim = UVSim.UVSim()
    uvSim.acc = "+1345"
    uvSim.mem = ['1000','1001','1002','1003','1004','1005','1006','1007','1008','1009','1010','1011']
    with pytest.raises(TypeError):
        LoadStore_Operations.LoadStore_Operations.store('a', uvSim)
    assert uvSim.mem[6] == "1006"
def test_write_pass():
    uvSim = UVSim.UVSim()
    uvSim.mem = ['1000','1001','1002','1003','1004','1005','1006','1007','1008','1009','1010','1011']
    assert IO_Operations.IO_Operations.write(3, uvSim) == "1003"
def test_write_fail():
    uvSim = UVSim.UVSim()
    uvSim.mem = ['1000','1001','1002','1003','1004','1005','1006','1007','1008','1009','1010','1011']
    with pytest.raises(IndexError):
        IO_Operations.IO_Operations.write(20, uvSim)
def test_read_pass(monkeypatch):
    uvSim = UVSim.UVSim()
    uvSim.mem = ['1000','1001','1002','1003','1004','1005','1006','1007','1008','1009','1010','1011']
    monkeypatch.setattr('builtins.input', lambda _: "+1097")
    IO_Operations.IO_Operations.read(5, uvSim)
    assert uvSim.mem[5] == "+1097"
def test_read_fail(monkeypatch):
    uvSim = UVSim.UVSim()
    uvSim.mem = ['1000','1001','1002','1003','1004','1005','1006','1007','1008','1009','1010','1011']
    monkeypatch.setattr('builtins.input', lambda _: "+1097")
    with pytest.raises(IndexError):
        IO_Operations.IO_Operations.read(20, uvSim)
def test_addit_pass():
    uvSim = UVSim.UVSim()
    uvSim.acc = "-1234"
    uvSim.mem = [+0000, +0000]  
    Arithmetic_Operations.Arithmetic_Operations.addit(1, uvSim)
    assert uvSim.acc == -1234
def test_addit_fail():
    uvSim = UVSim.UVSim()
    uvSim.acc = "40000"
    uvSim.mem = [+0000, +1234]  
    Arithmetic_Operations.Arithmetic_Operations.addit(1, uvSim)
    assert uvSim.acc == +1234
def test_sub_pass():
    uvSim = UVSim.UVSim()
    uvSim.acc = "0000"
    uvSim.mem = [+0000, -1234]  
    Arithmetic_Operations.Arithmetic_Operations.sub(1, uvSim)
    assert uvSim.acc == +1234
def test_sub_fail():
    uvSim = UVSim.UVSim()
    uvSim.acc = "-5678"
    uvSim.mem = [+0000, +5678]  
    Arithmetic_Operations.Arithmetic_Operations.sub(1, uvSim)
    assert uvSim.acc == -1356
def test_div_pass():
    uvSim = UVSim.UVSim()
    uvSim.acc = "0000"
    uvSim.mem = [+0000, +1000]  
    Arithmetic_Operations.Arithmetic_Operations.div(1, uvSim)
    assert uvSim.acc == 0
def test_div_fail():
    uvSim = UVSim.UVSim()
    uvSim.acc = "-1234"
    uvSim.mem = [+0000, +0000]  
    with pytest.raises(ZeroDivisionError):
        Arithmetic_Operations.Arithmetic_Operations.div(1, uvSim)
def test_mult_pass():
    uvSim = UVSim.UVSim()
    uvSim.acc = "+1234"
    uvSim.mem = [+0000, +0000]  
    Arithmetic_Operations.Arithmetic_Operations.mult(1, uvSim)
    assert uvSim.acc == +0000
def test_mult_fail():
    uvSim = UVSim.UVSim()
    uvSim = UVSim.UVSim()
    uvSim.acc = "4444"
    uvSim.mem = [+0000, +4444]  
    Arithmetic_Operations.Arithmetic_Operations.mult(1, uvSim)
    assert uvSim.acc == +9136
def test_branch_pass():
    uvSim = UVSim.UVSim()
    uvSim.ip = 0
    uvSim.acc = 0
    uvSim.mem = ['1110','1109','1108','1107','1106','4006','1110', '-99999']
    Control_Operations.Control_Operations.branch(6, uvSim)
    assert uvSim.ip == 5
def test_branch_fail():
    uvSim = UVSim.UVSim()
    uvSim.ip = 0
    uvSim.acc = 0
    uvSim.mem = ['1110','1109','1108','1107','1106','4006','1110', '-99999']
    with pytest.raises(IndexError):
        Control_Operations.Control_Operations.branch(20, uvSim)
def test_branch_neg_pass():
    uvSim = UVSim.UVSim()
    uvSim.ip = 0
    uvSim.acc = -1745
    uvSim.mem = ['1110','1109','1108','1107','4106','1106','1110','1110','1110','-99999']
    Control_Operations.Control_Operations.branch_neg(3, uvSim)
    assert uvSim.ip == 2
def test_branch_neg_fail():
    uvSim = UVSim.UVSim()
    uvSim.ip = 0
    uvSim.acc = -9999
    uvSim.mem = ['1110','1109','1108','1107','4106','1110','1110','1110','1110','-99999']
    with pytest.raises(IndexError):
        Control_Operations.Control_Operations.branch_neg(20, uvSim)
def test_branch_zero_pass():
    uvSim = UVSim.UVSim()
    uvSim.ip = 0
    uvSim.acc = 0
    uvSim.mem = ['1110','4206','1108','1107','1106','1110','1110','1110','-99999']
    Control_Operations.Control_Operations.branch_zero(6, uvSim)
    assert uvSim.ip == 5
def test_branch_zero_fail():
    uvSim = UVSim.UVSim()
    uvSim.ip = 0
    uvSim.acc= 0
    uvSim.mem = ['1110','4206','1108','1107','1100','4206','1110','1110', '4007' '-99999']
    with pytest.raises(IndexError):
        Control_Operations.Control_Operations.branch_zero(20, uvSim)
def test_halt_pass():
    uvSim = UVSim.UVSim()
    uvSim.ip = 0
    uvSim.acc = 0
    uvSim.mem = ['4300','4200','1108','1107','1106','1110','1110','1110','-99999']
    Control_Operations.Control_Operations.halt(uvSim)
    assert uvSim.halt_status == True
import disconv as foo

def test_tonum():
    assert foo.tonum([213,21541,65,47,[['g']],{1:'s'}])==[213, 21541, 65, 47, [[103]], {1: 115}]

def test_tofloat():
    assert foo.tofloat([213,21541,65,47,[['g']],{1:'s'}])==[213.0, 21541.0, 65.0, 47.0, [[[103.0]]], {1: [115.0]}]
def test_tostr():
    assert foo.tostr([213,21541,65,47,[['g']],{1:'s'}])==['213','21541','65','47',[['g']],{1:'s'}]
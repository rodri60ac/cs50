from numb3rs import validate

def test_format1():
    assert validate("255.255.255.255") == True
def test_format2():
    assert validate("1.1.1.1") == True
def test_format3():
    assert validate("1.2.3") == False

def test_range1():
    assert validate("255.0.255.0") == True

def test_range2():
    assert validate("3000.256.267.888") == False
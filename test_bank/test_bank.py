from bank import value

def test_hello():
    assert value("Hello") == "$0"

def test_h():
    assert value("Hey, how are you?") == "$20"

def test_other():
    assert value("Nice to see you") == "$100"
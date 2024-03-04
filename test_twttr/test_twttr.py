from twttr import shorten

def test_hello():
    assert shorten("Hello") == "Hll"

def test_rodrigo():
    assert shorten("Rodrigo") == "Rdrg"
from src.storage import load_polls

def test_storage():

    assert isinstance(load_polls(), list)

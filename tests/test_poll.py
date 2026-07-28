from src.validator import validate_title

def test_poll():

    assert validate_title("Favorite Language")

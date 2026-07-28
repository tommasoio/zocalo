from src.statistics import total_votes

def test_statistics():

    poll = {

        "votes": {

            "A": 3,
            "B": 2

        }

    }

    assert total_votes(poll) == 5

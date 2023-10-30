from app import process_query


def test_knows_about_dinosaurs():
    assert process_query("dinosaurs") == (
            "Dinosaurs ruled the Earth 200 million years ago"
            )


def test_knows_name():
    assert process_query("What is your name?") == "Ctrl+Alt+Defeat"


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"


def test_sum_two_numbers():
    assert process_query("What is 5 plus 2?") == "7"

    
def test_largest_number():
    assert process_query(
        "Which of the following numbers is the largest: 45, 70, 30?"
        ) == "70"

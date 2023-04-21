import project

def main():
    test_user_input()
    test_computer_input()
    test_index_to_text()
    test_draw_match_result()
    test_win_match_result()
    test_lose_match_result()

def test_user_input():
    assert project.user_input("rock") == project.ROCK
    assert project.user_input("Rock") == project.ROCK
    assert project.user_input("Rock") == project.ROCK
    
def test_computer_input():
    assert project.computer_input() in [0, 1, 2]

def test_index_to_text():
    assert project.index_to_text(0) == "Rock"
    assert project.index_to_text(1) == "Paper"
    assert project.index_to_text(2) == "Scissors"

def test_draw_match_result():
    assert project.match_result(project.ROCK, project.ROCK) == "It's a draw"
    assert project.match_result(project.PAPER, project.PAPER) == "It's a draw"
    assert project.match_result(project.SCISSORS, project.SCISSORS) == "It's a draw"

def test_win_match_result():
    assert project.match_result(project.ROCK, project.SCISSORS) == "You Won!, Rock Beats Scissors"
    assert project.match_result(project.PAPER, project.ROCK) == "You Won!, Paper Beats Rock"
    assert project.match_result(project.SCISSORS, project.PAPER) == "You Won!, Scissors Beats Paper"

def test_lose_match_result():
    assert project.match_result(project.SCISSORS, project.ROCK) == "You Lost, Rock Beats Scissors"
    assert project.match_result(project.ROCK, project.PAPER) == "You Lost, Paper Beats Rock"
    assert project.match_result(project.PAPER, project.SCISSORS) == "You Lost, Scissors Beats Paper"


if __name__ == "__main__":
    main()
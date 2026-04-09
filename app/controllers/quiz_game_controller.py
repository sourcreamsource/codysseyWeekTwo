from app.models.quiz import Quiz
from app.models.quiz_game import QuizGame
from app.views.console_view import ConsoleView


class QuizGameController:
    def __init__(self, game: QuizGame, view: ConsoleView) -> None:
        self.game = game
        self.view = view

    def run(self) -> None:
        pass

    def process_menu(self) -> None:
        pass

    def start_quiz(self) -> None:
        pass

    def create_quiz(self) -> Quiz:
        pass

    def add_quiz(self) -> None:
        pass

    def show_quiz_list(self) -> None:
        pass

    def show_score(self) -> None:
        pass

    def save_data(self) -> None:
        pass

    def load_data(self) -> None:
        pass

    def exit_game(self) -> None:
        pass

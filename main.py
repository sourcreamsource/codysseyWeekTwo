from app.controllers.quiz_game_controller import QuizGameController

def main() -> None:
    controller = QuizGameController()
    controller.run()

if __name__ == "__main__":
    main()

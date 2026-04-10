from app.models.quiz_game import QuizGame

def main() -> None:
    game = QuizGame()
    game.run()
    # game.read_json_data()

if __name__ == "__main__":
    main()

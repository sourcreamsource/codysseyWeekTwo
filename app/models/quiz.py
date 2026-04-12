from app.views.console_view import ConsoleView


class Quiz:
    def __init__(self, question: str, choices: list[str], answer: int, hint: str = "") -> None:
        self.console_view = ConsoleView()
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    def show_one_quiz(self) -> str:
        self.console_view.show_one_quiz(self.question, self.choices)

    def is_correct(self, user_answer: int) -> bool:
        return self.answer == user_answer

    def get_hint(self) -> str:
        return self.hint

    @classmethod
    def dict_to_quiz(cls, data: dict) -> "Quiz":
        return Quiz(data["question"], data["choices"], data["answer"], data.get("hint", ""))

    def quiz_to_dict(self) -> dict:
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint,
        }

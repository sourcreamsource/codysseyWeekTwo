class Quiz:
    def __init__(self, question: str, choices: list[str], answer: int) -> None:
        self.question = question
        self.choices = choices
        self.answer = answer

    def is_correct(self, user_answer: int) -> bool:
        pass

    def display(self) -> str:
        pass

    def to_dict(self) -> dict:
        pass

    def from_dict(cls, data: dict) -> "Quiz":
        pass

from app.views.console_view import ConsoleView

# 이 클래스는 단지 퀴즈 1개를 나타내는 클래스
class Quiz:
    def __init__(self, question: str, choices: list[str], answer: int) -> None:
        self.console_view = ConsoleView()
        self.question = question
        self.choices = choices
        self.answer = answer
        
    # 1개의 퀴즈를 보여준다.
    def show_one_quiz(self) -> str:
        self.console_view.show_one_quiz(self.question, self.choices)
    
    # 1개의 퀴즈 채점
    def is_correct(self, user_answer: int) -> bool:
        return self.answer == user_answer


    # ----------------------------------------
    # JSON 파일  →  딕셔너리  →  Quiz 객체
    @classmethod # 🔥 객체 없이 클래스에서 바로 호출할 수 있게 해주는 데코레이터입니다. 
                # 🔥 이 메서드는 Quiz 클래스 자체에 속하는 메서드로, 
                # 🔥 Quiz 객체를 생성하지 않고도 호출할 수 있습니다.
    def dict_to_quiz(cls, data: dict) -> "Quiz":
        return Quiz(data["question"], data["choices"], data["answer"])

    # ----------------------------------------
    # Quiz 객체  →  dictionary  →  JSON 파일 저장
    def quiz_to_dict(self) -> dict:   
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }



from app.validation.validation import Validation
from app.views.console_view import ConsoleView

class InputView:
    def __init__(self) -> None:
        self.validation = Validation()

    def input_quiz_answer(self) -> int | None:
        # 최대 5번까지 입력을 다시 받는다.
        attempt = 1

        while attempt <= 5:
            num = input("정답 입력: ")

            # 검증에 통과하면 숫자로 바꿔 반환한다.
            if self.validation.validate_quiz_answer_num(num):
                return int(num.strip())

            print(f'⚠️ 정답은 1부터 4 사이의 숫자로 입력하세요. \n\t시도 횟수: ({attempt}/5)\n')
            attempt += 1

        # 5번 모두 실패하면 종료 신호를 보낸다.
        self.view.show_error("정답 입력 5회 실패로 퀴즈가 종료되었습니다.")
        return None

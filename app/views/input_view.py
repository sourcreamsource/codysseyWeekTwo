from app.validation.validation import Validation
from app.views.console_view import ConsoleView

class InputView:
    def __init__(self) -> None:
        self.validation = Validation()
        self.view = ConsoleView()

    # ============================================================
    # 메뉴 번호 입력 시에만 쓰입니다.
    def input_menu_selection(self) -> str | None:
        # 최대 5번까지 입력을 다시 받는다.
        attempt = 1

        while attempt <= 5:
            num = input("🔢 번호 선택: ")
            print("\n")

            # 검증에 통과하면 공백을 제거한 값을 반환한다.
            if self.validation.validate_menu_selection_num(num):
                return num.strip()

            print(f"⚠️ 올바른 메뉴 번호를 입력하세요. \n\t시도 횟수: ({attempt}/5)\n")
            attempt += 1

        # 5번 모두 실패하면 종료 신호를 보낸다.
        self.view.show_error("메뉴 입력 5회 실패로 프로그램이 종료되었습니다.")
        return None

    # ============================================================
    # 유저의 답변을 입력받을 떄도 쓰이고,
    # 퀴즈 추가할 떄 답변을 입력할 때도 쓰입니다.
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


    # ============================================================
    # 퀴즈 문제를 입력
    def input_quiz_question(self) -> str | None:
        # 새 퀴즈의 문제를 최대 5번까지 입력받는다.
        attempt = 1
        question = ""

        while attempt <= 5:
            question = input("문제를 입력하세요: ").strip()
            if question:
                break

            self.view.show_error(f"⚠️ 문제는 비워둘 수 없습니다. ({attempt}/5)")
            attempt += 1

        if not question:
            self.view.show_error("문제 입력 5회 실패로 퀴즈 추가가 취소되었습니다.")
            return None

        return question

    # ============================================================
    # 퀴즈 문제의 선택지 4개를 입력 받는다. 하나라도 비어있으면 안된다.
    def input_quiz_choices(self) -> list[str] | None:
        # 선택지 4개를 입력받는다. 각 선택지도 최대 5번까지 입력 기회를 준다.
        choices = []

        for index in range(1, 5): # 1,2,3,4
            attempt = 1
            choice = ""

            while attempt <= 5:
                choice = input(f"선택지 {index}: ").strip()
                if choice:
                    break

                self.view.show_error(f"⚠️ 선택지는 비워둘 수 없습니다. ({attempt}/5)")
                attempt += 1

            if not choice:
                self.view.show_error("선택지 입력 5회 실패로 퀴즈 추가가 취소되었습니다.")
                return None

            choices.append(choice)

        return choices

    # ============================================================
    # 퀴즈 힌트를 입력받는다. 힌트는 비워둘 수 있다.
    def input_quiz_hint(self) -> str:
        return input("힌트를 입력하세요 (Enter로 생략 가능): ").strip()

    # ============================================================
    # 퀴즈 풀이 중 힌트를 볼지 입력받는다.
    def input_use_hint(self) -> bool:
        attempt = 1

        while attempt <= 5:
            answer = input("힌트를 보시겠습니까? (y/n): ").strip().lower()

            # 검증에 통과하면 y인지 아닌지를 bool로 반환한다.
            if self.validation.validate_use_hint(answer):
                return answer == "y"

            print(f"⚠️ y 또는 n만 입력하세요. \n\t시도 횟수: ({attempt}/5)\n")
            attempt += 1

        # 5번 모두 실패하면 힌트를 보지 않고 진행한다.
        self.view.show_error("⚠️ 힌트 선택 5회 실패로 힌트를 보지 않고 진행합니다.")
        return False

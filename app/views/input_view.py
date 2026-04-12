from __future__ import annotations

from app.validation.validation import Validation
from app.views.console_view import ConsoleView


class InputView:
    def __init__(self) -> None:
        self.validation = Validation()
        self.view = ConsoleView()

    def input_menu_selection(self) -> str | None:
        attempt = 1

        while attempt <= 5:
            num = input("🔢 번호 선택: ")
            print("\n")

            if self.validation.validate_menu_selection_num(num):
                return num.strip()

            print(f"⚠️ 올바른 메뉴 번호를 입력하세요. \n\t시도 횟수: ({attempt}/5)\n")
            attempt += 1

        self.view.show_error("⚠️ 메뉴 입력 5회 실패로 프로그램이 종료되었습니다.")
        return None

    def input_quiz_answer(self) -> int | None:
        attempt = 1

        while attempt <= 5:
            num = input("💬 정답 입력: ")

            if self.validation.validate_quiz_answer_num(num):
                return int(num.strip())

            print(f'⚠️ 정답은 1부터 4 사이의 숫자로 입력하세요. \n\t시도 횟수: ({attempt}/5)\n')
            attempt += 1

        self.view.show_error("⚠️ 정답 입력 5회 실패로 퀴즈가 종료되었습니다.\n\n")
        return None

    def input_quiz_question(self) -> str | None:
        attempt = 1
        question = ""

        while attempt <= 5:
            question = input("🤔 문제를 입력하세요: ").strip()
            if question:
                break

            self.view.show_error(f"⚠️ 문제는 비워둘 수 없습니다. ({attempt}/5)")
            attempt += 1

        if not question:
            self.view.show_error("⚠️ 문제 입력 5회 실패로 퀴즈 추가가 취소되었습니다.\n\n")
            return None

        return question

    def input_quiz_choices(self) -> list[str] | None:
        choices = []

        for index in range(1, 5):
            attempt = 1
            choice = ""

            while attempt <= 5:
                choice = input(f"선택지 {index}: ").strip()
                if choice:
                    break

                self.view.show_error(f"⚠️ 선택지는 비워둘 수 없습니다. ({attempt}/5)\n")
                attempt += 1

            if not choice:
                self.view.show_error("⚠️ 선택지 입력 5회 실패로 퀴즈 추가가 취소되었습니다.\n\n")
                return None

            choices.append(choice)

        return choices

    def input_quiz_hint(self) -> str:
        return input("힌트를 입력하세요 (Enter로 생략 가능): ").strip()

    def input_use_hint(self) -> bool:
        attempt = 1

        while attempt <= 5:
            answer = input("💬 💡 힌트를 보시겠습니까? (y/n): ").strip().lower()

            if self.validation.validate_use_hint(answer):
                return answer == "y"

            print(f"⚠️ y 또는 n만 입력하세요. \n\t시도 횟수: ({attempt}/5)\n")
            attempt += 1

        self.view.show_error("⚠️ 힌트 선택 5회 실패로 힌트를 보지 않고 진행합니다.\n\n")
        return False

    def input_remove_quiz_num(self, quiz_count: int) -> int | None:
        attempt = 1

        while attempt <= 5:
            num = input("💬 삭제할 퀴즈 번호를 입력하세요: ")

            if self.validation.validate_remove_quiz_num(num, quiz_count):
                return int(num.strip())

            print(f"⚠️ 존재하는 퀴즈 번호를 입력하세요. \n\t시도 횟수: ({attempt}/5)\n")
            attempt += 1

        self.view.show_error("⚠️ 삭제 번호 입력 5회 실패로 퀴즈 삭제가 취소되었습니다.\n\n")
        return None

    def input_quiz_count(self, quiz_count: int) -> int | None:
        attempt = 1

        while attempt <= 5:
            num = input(f"💬 몇 문제를 풀까요? (1 ~ {quiz_count} 내 선택): ")

            if self.validation.validate_quiz_count(num, quiz_count):
                return int(num.strip())

            print(f"⚠️ 1부터 {quiz_count} 사이의 숫자를 입력하세요. \n\t시도 횟수: ({attempt}/5)\n")
            attempt += 1

        self.view.show_error("⚠️ 문제 수 입력 5회 실패로 랜덤 퀴즈가 취소되었습니다.\n\n")
        return None

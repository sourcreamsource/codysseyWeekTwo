class Validation:
    def __init__(self):
        pass

    def validate_menu_selection_num(self, num: str) -> bool:
        # 공백을 제거한 뒤 1~8 사이의 숫자인지 확인한다.
        num = num.strip()

        if not num:
            return False

        if not num.isdigit():
            return False

        return 1 <= int(num) <= 8

    def validate_quiz_answer_num(self, num: str) -> bool:
        # 공백을 제거한 뒤 1~4 사이의 숫자인지 확인한다.
        num = num.strip()

        if not num:
            return False

        if not num.isdigit():
            return False

        return 1 <= int(num) <= 4

    def validate_use_hint(self, answer: str) -> bool:
        # 힌트 사용 여부는 y 또는 n만 허용한다.
        answer = answer.strip().lower()
        return answer == "y" or answer == "n"


    def validate_remove_quiz_num(self, num: str, quiz_count: int) -> bool:
        # 삭제할 퀴즈 번호는 숫자이면서 실제 퀴즈 목록 범위 안에 있어야 한다.
        num = num.strip()

        if not num:
            return False

        if not num.isdigit():
            return False

        selected_num = int(num)
        return 1 <= selected_num <= quiz_count

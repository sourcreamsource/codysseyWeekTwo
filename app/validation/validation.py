class Validation:
    def __init__(self):
        pass

    def validate_menu_selection_num(self, num: str) -> bool:
        # 공백을 제거한 뒤 1~7 사이의 숫자인지 확인한다.
        num = num.strip()

        if not num:
            return False

        if not num.isdigit():
            return False

        return 1 <= int(num) <= 7

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

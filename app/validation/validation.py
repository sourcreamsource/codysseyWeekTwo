class Validation:
    def __init__(self):
        pass

    def validate_quiz_answer_num(self, num: str) -> bool:
        # 공백을 제거한 뒤 1~4 사이의 숫자인지 확인한다.
        num = num.strip()

        if not num:
            return False

        if not num.isdigit():
            return False

        return 1 <= int(num) <= 4

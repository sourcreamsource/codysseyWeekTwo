class Validation:
    def __init__(self):
        pass

    def validate_menu_selection_num(self, num: str) -> bool:
        num = num.strip()

        if not num:
            return False

        if not num.isdigit():
            return False

        return 1 <= int(num) <= 8

    def validate_quiz_answer_num(self, num: str) -> bool:
        num = num.strip()

        if not num:
            return False

        if not num.isdigit():
            return False

        return 1 <= int(num) <= 4

    def validate_use_hint(self, answer: str) -> bool:
        answer = answer.strip().lower()
        return answer == "y" or answer == "n"

    def validate_remove_quiz_num(self, num: str, quiz_count: int) -> bool:
        num = num.strip()

        if not num:
            return False

        if not num.isdigit():
            return False

        selected_num = int(num)
        return 1 <= selected_num <= quiz_count

    def validate_quiz_count(self, num: str, quiz_count: int) -> bool:
        num = num.strip()

        if not num:
            return False

        if not num.isdigit():
            return False

        selected_num = int(num)
        return 1 <= selected_num <= quiz_count

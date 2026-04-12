from __future__ import annotations

from datetime import datetime
import json
import random

from app.data.tmp_data import create_default_json
from app.models.quiz import Quiz
from app.views.console_view import ConsoleView
from app.views.input_view import InputView


class QuizGame:
    def __init__(self):
        self.view = ConsoleView()
        self.input_view = InputView()
        self.quizzes: list[Quiz] = []
        self.best_score = 0
        self.game_history: list[dict] = []
        self.state_file = "state.json"

    def read_json_data(self) -> None:
        try:
            with open(self.state_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            quiz_dict_list = data["quizzes"]
            self.quizzes = [Quiz.dict_to_quiz(quiz_data) for quiz_data in quiz_dict_list]
            self.best_score = data["best_score"]
            self.game_history = data["game_history"]

        except FileNotFoundError:
            self.view.show_error("state.json 파일이 없어서 기본 데이터를 생성합니다.")
            is_created = create_default_json()
            if not is_created:
                self.view.show_error("기본 state.json 생성에 실패했습니다.")
                return
            self.read_json_data()

        except (json.JSONDecodeError, KeyError):
            self.view.show_error("state.json 데이터가 손상되어 기본 데이터로 복구합니다.")
            is_created = create_default_json()
            if not is_created:
                self.view.show_error("기본 state.json 생성에 실패했습니다.")
                return
            self.read_json_data()

    def quiz_start(self):
        if not self.quizzes:
            self.view.show_error("등록된 퀴즈가 없습니다.")
            return

        correct_num = 0
        hint_count = 0

        for quiz in self.quizzes:
            quiz.show_one_quiz()

            if self.input_view.input_use_hint():
                is_hint = self.view.show_hint(quiz.get_hint())
                if is_hint:
                    hint_count += 1

            user_answer = self.input_view.input_quiz_answer()
            if user_answer is None:
                return

            is_correct = quiz.is_correct(user_answer)
            self.view.show_is_correct(is_correct)

            if is_correct:
                correct_num += 1

        self.quiz_result(correct_num, hint_count)

    def quiz_start_random_by_count(self):
        if not self.quizzes:
            self.view.show_error("등록된 퀴즈가 없습니다.")
            return

        quiz_count = self.input_view.input_quiz_count(len(self.quizzes))
        if quiz_count is None:
            return

        selected_quizzes = random.sample(self.quizzes, quiz_count)
        correct_num = 0
        hint_count = 0

        for quiz in selected_quizzes:
            quiz.show_one_quiz()

            if self.input_view.input_use_hint():
                is_hint = self.view.show_hint(quiz.get_hint())
                if is_hint:
                    hint_count += 1

            user_answer = self.input_view.input_quiz_answer()
            if user_answer is None:
                return

            is_correct = quiz.is_correct(user_answer)
            self.view.show_is_correct(is_correct)

            if is_correct:
                correct_num += 1

        self.quiz_result(correct_num, hint_count, quiz_count)

    def quiz_result(self, correct_num: int, hint_count: int, total: int | None = None) -> None:
        if total is None:
            total = len(self.quizzes)

        score = int((correct_num / total) * 100)
        score -= hint_count * 1

        if score < 0:
            score = 0

        is_best_score = score > self.best_score
        if is_best_score:
            self.best_score = score

        game_result = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "questions": total,
            "correct": correct_num,
            "hint_count": hint_count,
            "score": score,
        }
        self.game_history.append(game_result)
        self.view.show_quiz_result(total, correct_num, score, is_best_score)

    def save_dict_data_to_json(self) -> None:
        quiz_dict_list = [quiz.quiz_to_dict() for quiz in self.quizzes]
        data = {
            "quizzes": quiz_dict_list,
            "best_score": self.best_score,
            "game_history": self.game_history,
        }

        with open(self.state_file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def check_quiz_score(self):
        if not self.game_history:
            self.view.show_error("아직 퀴즈를 푼 기록이 없습니다.")
            return

        latest_history = self.game_history[-1]
        self.view.show_score_history(
            self.best_score,
            latest_history["questions"],
            latest_history["correct"],
            latest_history.get("hint_count", 0),
        )

    def add_quiz(self):
        question = self.input_view.input_quiz_question()
        if question is None:
            return

        choices = self.input_view.input_quiz_choices()
        if choices is None:
            return

        answer = self.input_view.input_quiz_answer()
        if answer is None:
            return

        hint = self.input_view.input_quiz_hint()

        quiz_data = {
            "question": question,
            "choices": choices,
            "answer": answer,
            "hint": hint,
        }

        new_quiz = Quiz.dict_to_quiz(quiz_data)
        self.quizzes.append(new_quiz)
        self.save_dict_data_to_json()
        self.view.show_add_quiz_success()

    def remove_quiz(self):
        if not self.quizzes:
            self.view.show_error("❌ 삭제할 퀴즈가 없습니다.")
            return

        self.view.show_remove_quiz()
        self.view.show_quiz_list(self.quizzes)

        selected_num = self.input_view.input_remove_quiz_num(len(self.quizzes))
        if selected_num is None:
            return

        remove_index = selected_num - 1
        del self.quizzes[remove_index]
        self.save_dict_data_to_json()
        self.view.show_remove_quiz_success()

    def view_game_history(self):
        self.view.show_game_history(self.game_history)

from __future__ import annotations
from app.models.quiz_game import QuizGame


class QuizGameController:
    def __init__(self) -> None:
        # QuizGame은 퀴즈 목록, 점수, 저장/불러오기 같은 게임 상태와 기능을 담당한다.
        self.game = QuizGame()

        # Controller는 게임 객체가 가진 view/input_view를 사용해서 흐름만 제어한다.
        self.view = self.game.view
        self.input_view = self.game.input_view

    def run(self) -> None:
        try:
            # 프로그램이 시작되면 먼저 state.json 데이터를 메모리로 읽어온다.
            self.game.read_json_data()

            self.view.show_welcome()

            while True:
                self.view.show_menu()

                select = self.input_view.input_menu_selection()
                if select is None:
                    self.game.save_dict_data_to_json()
                    break

                if select == "1":
                    self.view.show_start_message(len(self.game.quizzes))
                    self.game.quiz_start()

                elif select == "2":
                    self.view.show_start_message(len(self.game.quizzes))
                    self.game.quiz_start_random_by_count()

                elif select == "3":
                    self.view.show_quiz_list(self.game.quizzes)

                elif select == "4":
                    self.view.add_new_quiz()
                    self.game.add_quiz()

                elif select == "5":
                    self.game.remove_quiz()

                elif select == "6":
                    self.game.check_quiz_score()

                elif select == "7":
                    self.game.view_game_history()

                elif select == "8":
                    self.game.save_dict_data_to_json()
                    break

                else:
                    print("⚠️ 올바른 메뉴 번호를 입력하세요.")

        except (KeyboardInterrupt, EOFError):
            self.view.show_error("🔄 입력이 중단되어 현재 상태를 저장하고 종료합니다.")
            self.game.save_dict_data_to_json()

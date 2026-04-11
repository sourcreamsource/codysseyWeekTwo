from datetime import datetime
import json
from app.data.tmp_data import create_default_json
from app.models.quiz import Quiz
from app.views.console_view import ConsoleView
from app.views.input_view import InputView

# 퀴즈 전체를 컨트롤하는 존재
class QuizGame:
    def __init__(self):
        # 화면 출력 전용 객체
        self.view = ConsoleView()

        # 입력 처리 전용 객체
        self.input_view = InputView()

        # 🟩 메모리에 올라온 Quiz 객체들을 저장하는 리스트
        # 🔥 ex. 붕어빵을 열심히 찍어낸다. 여기서 객체의 진정한 역할을 알게됨.
        # list[Quiz] = Quiz 객체들을 담는 리스트
        self.quizzes: list[Quiz] = []

        # 최고 점수 저장
        self.best_score = 0

        # 플레이 기록 저장
        self.game_history: list[dict] = []

        # 저장할 파일 이름
        self.state_file = "state.json"

    # =======================================================
    # json 파일 읽어서 Quiz 객체로 만들기
    # JSON 파일을 읽으면 자동으로 dict가 됩니다
    def read_json_data(self) -> None:
        try:
            # 1. state.json 파일을 읽는다.
            with open(self.state_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                # print(data) # 확인용

            # 2. quizzes 키에 들어있는 dict 목록을 꺼낸다.
            quiz_dict_list = data["quizzes"]

            # 3. dict 하나를 Quiz 객체 하나로 바꿔서 메모리에 올린다.
            self.quizzes = [Quiz.dict_to_quiz(quiz_data) for quiz_data in quiz_dict_list]

            # 4. 점수와 기록도 같이 메모리에 올린다.
            self.best_score = data["best_score"]
            self.game_history = data["game_history"]

        except FileNotFoundError:
            # 파일이 없으면 기본 state.json 파일을 만든 뒤 다시 읽는다.
            self.view.show_error("state.json 파일이 없어서 기본 데이터를 생성합니다.")
            is_created = create_default_json()
            if not is_created:
                self.view.show_error("기본 state.json 생성에 실패했습니다.")
                return
            self.read_json_data()

        except (json.JSONDecodeError, KeyError):
            # 파일이 손상되었으면 기본 state.json 파일을 다시 만든 뒤 읽는다.
            self.view.show_error("state.json 데이터가 손상되어 기본 데이터로 복구합니다.")
            is_created = create_default_json()
            if not is_created:
                self.view.show_error("기본 state.json 생성에 실패했습니다.")
                return
            self.read_json_data()


    # =======================================================
    # QuizGame이 가지고 있는 Quiz 객체들을 순서대로 보여주고 채점한다.
    def quiz_start(self):
        # 퀴즈가 하나도 없으면 더 이상 진행하지 않는다.
        if not self.quizzes: # 이미 elf.quizzes가 객체입니다.
            self.view.show_error("등록된 퀴즈가 없습니다.")
            return

        # 맞힌 문제 수를 저장한다.
        correct_num = 0

        # 힌트를 사용한 횟수를 저장한다.
        hint_count = 0

        # self.quizzes 안에 있는 Quiz 객체들을 하나씩 꺼내서 문제를 푼다.
        for quiz in self.quizzes:
            # 꺼낸 Quiz 객체의 문제와 선택지를 화면에 보여준다.
            quiz.show_one_quiz()

            # 사용자가 원하면 힌트를 보여준다. (이 위치가 적절한 것 같다.)
            if self.input_view.input_use_hint():
                self.view.show_hint(quiz.get_hint())
                hint_count += 1

            # 입력 처리 클래스에서 정답 입력을 받고, 최대 5번까지 재시도한다.
            user_answer = self.input_view.input_quiz_answer()
            if user_answer is None:
                return

            # Quiz 객체의 is_correct()를 사용해서 정답 여부를 확인한다.
            is_correct = quiz.is_correct(user_answer)

            # 맞았는지에 대한 내용을 출력한다.
            self.view.show_is_correct(is_correct)

            # 정답이면 맞힌 개수를 1 증가시킨다.
            if is_correct:
                correct_num += 1

        # 최종 결과를 계산하고 화면에 보여준다.
        self.quiz_result(correct_num, hint_count)


    # =======================================================
    # 퀴즈 결과를 계산하고 화면에 보여준다.
    def quiz_result(self, correct_num: int, hint_count: int) -> None:
        # 전체 문제 수를 구한다.
        total = len(self.quizzes)
        
        # 100점 만점 기준 점수를 계산한다.
        score = int((correct_num / total) * 100)

        # -------------------------------------
        # 힌트를 사용하면 힌트 1회당 1점을 차감한다.
        score -= hint_count * 1

        # 점수가 음수가 되지 않도록 막는다.
        if score < 0:
            score = 0
        # -------------------------------------

        # 현재 점수가 최고 점수보다 높으면 최고 점수를 갱신한다.
        is_best_score = score > self.best_score
        if is_best_score:
            self.best_score = score

        # josn에 진행한 game history 부분을 기록하는 것!
        game_result = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "questions": total,
            "correct": correct_num,
            "hint_count": hint_count,
            "score": score,
        }

        # 만든 게임 기록을 전체 기록 리스트에 추가한다.
        self.game_history.append(game_result)

        # 최종 결과를 화면에 보여준다.
        self.view.show_quiz_result(total, correct_num, score, is_best_score)


    # =======================================================
    # Quiz 객체를 json 파일로 저장하기
    # 🔥 이부분이 어렵다고 생각함
    def save_dict_data_to_json(self) -> None:
        # 1. 메모리에 있는 Quiz 객체들을 dict 형태로 바꾼다.
        quiz_dict_list = [quiz.quiz_to_dict() for quiz in self.quizzes]

        # 2. JSON 파일에 저장할 전체 데이터를 하나의 dict로 만든다.
        data = {
            "quizzes": quiz_dict_list, # 전체 퀴즈 dict list
            "best_score": self.best_score,
            "game_history": self.game_history,
        }

        # 3. 위에서 만든 dict를 state.json 파일로 저장한다. (dump)
        # write
        with open(self.state_file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)



    # =======================================================
    # 점수 확인하기
    def check_quiz_score(self):
        # 아직 퀴즈를 푼 기록이 없으면 안내하고 종료한다.
        if not self.game_history:
            self.view.show_error("아직 퀴즈를 푼 기록이 없습니다.")
            return

        # 가장 최근 게임 기록을 꺼낸다.
        latest_history = self.game_history[-1]

        # 최고 점수와 최근 게임의 문제 수/정답 수를 화면에 보여준다.
        self.view.show_score_history(
            self.best_score,
            latest_history["questions"],
            latest_history["correct"],
        )


    # =======================================================
    # 퀴즈 추가하기
    def add_quiz(self):
        # InputView에서 새 퀴즈 문제를 입력받는다.
        question = self.input_view.input_quiz_question()
        if question is None:
            return

        # InputView에서 선택지 4개를 입력받는다.
        choices = self.input_view.input_quiz_choices()
        if choices is None:
            return

        # InputView에서 정답 번호를 입력받는다.
        answer = self.input_view.input_quiz_answer()
        if answer is None:
            return

        # InputView에서 힌트를 입력받는다. 힌트는 비워둘 수 있다.
        hint = self.input_view.input_quiz_hint()

        quiz_data = {
            "question": question,
            "choices": choices,
            "answer": answer,
            "hint": hint,
        }

        # dict 데이터를 Quiz 객체로 바꾼다.
        new_quiz = Quiz.dict_to_quiz(quiz_data)

        # 메모리에 올라온 퀴즈 목록에 새 Quiz 객체를 추가한다.
        self.quizzes.append(new_quiz)

        # 추가한 퀴즈가 종료 전에 사라지지 않도록 바로 저장한다.
        self.save_dict_data_to_json()

        # 퀴즈 추가가 끝났음을 사용자에게 알려준다.
        self.view.show_add_quiz_success()


    # =======================================================
    # 퀴즈 삭제하기
    def remove_quiz(self):
        pass


    # =======================================================
    def run(self) -> None:
        # 프로그램이 시작되면 먼저 state.json 데이터를 메모리로 읽어온다.
        # 🔥 근데 매번 메뉴가 끝날 때마다 리팩토링? 되어야 하는 것 아닌가? 그렇기 때문에 while문 안에서 첫 단계에서 돌아야 하는 것 아닌가 싶습니다.
        self.read_json_data()

        self.view.show_welcome()

        while True:
            # 메뉴 보여주기
            self.view.show_menu() 

            # 사용자 입력 받기
            select = self.input_view.input_menu_selection()
            # 사용자 입력 문제가 반복되면 저장하고 종료!
            if select is None:
                self.save_dict_data_to_json()
                break


            if select == "1":   
                # 1. 퀴즈 풀기
                # 현재 메모리에 올라온 실제 퀴즈 개수를 보여준다.
                self.view.show_start_message(len(self.quizzes))
                self.quiz_start()

            elif select == "2": 
                # 2. 퀴즈 추가
                # 📌 새로운 퀴즈를 추가합니다.
                self.view.add_new_quiz()
                self.add_quiz()

            elif select == "3": 
                # 3. 퀴즈 목록
                # state.json 에서 읽어온 실제 Quiz 객체 목록을 보여준다.
                self.view.show_quiz_list(self.quizzes)

            elif select == "4": 
                # 4. 점수 확인
                self.check_quiz_score()

            elif select == "5": 
                # 5. 종료
                # 프로그램이 끝나기 전에 현재 상태를 state.json에 저장한다.
                self.save_dict_data_to_json()
                break
                # return?
                
            else:
                print("⚠️ 올바른 메뉴 번호를 입력하세요.")



# def start_quiz(self) -> None:
#     pass

# def create_quiz(self) -> Quiz:
#     pass

# def add_quiz(self) -> None:
#     pass

# def show_quiz_list(self) -> None:
#     pass

# def show_score(self) -> None:
#     pass



# def exit_game(self) -> None:
#     pass

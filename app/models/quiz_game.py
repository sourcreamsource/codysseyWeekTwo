import json
from app.models.quiz import Quiz
from app.views.console_view import ConsoleView

# 퀴즈 전체를 컨트롤하는 존재
class QuizGame:
    def __init__(self):
        # 화면 출력 전용 객체
        self.view = ConsoleView()

        # 메모리에 올라온 Quiz 객체들을 저장하는 리스트
        # 🔥 ex. 붕어빵을 열심히 찍어낸다. 여기서 객체의 진정한 역할을 알게됨.
        self.quizzes: list[Quiz] = []

        # 최고 점수 저장
        self.best_score = 0

        # 플레이 기록 저장
        self.game_history: list[dict] = []

        # 저장할 파일 이름
        self.state_file = "state.json"

    # ----------------------------
    # json 파일 읽어서 Quiz 객체로 만들기
    # JSON 파일을 읽으면 자동으로 dict가 됩니다
    def read_json_data(self) -> None:
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

    # ----------------------------
    # Quiz 객체를 json 파일로 저장하기
    # 🔥 이부분이 어렵다고 생각함
    def save_dict_data_to_json(self) -> None:
        # 1. 메모리에 있는 Quiz 객체들을 dict 형태로 바꾼다.
        quiz_dict_list = [quiz.quiz_to_dict() for quiz in self.quizzes]
                # ⚠️ 이미 quizzes Quiz()객체 이기 때문에 이 객체의 quiz_to_dict()를 실행한 것.
                # 그럼 이 list는 dict list가 되겠지.

        # 2. JSON 파일에 저장할 전체 데이터를 하나의 dict로 만든다.
        # 🔥 다시 이렇게 모은다.
        data = {
            "quizzes": quiz_dict_list, # 전체 퀴즈 dict list
            "best_score": self.best_score,
            "game_history": self.game_history,
        }

        # 3. 위에서 만든 dict를 state.json 파일로 저장한다. (dump)
        # write
        with open(self.state_file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)



    # ----------------------------
    # QuizGame이 가지고 있는 Quiz 객체들을 순서대로 채점한다.
    def quiz_start(self):
        pass



    # ----------------------------
    # 점수 확인하기
    def check_quiz_score(self):
        pass



    # ----------------------------
    # 퀴즈 목록 표시
    def view_quiz_list(self):
        pass

    # 퀴즈 추가하기
    def add_quiz(self):
        pass

    # 퀴즈 삭제하기
    def remove_quiz(self):
        pass

    
    # ----------------------------
    def input_and_validate(self) -> int:
        input_value = input("🔢 번호 선택: ")
        print('\n')
        # validation class function 추가하기
        return input_value # tpye 변환 해야합니다. util 폴더 만들어도 됨

    # ----------------------------
    def run(self) -> None:
        

        self.view.show_welcome()

        while True:
            # 메뉴 보여주기
            self.view.show_menu() 

            # 사용자 입력 받기
            select = self.input_and_validate()

            if select == "1":   
                # 1. 퀴즈 풀기
                fake_num_data = 999
                self.view.show_start_message(fake_num_data)
    

            elif select == "2": 
                # 2. 퀴즈 추가
                # 📌 새로운 퀴즈를 추가합니다.
                self.view.add_new_quiz()
                

            elif select == "3": 
                # 3. 퀴즈 목록
                fake_list_data = ['퀴즈1','퀴즈2','퀴즈3','퀴즈4','퀴즈5']
                self.view.show_quiz_list(fake_list_data)

            elif select == "4": 
                # 4. 점수 확인
                best_score = 80 # fake
                total = 5 # fake
                correct_num = 4 # fake
                self.view.show_score_history(best_score, total, correct_num)
                

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

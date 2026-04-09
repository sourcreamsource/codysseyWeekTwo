from app.models.quiz import Quiz
from app.views.console_view import ConsoleView

# 퀴즈 전체를 컨트롤하는 존재
class QuizGame:
    def __init__(self):
        # self.quiz = Quiz()
        self.view = ConsoleView()

    # ----------------------------
    # json 파일 읽어서 Quiz 객체로 만들기
    # JSON 파일을 읽으면 자동으로 dict가 됩니다
    def read_json_data(self) -> None:
        pass

    # Quiz 객체를 json 파일로 저장하기
    # 🔥 이부분이 어렵다고 생각함
    def save_dict_data_to_json(self) -> None:
        pass



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


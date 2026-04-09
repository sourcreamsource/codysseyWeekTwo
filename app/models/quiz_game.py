from app.models.quiz import Quiz
from app.views.console_view import ConsoleView

# 퀴즈 전체를 컨트롤하는 존재
class QuizGame:
    def __init__(self, quiz: Quiz, view: ConsoleView):
        self.quiz = quiz
        self.console_view = view

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
    # 메뉴 표시
    # 요구사항 때문에 여기에 만들고 controller에서 호출하는 형태로 만듬.
    def show_quiz_menu(self):
        self.console_view.show_menu() 


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
        value = input("🔢 번호 선택: ")
        # 
        # return select

    # ----------------------------
    def run(self) -> None:
        # 여기는 controller 니까 여기서는 다 합쳐도 된다고 생각하자!!!
        while True:

            # 메뉴 보여주기
            self.game.show_quiz_menu()

            # 사용자 입력 받기
            select = self.input_and_validate()

            if select == "1":    # 회원가입
                self.db_member_dict_list.append(self.sign.sign_up())
                print(f"(확인용) 현재 입력되어있는 회원 리스트 : {self.db_member_dict_list}")
                self.record_member_num()
                print(f"(확인용) 회원번호 기록여부 : {self.member_number_set}")

            elif select == "2":  # 로그인
                self.is_logged_in, self.logged_member_number = self.sign.sign_in(self.db_member_dict_list, self.is_logged_in, self.logged_member_number)
                self.posts = Posts(self.is_logged_in, self.logged_member_number)

            elif select == "3":  # 개인정보 조회
                self.sign.list_person_info(self.db_member_dict_list, self.is_logged_in, self.logged_member_number)

            elif select == "4":  # 개인정보 수정
                self.db_member_dict_list = self.sign.modify_person_info(self.db_member_dict_list, self.is_logged_in, self.logged_member_number)
                print(f"(확인용) 현재 수정 이후 회원 리스트 : {self.db_member_dict_list}")

            elif select == "5":  # 회원 탈퇴
                self.db_member_dict_list = self.sign.quit_member(self.db_member_dict_list, self.is_logged_in, self.logged_member_number)
                print(f"(확인용) 현재 탈퇴 이후 회원 리스트 : {self.db_member_dict_list}")
            
            elif select == "0":
                return print("👋 bye, bye..  종료합니다.")
            else:
                print("올바른 번호를 입력하세요.")




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


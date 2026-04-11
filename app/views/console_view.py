class ConsoleView:
    def __init__(self):
        pass

    # -----------------------------------------------------------
    def show_welcome(self):
        print('안녕하세요. 지금부터 퀴즈 게임을 시작하겠습니다.')

    # -----------------------------------------------------------
    def show_menu(self):
        print('========================================')
        print('        🎯 나만의 퀴즈 게임 🎯  ')
        print('========================================')
        print('1. 퀴즈 풀기')
        print('2. 퀴즈 풀기 (문제 수 지정, 랜덤 출제)')
        print('3. 퀴즈 목록 보기')
        print('4. 퀴즈 추가하기')
        print('5. 퀴즈 삭제하기')
        print('6. 점수 확인하기')
        print('7. 문제 기록 보기')
        print('8. 종료')
        print('========================================')

    # -----------------------------------------------------------
    def show_start_message(self, count_quiz):
        print(f'📝 퀴즈를 시작합니다! (총 {count_quiz}문제)')

    # -----------------------------------------------------------   
    def show_one_quiz(self, question: str, choices: list[str]):
        print('문제: ', question)
        for i, choice in enumerate(choices, 1):  
            if i > 4:
                break
            print(f"{i}. {choice}")

    # -----------------------------------------------------------   
    def show_is_correct(self, is_correct: bool):
        if is_correct:
            print("✅ 정답입니다!")
        else:
            print("❌ 오답입니다!")

    # -----------------------------------------------------------   
    def show_hint(self, hint: str):
        if not hint or hint == "":
            print("💡 등록된 힌트가 없습니다.")
            return
        print(f"💡 힌트: {hint}")

    # -----------------------------------------------------------   
    def show_quiz_result(self, total, correct_num, score, best_score):
        print(f"🏆 결과: {total}문제 중 {correct_num}문제 정답! ({score}점)")
        if best_score:
            print("🎉 새로운 최고 점수입니다!")

    # -----------------------------------------------------------   
    def show_saved_result(self):
        # 에러가 발생하지 않았을 경우 
        print('✅ 성공적으로 저장했습니다.')


    # -----------------------------------------------------------   
    def show_score_history(self, best_score, total, correct_num, hint_count):
        print(f'🏆 최고 점수: {best_score}점 ({total}문제 중 {correct_num}문제 정답)')
        print(f'💡 최근 힌트 사용 횟수: {hint_count}회')
        
    
    # -----------------------------------------------------------   
    def show_quiz_list(self, quizzes):
        print(f'📋 등록된 퀴즈 목록 ( {len(quizzes)}개 )')
        for i, quiz in enumerate(quizzes, start=1): # enumerate는 리스트의 인덱스와 값을 동시에 가져올 수 있게 해주는 함수입니다. start=1은 인덱스가 1부터 시작하도록 설정하는 옵션입니다.
            if quiz.hint:
                hint_status = "힌트 있음"
            else:
                hint_status = "힌트 없음"

            print(f'{i}. {quiz.question} / {hint_status}')

    # -----------------------------------------------------------   
    def add_new_quiz(self):
        print('📌 새로운 퀴즈를 추가합니다.')

    def show_add_quiz_success(self):
        print('✅ 퀴즈가 추가되었습니다!')


    # -----------------------------------------------------------   
    def show_remove_quiz(self):
        print('📌 퀴즈를 삭제합니다.')

    def show_remove_quiz_success(self):
        print('✅ 퀴즈가 삭제되었습니다!')


    # -----------------------------------------------------------   
    def show_error(self, message: str):
        # 에러가 발생했을 경우
        print(f'❌ 에러: {message}')

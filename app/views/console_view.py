class ConsoleView:
    def show_welcome(self) -> None:
        print('안녕하세요. 지금부터 퀴즈 게임을 시작하겠습니다.')

    def show_menu(self) -> None:
        print('========================================')
        print('        🎯 나만의 퀴즈 게임 🎯  ')
        print('========================================')
        print('1. 퀴즈 풀기')
        print('2. 퀴즈 추가하기')
        print('3. 퀴즈 목록 보기')
        print('4. 점수 확인하기')
        print('5. 종료')
        print('========================================')


    def show_message(self, message: str) -> None:
        print('')

    def show_quiz(self, quiz) -> None:
        # json에 정한 구조를 그대로 가져다가 쓰면 됩니다.
        print('문제: ', quiz.question)
        print('선택지: ', quiz.choices)


    def show_quiz_list(self, quizzes) -> None:
        # print(f'퀴즈 목록: ')
        pass
        

    def show_score(self, score: int, best_score: int) -> None:
        print(f'현재 점수: {score}')
        print(f'최고 점수: {best_score}')

    def show_saved_result(self) -> None:
        # 에러가 발생하지 않았을 경우 
        print('✅ 성공적으로 저장했습니다.')

    def show_error(self, message: str) -> None:
        # 에러가 발생했을 경우
        print(f'❌ 에러: {message}')

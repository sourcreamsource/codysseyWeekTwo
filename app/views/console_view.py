class ConsoleView:
    def __init__(self):
        pass

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

    # def show_message(self, message: str) -> None:
    #     print('')

    def show_one_quiz(self, question: str, choices: list[str]) -> None:
        print('문제: ', question)
        for i, choice in enumerate(choices, 1):  
            if i > 4:
                break
            print(f"{i}. {choice}")







    def show_quiz_list(self, quizzes) -> None:
        print(f'📋 등록된 퀴즈 목록 ( {len(quizzes)}개 )')
        for i, quiz in enumerate(quizzes, start=1): # enumerate는 리스트의 인덱스와 값을 동시에 가져올 수 있게 해주는 함수입니다. start=1은 인덱스가 1부터 시작하도록 설정하는 옵션입니다.
            print(f'{i}. {quiz.question}')

    def show_score(self, score: int, best_score: int) -> None:
        print(f'현재 점수: {score}')
        print(f'최고 점수: {best_score}')



    def show_saved_result(self) -> None:
        # 에러가 발생하지 않았을 경우 
        print('✅ 성공적으로 저장했습니다.')

    def show_error(self, message: str) -> None:
        # 에러가 발생했을 경우
        print(f'❌ 에러: {message}')

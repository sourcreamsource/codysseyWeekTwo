import json
import os

def create_default_json():
    # 1. 저장할 기본 데이터 구성
    default_data = {
        "quizzes": [
            {
                "question": "파이썬에서 리스트에 요소를 추가하는 함수는?",
                "choices": ["add()", "append()", "insert_all()", "push()"],
                "answer": 2,
                "hint": "리스트의 맨 뒤에 요소를 이어 붙인다는 뜻을 가진 단어입니다."
            },
            {
                "question": "다음 중 파이썬의 논리 자료형(Boolean)이 아닌 것은?",
                "choices": ["True", "False", "None", "bool"],
                "answer": 3,
                "hint": "None은 값이 없음을 나타내는 특수 상수입니다."
            },
            {
                "question": "반복문에서 현재 루프를 건너뛰고 다음 루프로 넘어가는 키워드는?",
                "choices": ["break", "pass", "continue", "skip"],
                "answer": 3,
                "hint": "'계속하다'라는 의미를 가진 영단어입니다."
            },
            {
                "question": "파이썬의 '딕셔너리' 자료형을 선언할 때 사용하는 기호는?",
                "choices": ["[]", "()", "{}", "<>"],
                "answer": 3,
                "hint": "중괄호를 사용합니다."
            },
            {
                "question": "파일을 열 때 사용하는 파이썬 내장 함수는?",
                "choices": ["file()", "read()", "open()", "load()"],
                "answer": 3,
                "hint": "무언가를 '열다'라는 의미의 단어입니다."
            }
        ],
        "best_score": 0,
        "game_history": []
    }

    # 2. 저장 경로 설정 (프로젝트 루트의 state.json)
    # data/ 폴더 안에 있으므로 '..', '..'을 사용하여 루트 디렉토리로 이동합니다.
    file_path = os.path.join(os.path.dirname(__file__), "..", "..", "state.json")

    # 3. 파일 쓰기 (UTF-8 인코딩 적용)
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            # json.dump() 함수는 파이썬 객체를 JSON 형식으로 변환하여 파일에 저장합니다.
            json.dump(default_data, f, ensure_ascii=False, indent=4)
        print("✅ state.json 파일이 루트 디렉토리에 생성되었습니다.")
    except Exception as e:
        print(f"❌ 파일 생성 중 오류 발생: {e}")

if __name__ == "__main__":
    create_default_json()

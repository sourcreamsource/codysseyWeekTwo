# 🟩 2주차: Git과 함께하는 Python 첫 발자국  

## 📜 프로젝트 개요  
- Python 콘솔 퀴즈 게임을 만드는 프로젝트  
- Python과 Git은 "내가 만든 프로그램이 왜 이렇게 동작하는지"를 설명하고, 그 과정을 기록하며 성장하기 위한 핵심 도구  
- `Quiz`, `QuizGame`, `ConsoleView`, `InputView`, `Validation`의 역할을 나누어 구현한다.  
- 모델, 입력/출력 뷰, 검증 클래스를 분리해 각 파일의 책임이 섞이지 않도록 구성한다.  
- `state.json`으로 퀴즈 목록, 최고 점수, 게임 기록을 저장한다.  
- 프로그램을 종료하고 다시 실행해도 저장된 퀴즈와 점수 기록을 유지한다.  


<br><br>

## 🤔 퀴즈 주제 선정 이유  
- 퀴즈 주제는 Python 기초 문법으로 정했다.  
- 이 프로젝트의 목표가 Python 기초와 클래스, 파일 입출력, Git 사용법을 익히는 것이기 때문에 프로젝트 주제와 가장 잘 맞는다.  
- 리스트, Boolean, 반복문, 딕셔너리, 파일 입출력처럼 초반 학습에서 자주 쓰는 개념을 문제로 구성했다.  

<br><br>

## 🖥️ 실행 환경 및 실행 방법  
- OS: macOS  
- Shell: zsh  
- Python: 3.11 이상  
    - uv 설치  
        - brew install uv  
    - 환경 셋팅  
        - uv sync  
    - 실행 방법  
        - uv run main.py  
- Git: 2.51.0  

<br><br>

## ✅ 기능 목록 (요구사항 체크리스트)  

- [x] `main.py` 실행 진입점 구성  
- [x] MVC 역할 분리 기반 구조 구성  

<br>

- [x] `Quiz` 클래스 구현  
- [x] `QuizGame` 클래스 구현  
- [x] `ConsoleView` 클래스 구현  
- [x] `InputView` 클래스 구현  
- [x] `Validation` 클래스 구현  

<br>

- [x] `Quiz` 객체 1개가 문제 1개를 표현하도록 구성  
- [x] `QuizGame`이 여러 `Quiz` 객체를 리스트로 관리하도록 구성  

<br>

- [x] `state.json` 기반 데이터 저장 구조 구성  
- [x] `state.json`에서 JSON 데이터를 읽어 `Quiz` 객체로 변환  
- [x] `Quiz` 객체를 다시 dict 형태로 변환해 `state.json`에 저장  
- [x] `state.json` 파일이 없을 때 기본 데이터 생성  
- [x] `state.json` 파일이 손상되었을 때 기본 데이터로 복구  
- [x] 기본 퀴즈 데이터 구성  
- [x] 퀴즈 문제, 선택지 4개, 정답 번호 저장  
- [x] 힌트 데이터 저장  

<br>

- [x] 프로그램 시작 시 저장 데이터 자동 불러오기  
- [x] 프로그램 종료 시 현재 데이터 자동 저장  

<br>

- [x] 메인 메뉴 출력  
- [x] 메뉴 입력 검증  
- [x] 잘못된 메뉴 입력 시 최대 5회 재입력 처리  

<br>

- [x] `1. 퀴즈 풀기` 기능 구현  
- [x] 전체 퀴즈 순차 출제  
- [x] 문제와 선택지 출력  
- [x] 정답 입력 처리  
- [x] 정답 번호 1~4 입력 검증  
- [x] 잘못된 정답 입력 시 최대 5회 재입력 처리  
- [x] 정답/오답 결과 출력  
- [x] 최종 점수 계산  
- [x] 최고 점수 갱신  
- [x] `2. 랜덤 퀴즈 풀기 (문제 수 지정)` 기능 구현  
- [x] 풀 문제 수 입력 처리  
- [x] 풀 문제 수 범위 검증  
- [x] 입력한 문제 수만큼 랜덤 출제  
- [x] `random.sample()`을 이용한 랜덤 퀴즈 선택  
- [x] `3. 퀴즈 목록 보기` 기능 구현  
- [x] 등록된 퀴즈 목록 출력  
- [x] 퀴즈별 힌트 있음/없음 표시  
- [x] `4. 퀴즈 추가하기` 기능 구현  
- [x] 새 퀴즈 문제 입력  
- [x] 선택지 4개 입력  
- [x] 정답 번호 입력  
- [x] 힌트 입력  
- [x] 문제/선택지 빈 입력 검증  
- [x] 퀴즈 추가 후 `state.json`에 즉시 저장  
- [x] 퀴즈 추가 성공 메시지 출력  
- [x] `5. 퀴즈 삭제하기` 기능 구현  
- [x] 삭제 전 퀴즈 목록 출력  
- [x] 삭제할 퀴즈 번호 입력  
- [x] 삭제 번호 숫자 및 범위 검증  
- [x] 퀴즈 삭제 후 `state.json`에 즉시 저장  
- [x] 퀴즈 삭제 성공 메시지 출력  
- [x] `6. 점수 확인하기` 기능 구현  
- [x] 최고 점수 출력  
- [x] 최근 게임의 문제 수와 정답 수 출력  
- [x] 최근 힌트 사용 횟수 출력  
- [x] 아직 푼 기록이 없을 때 안내 메시지 출력  
- [x] `7. 기록 보기` 기능 구현  
- [x] 게임 기록 목록 출력  
- [x] 기록별 날짜, 문제 수, 정답 수, 힌트 사용 횟수, 점수 출력  
- [x] `8. 종료` 기능 구현  
- [x] 종료 전 `state.json` 저장  
- [x] 힌트 보기 기능 구현  
- [x] 힌트 사용 여부 입력 검증  
- [x] 힌트 사용 시 점수 차감  
- [x] 힌트 사용 횟수를 게임 기록에 저장  
- [x] 게임 기록을 `state.json`에 저장  

<br>

- [x] 입력 중단 `KeyboardInterrupt`, `EOFError` 안전 종료 처리  





<br><br>

## 📁 파일 구조  
- `models`: 퀴즈 객체와 게임 전체 흐름 담당  
- `views`: 콘솔 출력과 사용자 입력 담당  
- `validation`: 메뉴 번호, 정답 번호, 삭제 번호 등 입력 검증 담당  
- `data`: 기본 `state.json` 생성용 더미 데이터 담당  
- `main.py`: 프로그램 실행 진입점  
- `state.json`: 퀴즈 목록, 최고 점수, 게임 기록 저장 파일  

```markdown
    📦 codysseyWeekTwo  
    ┣ 📂 app  
    ┃ ┣ 📂 data  
    ┃ ┃ ┗ 📄 tmp_data.py  
    ┃ ┣ 📂 models  
    ┃ ┃ ┣ 📄 quiz.py  
    ┃ ┃ ┗ 📄 quiz_game.py  
    ┃ ┣ 📂 validation  
    ┃ ┃ ┗ 📄 validation.py  
    ┃ ┗ 📂 views  
    ┃   ┣ 📄 console_view.py  
    ┃   ┗ 📄 input_view.py  
    ┣ 📂 docs  
    ┃ ┗ 📂 01_requirements  
    ┣ 📄 main.py  
    ┣ 📄 state.json  
    ┣ 📄 README.md  
    ┣ 📄 .gitignore  
    ┣ 📄 pyproject.toml  
    ┣ 📄 uv.lock  
    ┗ 📄 poetry.lock  
```





<br><br>

## 🗂️ 데이터 파일 설명  
> `state.json` 경로/역할/스키마  
- 경로: 프로젝트 루트 `state.json`  
- 역할: `퀴즈 목록`, `최고 점수`, `게임 기록`을 저장  

```json
{  
  "quizzes": [  
    {  
      "question": "문제",  
      "choices": ["선택지1", "선택지2", "선택지3", "선택지4"],  
      "answer": 1,  
      "hint": "힌트 내용"  
    }  
  ],  
  "best_score": 80,  
  "game_history": [  
    {  
      "date": "2026-04-12 03:03:28",  
      "questions": 5,  
      "correct": 4,  
      "hint_count": 1,  
      "score": 75  
    }  
  ]  
}  
```

- `quizzes`: 저장된 퀴즈 목록  
- `question`: 문제 내용  
- `choices`: 선택지 4개  
- `answer`: 정답 번호, 1~4 중 하나  
- `hint`: 힌트 내용, 없으면 빈 문자열  
- `best_score`: 지금까지 기록한 최고 점수  
- `game_history`: 퀴즈를 푼 기록 목록  
- `hint_count`: 해당 게임에서 힌트를 사용한 횟수  

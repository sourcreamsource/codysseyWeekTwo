# 🟩 2주차: Git과 함께하는 Python 첫 발자국  

## 📜 프로젝트 개요  
- Python 콘솔 퀴즈 게임을 만드는 프로젝트  
- Python과 Git은 "내가 만든 프로그램이 왜 이렇게 동작하는지"를 설명하고, 그 과정을 기록하며 성장하기 위함.  
- `Quiz`, `QuizGame`, `ConsoleView`, `InputView`, `Validation`의 역할을 나누어 구현한다.  
- 모델, 입력/출력 뷰, 검증 클래스를 분리해 각 파일의 책임이 섞이지 않도록 구성한다.  
- `state.json`으로 퀴즈 목록, 최고 점수, 게임 기록을 저장한다.  
- 프로그램을 종료하고 다시 실행해도 저장된 퀴즈와 점수 기록을 유지한다.  




<br><br>

## 🤔 퀴즈 주제 선정 이유  
(출제자의 의도가 무엇일까???)  
- 이 프로젝트의 목표가 `Python 기초 문법과 클래스`, `파일 입출력`, `Git 사용법`을 익히는 것에 목적이 있는 것으로 파악되며,  
- 방대한 양의 데이터를 다루게 될텐데 거기서 클래스와 객체를 이용하여 어떻게 관리할 것인지에 대해서 알 수 있다.  




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

## 📁 파일 구조  
- `models`: 퀴즈 객체와 게임 전체 흐름 담당  
- `controllers`: 프로그램 실행 흐름과 메뉴 분기 담당  
- `views`: 콘솔 출력과 사용자 입력 담당  
- `validation`: 메뉴 번호, 정답 번호, 삭제 번호 등 입력 검증 담당  
- `data`: 기본 `state.json` 생성용 더미 데이터 담당  
- `main.py`: 프로그램 실행 진입점  
- `state.json`: 퀴즈 목록, 최고 점수, 게임 기록 저장 파일  

```markdown
    📦 codysseyWeekTwo  
    ┣ 📂 app  
    ┃ ┣ 📂 controllers  
    ┃ ┃ ┗ 📄 quiz_game_controller.py  
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


<br>

### 🟡 JSON으로 저장하는 이유와 JSON 형식의 특징  
- JSON은 사람이 읽기 쉬운 텍스트 기반 데이터 형식이다.  
- Python의 `dict`, `list`, `str`, `int`, `bool` 같은 기본 자료형과 구조가 비슷해서 처음 배우는 단계에서 이해하기 쉽다.  
- 이 프로젝트의 퀴즈 데이터는 문제, 선택지, 정답, 힌트처럼 key-value 구조로 표현하기 좋다.  
- `json.load()`를 사용하면 `state.json` 파일 내용을 Python의 `dict`로 쉽게 불러올 수 있다.  
- `json.dump()`를 사용하면 Python의 `dict`를 다시 JSON 파일로 쉽게 저장할 수 있다.  
- 별도 데이터베이스 설치 없이 표준 라이브러리만으로 저장/불러오기를 구현할 수 있다.  
- 프로그램을 종료해도 `state.json` 파일이 남기 때문에 퀴즈 목록, 최고 점수, 게임 기록을 유지할 수 있다.  
- JSON은 텍스트 파일이므로 Git에서 변경 내용을 비교하기 쉽다.  


<br>

### 🟡 퀴즈 데이터가 1000개 이상으로 늘어난다면 생길 수 있는 한계  
- 현재 방식은 `state.json` 파일 전체를 한 번에 읽고 전체를 다시 저장한다.  
- 퀴즈가 1000개 이상으로 늘어나면 파일 크기가 커지고, 프로그램 시작 시 전체 로딩 시간이 길어질 수 있다.  
- 퀴즈 1개만 추가하거나 삭제해도 전체 JSON 파일을 다시 저장해야 하므로 비효율적이다.  
- 여러 사용자가 동시에 파일을 수정하는 상황에서는 마지막에 저장한 내용이 이전 저장 내용을 덮어쓸 위험이 있다.  
- JSON 파일은 특정 조건의 퀴즈만 빠르게 검색하거나 정렬하는 기능이 약하다.  
- 예를 들어 “힌트가 있는 문제만 찾기”, “최근 추가한 문제만 찾기” 같은 기능은 매번 전체 리스트를 순회해야 한다.  
- 파일이 커질수록 손상되었을 때 복구 부담도 커진다.  
- 데이터가 더 많아지거나 검색/수정이 복잡해진다면 SQLite 같은 데이터베이스를 사용하는 편이 더 적절하다.  
- 현재 프로젝트는 학습용 콘솔 프로그램이고 데이터 규모가 작기 때문에 JSON 방식이 충분히 적합하다.  


<br><br>

## 🎮 메뉴 구성  
- `1. 퀴즈 풀기`: 저장된 전체 퀴즈를 순서대로 푼다.  
- `2. 랜덤 퀴즈 풀기`: 풀 문제 수를 입력하고 해당 개수만큼 랜덤 출제한다.  
- `3. 퀴즈 목록 보기`: 저장된 퀴즈 목록과 힌트 여부를 확인한다.  
- `4. 퀴즈 추가하기`: 문제, 선택지 4개, 정답 번호, 힌트를 입력해 새 퀴즈를 추가한다.  
- `5. 퀴즈 삭제하기`: 목록에서 번호를 선택해 퀴즈를 삭제한다.  
- `6. 점수 확인하기`: 최고 점수와 최근 기록 정보를 확인한다.  
- `7. 기록 보기`: 날짜별 게임 기록을 확인한다.  
- `8. 종료`: 현재 상태를 저장하고 프로그램을 종료한다.  




<br><br>

## 🧩 클래스  

### 🟡 클래스는 왜 사용했는가?  
- 역할을 묶는 것!  

- 특정 데이터와 특정 기능을 한 곳에 묶어놓고, 객체로 생성을 하게 되면 특정 데이터 메모리에 올라가 있는 상태에서 원하는 특정 기능을 원하는대로 동작하게 할 수 있기 때문이다.  
  - 클래스를 사용하면 `quiz.is_correct(user_answer)`처럼 객체가 자기 데이터를 가지고 직접 동작할 수 있다.  
  - 즉 함수 중심 구현은 “동작”을 나누는 데 유리하고, 클래스 중심 구현은 “상태와 동작을 함께 묶는 것”에 유리하다.  
  - 즉 함수 중심 구현은 “동작”을 나누는 데 유리하고, 클래스 중심 구현은 “상태와 동작을 함께 묶는 것”에 유리하다.  
  

<br>

### 🟡 퀴즈게임 역할 정리  
- `Quiz`: 퀴즈 1문제를 표현한다. 문제, 선택지, 정답, 힌트를 속성으로 가진다.  
- `QuizGame`: 게임 전체를 관리한다. 퀴즈 목록, 최고 점수, 게임 기록, 저장/불러오기, 메뉴 흐름을 담당한다.  
- `ConsoleView`: 콘솔 출력 담당이다. 메뉴, 문제, 결과, 점수, 기록, 에러 메시지를 출력한다.  
- `InputView`: 콘솔 입력 담당이다. 메뉴 번호, 정답 번호, 퀴즈 추가 입력, 삭제 번호, 힌트 사용 여부를 입력받는다.  
- `Validation`: 입력 검증 담당이다. 메뉴 범위, 정답 범위, 삭제 번호 범위, 힌트 사용 여부 등을 검사한다.  


<br>




<br><br>

## 🛡️ 입력 검증 및 예외 처리  
- 메뉴 번호는 `1~8` 사이의 숫자만 허용한다.  
- 정답 번호는 `1~4` 사이의 숫자만 허용한다.  
- 랜덤 퀴즈의 문제 수는 `1~현재 퀴즈 개수` 사이의 숫자만 허용한다.  
- 퀴즈 삭제 번호는 실제 존재하는 퀴즈 번호만 허용한다.  
- 문제와 선택지는 빈 문자열을 허용하지 않는다.  
- 잘못된 입력은 최대 5회까지 다시 입력받는다.  
- `Ctrl+C`로 인한 `KeyboardInterrupt` 발생 시 현재 상태를 저장하고 종료한다.  
- 입력 스트림 종료로 인한 `EOFError` 발생 시 현재 상태를 저장하고 종료한다.  
- `state.json` 파일이 없거나 손상된 경우 `app/data/tmp_data.py`의 기본 데이터로 복구한다.  


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

## 🌿 Git 작업 방식  
요구사항에 맞춰 기능 단위 브랜치를 만들고, 기능 완료 후 `main`에 `--no-ff` 방식으로 병합한다.  

```bash
git checkout -b feature/example-feature  
git add .  
git commit -m "Feat: 기능 설명"  
git switch main  
git merge --no-ff feature/example-feature -m "merge: feature/example-feature"  
```

- 사용한 브랜치 이름 예시:  

  - `feature/recover-state-with-default-data`  
  - `feature/play-multiple-quizzes`  
  - ...  

- 커밋 메시지 예시:  
  ```text
  Feat: state.json 오류 시 기본 데이터 복구 기능 추가  
  Feat: 여러 퀴즈 순차 풀이 기능 추가  
  Feat: 퀴즈 게임 기록 저장 기능 추가  
  Feat: 퀴즈 삭제 기능 구현  
  ```


<br>

#### ⚫️ Git 로그 화면  
<img src="./public/screenshots/09_git_log.jpg" width="1080" alt="git log --oneline --graph 실행 결과">

<br>

#### ⚫️ Git clone  
<img src="./public/screenshots/10_git_clone.jpg" width="700" alt="git clone 실행 결과">

<br>

#### ⚫️ Git pull  
<img src="./public/screenshots/11_git_pull.jpg" width="700" alt="git pull 실행 결과">






<br><br>

## 🔧 요구사항이 바뀐다면 먼저 수정할 위치  
- 정답 채점 방식이 바뀐다면 [quiz.py](./app/models/quiz.py)의 `Quiz.is_correct()`를 먼저 확인한다.  
- 점수 계산 방식이 바뀐다면 [quiz_game.py](./app/models/quiz_game.py)의 `QuizGame.quiz_result()`를 먼저 수정한다.  
- 힌트 차감 점수가 바뀐다면 [quiz_game.py](./app/models/quiz_game.py)의 `QuizGame.quiz_result()`에서 `hint_count`를 사용해 점수를 차감하는 부분을 수정한다.  
- 선택지 개수가 4개에서 5개로 바뀐다면 [input_view.py](./app/views/input_view.py)의 `InputView.input_quiz_choices()`를 먼저 수정한다.  
- 선택지 개수가 바뀌면 [validation.py](./app/validation/validation.py)의 `Validation.validate_quiz_answer_num()`도 함께 수정해야 한다.  
- 선택지 출력 방식이 바뀐다면 [console_view.py](./app/views/console_view.py)의 `ConsoleView.show_one_quiz()`를 수정한다.  
- 메뉴 번호가 추가되거나 바뀐다면 [console_view.py](./app/views/console_view.py)의 `ConsoleView.show_menu()`와 [validation.py](./app/validation/validation.py)의 `Validation.validate_menu_selection_num()`을 수정한다.  
- 메뉴 동작 흐름이 바뀐다면 [quiz_game_controller.py](./app/controllers/quiz_game_controller.py)의 `QuizGameController.run()`을 수정한다.  
- 저장 데이터 구조가 바뀐다면 [quiz.py](./app/models/quiz.py)의 `quiz_to_dict()`, `dict_to_quiz()`와 [quiz_game.py](./app/models/quiz_game.py)의 저장/불러오기 메서드를 함께 확인한다.  





<br><br>

## 📸 스크린샷 기록  
요구사항에서는 실행 결과와 Git 기록을 스크린샷으로 남기는 것을 권장한다.  

#### 추천 저장 경로:  

```text
  public/screenshots/  
```

- 권장 스크린샷:  
  - 프로그램 시작 화면 (01_menu.jpg)  
  - 퀴즈 풀이 화면    (02_play.jpg)  
  - 랜덤 퀴즈 풀이 화면 (03_random_play.jpg)  
  - 퀴즈 추가 화면    (04_add_quiz.jpg)  
  - 퀴즈 목록 화면    (05_list_quiz.jpg)  
  - 퀴즈 삭제 화면    (06_remove_quiz.jpg)  
  - 점수 확인 화면    (07_score.jpg)  
  - 기록 보기 화면    (08_history.jpg)  
  - `git log --oneline --graph` 실행 결과  (09_git_log.jpg)  


<br><br>

### 🖼️ 실행 화면 스크린샷  

#### ⚫️ 1. 프로그램 시작 화면  
<img src="./public/screenshots/01_menu.jpg" width="550" alt="프로그램 시작 화면">

<br>

#### ⚫️ 2. 퀴즈 풀이 화면  
<img src="./public/screenshots/02_play.jpg" width="500" alt="퀴즈 풀이 화면">

<br>

#### ⚫️ 3. 랜덤 퀴즈 풀이 화면  
<img src="./public/screenshots/03_random_play.jpg" width="600" alt="랜덤 퀴즈 풀이 화면">

<br>

#### ⚫️ 4. 퀴즈 추가 화면  
<img src="./public/screenshots/04_add_quiz.jpg" width="500" alt="퀴즈 추가 화면">

<br>

#### ⚫️ 5. 퀴즈 목록 화면  
<img src="./public/screenshots/05_list_quiz.jpg" width="700" alt="퀴즈 목록 화면">

<br>

#### ⚫️ 6. 퀴즈 삭제 화면  
<img src="./public/screenshots/06_remove_quiz.jpg" width="700" alt="퀴즈 삭제 화면">

<br>

#### ⚫️ 7. 점수 확인 화면  
<img src="./public/screenshots/07_score.jpg" width="500" alt="점수 확인 화면">

<br>

#### ⚫️ 8. 기록 보기 화면  
<img src="./public/screenshots/08_history.jpg" width="700" alt="기록 보기 화면">

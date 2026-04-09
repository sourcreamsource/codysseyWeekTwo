# 🟩 2주차: Git과 함께하는 Python 첫 발자국  

## 📜 프로젝트 개요  
- Python 콘솔 퀴즈 게임을 만드는 프로젝트  
- Python과 Git은 "내가 만든 프로그램이 왜 이렇게 동작하는지"를 설명하고, 그 과정을 기록하며 성장하기 위한 핵심 도구  
- 구조는 문서 중심이 아니라 MVC 패턴 기준으로 잡는다.  
- `Quiz`, `QuizGame` 역할을 분리하고, `state.json`으로 퀴즈와 최고 점수를 저장한다.  


<br><br>

## 🤔 퀴즈 주제 선정 이유  


<br><br>

## 🖥️ 실행 환경 및 실행 방법  
- OS: macOS  
- Shell: zsh  
- Python: 3.11  
    - uv 설치  
        - brew install uv  
    - 환경 셋팅  
        - uv sync  
    - 실행 방법  
        - uv run main.py  
- Git: 2.51.0  

<br><br>

## ✅ 기능 목록 (요구사항 체크리스트)  






<br><br>

## 📁 파일 구조  
- `models`: 퀴즈 데이터 구조와 직렬화 담당  
- `views`: 콘솔 출력과 사용자 입력 담당  
- `controllers`: 메뉴 흐름과 게임 진행 담당  
- `services`: 상태 저장, 불러오기, 점수 관리 담당  
- `utils`: 공통 입력 검증, 예외 처리 보조 함수 담당  

```markdown
    📦 codysseyWeekTwo  
    ┣ 📂 app  
    ┃ ┣ 📂 controllers  
    ┃ ┣ 📂 models  
    ┃ ┣ 📂 services  
    ┃ ┣ 📂 utils  
    ┃ ┗ 📂 views  
    ┣ 📂 docs  
    ┃ ┗ 📂 requirements  
    ┣ 📂 public  
    ┃ ┗ 📂 screenshots  
    ┣ 📄 main.py  
    ┣ 📄 state.json  
    ┣ 📄 README.md  
    ┣ 📄 .gitignore  
    ┗ 📄 요구사항.md  
```





<br><br>

## 🗂️ 데이터 파일 설명  
> `state.json` 경로/역할/스키마  
- 경로: 프로젝트 루트 `state.json`  
- 역할: 퀴즈 목록과 최고 점수를 저장  

```json
{  
  "quizzes": [  
    {  
      "question": "문제",  
      "choices": ["선택지1", "선택지2", "선택지3", "선택지4"],  
      "answer": 1  
    }  
  ],  
  "best_score": 0  
}  
```

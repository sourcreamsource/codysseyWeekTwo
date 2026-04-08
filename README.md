# 🟩 2주차: Git과 함께하는 Python 첫 발자국  

## 📜 프로젝트 개요  
- Python 콘솔 퀴즈 게임을 만드는 프로젝트  
- Python과 Git은 "내가 만든 프로그램이 왜 이렇게 동작하는지"를 설명하고, 그 과정을 기록하며 성장하기 위한 핵심 도구  
- 구조는 문서 중심이 아니라 MVC 패턴 기준으로 잡는다.  
- `Quiz`, `QuizGame` 역할을 분리하고, `state.json`으로 퀴즈와 최고 점수를 저장한다.  

<br><br>

## 🖥️ 실행 환경  
- OS: macOS  
- Shell: zsh  
- Python: 3.11  
    - uv 설치  
        - brew install uv  
    - 환경 셋팅  
        - uv sync  
    - 실행  
        - uv run main.py  
- Git: 2.51.0  

<br><br>

## ✅ 진행 체크리스트  
- [ ] 프로젝트 기본 구조 정리  
- [ ] MVC 폴더 구조 생성  
- [ ] README 정비  
- [ ] Quiz 모델 구현  
- [ ] QuizGame 컨트롤러 구현  
- [ ] 콘솔 메뉴 뷰 구현  
- [ ] 파일 저장/불러오기 구현  
- [ ] 퀴즈 플레이 구현  
- [ ] 퀴즈 추가 / 목록 / 점수 기능 구현  

<br><br>

## 📋 주요 구조  

### 🟡 1. Application  
- [main.py](./main.py)  
- [app/models](./app/models)  
- [app/views](./app/views)  
- [app/controllers](./app/controllers)  
- [app/services](./app/services)  
- [app/utils](./app/utils)  

### 🟡 2. Documents  
- [요구사항.md](./요구사항.md)  
- [docs/requirements](./docs/requirements)  

### 🟡 3. Assets  
- [public/screenshots](./public/screenshots)  

<br><br>

## 🧠 설계 방향  
- `models`: 퀴즈 데이터 구조와 직렬화 담당  
- `views`: 콘솔 출력과 사용자 입력 담당  
- `controllers`: 메뉴 흐름과 게임 진행 담당  
- `services`: 상태 저장, 불러오기, 점수 관리 담당  
- `utils`: 공통 입력 검증, 예외 처리 보조 함수 담당  

<br><br>

## 📁 파일 구조  

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

## ▶ 실행 방법  

```bash
uv run main.py  
```

<br><br>

## 🗂️ 데이터 파일 설명  
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

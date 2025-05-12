# Nous Chat CLI

---

## Introduction (English)

**Nous Chat CLI** is a Python-based terminal application for real-time interaction with an AI chatbot.  
It supports saving/loading conversations, running scripted conversations, and now supports "AI vs AI" mode where two AIs interact with each other in user/assistant roles, along with multilingual prompts and robust error handling.

### Features

- Real-time conversation with the AI chatbot
- Save and load conversation logs (sessions) by name
- Scripted chat: have the bot automatically reply to a list of preset messages
- **AI vs. AI roleplay:** two AIs converse in assistant and user roles (with user-AI only asking questions)
- Multilingual prompt support (English, Korean)
- Solid error handling for file/network/server issues
- All conversation logs stored as JSON files

### Installation & Setup

1. **Install dependencies**
   ```bash
   pip install requests
   ```

2. **API Key Setup**
   - Create `api_key.py` in the project root and set your keys:
     ```python
     API_KEY = "YOUR_API_KEY_1"
     API_KEY2 = "YOUR_API_KEY_2"
     ```

### Usage

1. Run the CLI:
   ```bash
   python main.py
   ```

2. Select from the menu:
   - **1. Start New Chat:** Real-time chat with AI
   - **2. Load Existing Chat:** Resume a saved session
   - **3. Exit**
   - **4. Run Scripted Chat:** Auto-send preset questions to the AI
   - **5. Run AI vs. AI Roleplay:** Two AIs converse (choose language, roles)

3. Type `exit` or `quit` during chat to save and exit.

### Conversation Logs

- All chats are saved as JSON files in `chat_logs/`.
- The filename is based on the chosen session name.

### Notes

- Requires internet connection.
- API usage may incur charges – check your provider’s policy.

### Example Menu

```
=== Nous Chat CLI ===
1. 🆕 Start New Chat
2. 📂 Load Existing Chat
3. ❌ Exit
4. 🤖 Run scripted chat
5. 🤖🤖 Run AI vs. AI roleplay
Select option number:
```

### License

This project is free to use and modify.

---

## 소개 (Korean)

**Nous Chat CLI**는 터미널(커맨드라인) 환경에서 AI 챗봇과 실시간으로 대화하고 대화 내역을 관리할 수 있는 Python 기반 챗봇 어플리케이션입니다.  
저장/불러오기, 프리셋(스크립트) 자동 대화, **AI vs AI 역할극**(사용자 역할 AI가 질문만 하는 역할), 다국어(한글/영어) 프롬프트, 예외 안전성까지 폭넓게 지원합니다.

### 주요 기능

- 실시간 챗봇 대화
- 세션별 대화 기록 저장 및 불러오기
- 프리셋(문장 리스트) 자동 대화 진행
- **AI vs AI 역할극:** 두 AI가 번갈아가며 사용자/어시스턴트 역할로 상호 대화(질문만 하도록 프롬프트 강화)
- 한글/영어 다국어 프롬프트 지원
- 네트워크/파일 에러 robust 예외처리
- JSON 파일 기반 대화 로그 관리

### 설치 및 준비

1. 의존성 설치
   ```bash
   pip install requests
   ```

2. API 키 준비  
   - 프로젝트 루트에 `api_key.py` 파일을 생성 후 다음과 같이 작성
     ```python
     API_KEY = "YOUR_API_KEY_1"
     API_KEY2 = "YOUR_API_KEY_2"
     ```

### 사용 방법

1. 터미널에서 실행
   ```bash
   python main.py
   ```

2. 메뉴에서 원하는 기능 번호 선택  
   - **1. 새 대화 시작:** 실시간 챗봇 대화
   - **2. 기존 대화 불러오기:** 저장된 세션 불러오기
   - **3. 종료**
   - **4. 자동 문장 대화 실행:** 프리셋 리스트 자동 대화 진행
   - **5. AI vs AI 역할극:** (언어 선택 포함, 다양한 역할 프롬프트)

3. 대화 중 `exit` 또는 `quit` 입력시 저장 및 종료

### 대화 기록

- 모든 대화는 `chat_logs/` 폴더 내 JSON 파일로 저장
- 파일명은 세션명으로 관리

### 참고

- 반드시 인터넷 연결 필요
- API 호출시 서비스 별 요금/제한 정책에 유의

### 예시 화면

```
=== Nous Chat CLI ===
1. 🆕 새 대화 시작
2. 📂 기존 대화 불러오기
3. ❌ 종료
4. 🤖 자동 문장 대화 실행
5. 🤖🤖 AI vs. AI 역할극
번호 선택:
```

### 라이선스

본 프로젝트는 자유롭게 수정, 복제, 상업적 이용 가능합니다.
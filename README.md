# Nous Chat CLI

---

## Introduction (English)

**Nous Chat CLI** is a Python-based terminal application for real-time chatbot interaction.  
Supports conversation saving/loading, scripted (preset) chat, robust error handling, and especially an “AI vs AI Debate” mode – two AIs freely discuss a variety of topics as if they were real users, in both English and Korean.

### Features

- Real-time conversation with the AI chatbot
- Save/load sessions (JSON)
- Scripted chat (send preset lines automatically)
- **AI vs AI Debate mode:** Two AIs engage in a lively, open-ended discussion as if both were human users (not an assistant!). Topics change naturally, and answers/solutions/advice are avoided.
- Multilingual prompts (English/Korean)
- Robust error handling for network, file, server issues

### Installation & Setup

1. **Install dependencies**
   ```bash
   pip install requests
   ```

2. **API Key Setup**  
   - Create `api_key.py` in the project root:
     ```python
     API_KEY = "YOUR_API_KEY_1"
     API_KEY2 = "YOUR_API_KEY_2"
     ```

### Usage

1. Run:
   ```bash
   python main.py
   ```

2. Menu options:
   - **1. Start New Chat:** Real-time chat with AI
   - **2. Load Existing Chat:** Resume a saved session
   - **3. Exit**
   - **4. Run Scripted Chat:** Auto-send preset lines
   - **5. AI vs AI Debate:** Two AIs discuss freely as users; pick language, no “assistant” role

3. Enter `exit` or `quit` to save and exit during chat.

### Conversation Logs

- JSON files at `chat_logs/`
- Filenames are set on session creation

### Notes

- Requires internet connection  
- API use may incur charges, check your provider’s policy

### Example Menu

```
=== Nous Chat CLI ===
1. 🆕 Start New Chat
2. 📂 Load Existing Chat
3. ❌ Exit
4. 🤖 Run scripted chat
5. 🤖🤖 AI vs. AI debate
Select option number:
```

### License

This project is free to use, modify, and redistribute.

---

## 소개 (Korean)

**Nous Chat CLI**는 터미널(커맨드라인)에서 AI 챗봇과 대화하고,  
대화 내역을 저장/불러오거나, 프리셋 자동 대화,  
**“두 유저 AI의 자유 토론” (AI vs AI Debate)**, robust한 예외처리, 다국어 프롬프트까지 지원하는 Python 애플리케이션입니다.

### 주요 기능

- 실시간 챗봇 대화
- 대화 기록 세션 저장/불러오기 (JSON)
- 프리셋 리스트 자동 대화
- **AI vs AI 자유 토론** 모드:  
  두 AI가 “실제 사람 유저처럼” 다양한 주제로 찬반·질문·반박 등 자유롭게 논의  
  (상대방을 도와주거나 마무리/정답 안내 없이 계속 이어가도록 프롬프트 강화, 언어 선택 가능)
- 한글/영어 다국어 프롬프트
- 네트/저장 robust 예외처리

### 설치 및 준비

1. 의존성 설치
   ```bash
   pip install requests
   ```

2. API 키 준비  
   - 루트에 `api_key.py` 파일을 만들고
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
   - **1. 새 대화 시작**
   - **2. 기존 대화 불러오기**
   - **3. 종료**
   - **4. 자동 문장 대화 실행**
   - **5. AI vs AI 자유 토론** (언어 선택, 자유토론 유저프롬프트)

3. 대화 중 `exit` 혹은 `quit` 입력시 저장/종료

### 대화 기록

- 모든 대화는 `chat_logs/` 폴더 내 JSON 파일로 저장됨
- 세션명 기준 파일명으로 관리

### 참고

- 인터넷 필수
- API 과금 정책 유의

### 예시 화면

```
=== Nous Chat CLI ===
1. 🆕 새 대화 시작
2. 📂 기존 대화 불러오기
3. ❌ 종료
4. 🤖 자동 문장 대화 실행
5. 🤖🤖 AI vs. AI 자유 토론
번호 선택:
```

### 라이선스

본 프로젝트는 자유롭게 수정, 배포, 상업적 이용 가능합니다.
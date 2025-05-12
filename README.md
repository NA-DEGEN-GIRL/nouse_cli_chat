# Nous Chat CLI

## Introduction

**Nous Chat CLI** is a Python-based chatting application that allows you to freely converse with an AI chatbot in a terminal (command-line) environment, and save/manage your conversation history. It works with OpenAI-compatible chatbot APIs, providing features such as loading previous conversations, saving, scripted automatic chat, and exiting.

## Features

- Real-time conversation with the AI chatbot
- Save and load conversation logs (sessions) by name
- Run a scripted chat with a preset list of messages
- Easy conversation management and exit
- Conversation logs stored as JSON files

## Installation & Setup

1. **Install dependencies**
   ```bash
   pip install requests
   ```

2. **Prepare your API key**
   - Create a file named `api_key.py` in the project root and write your API key as follows:
     ```python
     API_KEY = [REDACTED]
     ```

## Usage

1. Run the following command in your terminal:
   ```bash
   python main.py
   ```

2. Select the number for the desired feature after the menu appears:
   - **Start New Chat:** Start a new conversation session.
   - **Load Existing Chat:** Load and continue a previously saved conversation.
   - **Exit:** Exit the program.
   - **Run Scripted Chat:** Send a predefined list of messages automatically and interact with the chatbot in batch mode.

3. While chatting, enter `exit` or `quit` to end and automatically save the conversation.

## Conversation Logs

- All chats are stored in the `chat_logs/` directory in JSON format.
- Filenames are based on the name you enter at the start of the session, managed separately per session.

## Notes

- Internet connection is required.
- API usage may incur charges, so please check your API service’s policy.

## Example Menu

```
=== Nous Chat CLI ===
1. 🆕 Start New Chat
2. 📂 Load Existing Chat
3. ❌ Exit
4. 🤖 Run scripted chat
Select option number:
```

## License

This project is free to modify and use.

---

# Nous Chat CLI

## 소개

**Nous Chat CLI**는 터미널(커맨드라인) 환경에서 AI 챗봇과 대화하고, 대화 내역을 저장·관리할 수 있는 Python 기반 애플리케이션입니다. OpenAI 호환 챗봇 API와 연동되며, 이전 대화 불러오기, 저장, **자동 문장 대화 실행**, 종료 등의 기능을 제공합니다.

## 주요 기능

- 챗봇과 실시간 대화
- 각 대화 기록(세션)별로 저장 및 불러오기
- 미리 정의된 문장 리스트로 자동 대화하기(배치 대화)
- 간편한 대화 종료 및 관리
- JSON 파일 기반으로 대화 로그 유지

## 설치 및 준비

1. **의존성 설치**
   ```bash
   pip install requests
   ```

2. **API 키 준비**
   - 프로젝트 루트에 `api_key.py` 파일을 생성한 뒤, 아래와 같이 본인의 API 키를 입력하세요.
     ```python
     API_KEY = [REDACTED]
     ```

## 사용 방법

1. 터미널에서 아래와 같이 실행합니다:
   ```bash
   python main.py
   ```

2. 메뉴에서 원하는 기능의 번호를 선택합니다.
   - **새 대화 시작:** 새로운 대화를 시작합니다.
   - **기존 대화 불러오기:** 저장된 대화 기록을 불러옵니다.
   - **종료:** 프로그램 종료.
   - **자동 문장 대화:** 미리 정의된 문장 리스트로 챗봇과 자동 대화를 진행합니다.

3. 대화 중 `exit` 또는 `quit`을 입력하면 대화가 종료되고 저장됩니다.

## 대화 기록

- 모든 대화는 `chat_logs/` 폴더에 JSON 파일 형태로 저장됩니다.
- 파일명은 대화 시작 시 입력한 이름이며, 각 세션별로 관리됩니다.

## 참고

- 인터넷 연결이 필요합니다.
- API 호출 시 과금이 발생할 수 있습니다. 본인의 서비스 정책을 확인해 주세요.

## 예시 화면

```
=== Nous Chat CLI ===
1. 🆕 새 대화 시작
2. 📂 기존 대화 불러오기
3. ❌ 종료
4. 🤖 자동 문장 대화 실행
번호 선택:
```

## 라이선스

해당 프로젝트는 자유롭게 수정 및 사용 가능합니다.
import requests
import os
import json
from datetime import datetime
from api_key import API_KEY

URL = "https://inference-api.nousresearch.com/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
LOG_DIR = "chat_logs"
os.makedirs(LOG_DIR, exist_ok=True)

def save_chat(name, messages):
    with open(f"{LOG_DIR}/{name}.json", "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)

def load_chat(name):
    with open(f"{LOG_DIR}/{name}.json", "r", encoding="utf-8") as f:
        return json.load(f)

def list_chats():
    files = [f[:-5] for f in os.listdir(LOG_DIR) if f.endswith(".json")]
    return sorted(files)

def chat_loop(messages, chat_name):
    print("💬 대화를 시작하세요. 'exit' 입력 시 종료됩니다.\n")
    while True:
        user_input = input("👤 You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("👋 대화를 종료합니다.\n")
            save_chat(chat_name, messages)
            break

        messages.append({"role": "user", "content": user_input})

        data = {
            "model": "Hermes-3-Llama-3.1-70B",
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 512
        }

        response = requests.post(URL, headers=HEADERS, json=data)
        res = response.json()
        reply = res["choices"][0]["message"]["content"]
        print(f"🤖 Bot: {reply}\n")
        messages.append({"role": "assistant", "content": reply})


def main_menu():
    while True:
        print("\n=== Nous Chat CLI ===")
        print("1. 🆕 새 대화 시작")
        print("2. 📂 기존 대화 불러오기")
        print("3. ❌ 종료")

        choice = input("번호 선택: ")

        if choice == "1":
            name = input("새 대화 이름 입력: ").strip()
            messages = [
                {"role": "system", "content": "You are a helpful assistant."}
            ]
            chat_loop(messages, name)

        elif choice == "2":
            chats = list_chats()
            if not chats:
                print("❗ 저장된 대화가 없습니다.")
                continue
            print("\n📄 저장된 대화 목록:")
            for i, c in enumerate(chats):
                print(f"{i + 1}. {c}")
            idx = input("불러올 대화 번호 선택: ")
            if not idx.isdigit() or int(idx) < 1 or int(idx) > len(chats):
                print("❗ 올바른 번호를 입력하세요.")
                continue
            name = chats[int(idx) - 1]
            messages = load_chat(name)
            chat_loop(messages, name)

        elif choice == "3":
            print("👋 종료합니다.")
            break
        else:
            print("❗ 잘못된 입력입니다.")

if __name__ == "__main__":
    main_menu()

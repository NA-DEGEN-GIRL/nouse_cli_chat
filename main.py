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
    print("💬 Start chatting. Type 'exit' to quit.\n")
    while True:
        user_input = input("👤 You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("👋 Ending the chat.\n")
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
        print("1. 🆕 Start New Chat")
        print("2. 📂 Load Existing Chat")
        print("3. ❌ Exit")

        choice = input("Select option number: ")

        if choice == "1":
            name = input("Enter a name for the new chat: ").strip()
            messages = [
                {"role": "system", "content": "You are a helpful assistant."}
            ]
            chat_loop(messages, name)

        elif choice == "2":
            chats = list_chats()
            if not chats:
                print("❗ No chat logs found.")
                continue
            print("\n📄 Saved chats:")
            for i, c in enumerate(chats):
                print(f"{i + 1}. {c}")
            idx = input("Select the number to load a chat: ")
            if not idx.isdigit() or int(idx) < 1 or int(idx) > len(chats):
                print("❗ Please enter a valid number.")
                continue
            name = chats[int(idx) - 1]
            messages = load_chat(name)
            chat_loop(messages, name)

        elif choice == "3":
            print("👋 Exiting.")
            break
        else:
            print("❗ Invalid input.")

if __name__ == "__main__":
    main_menu()

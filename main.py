import requests
import os
import json
from datetime import datetime
from api_key import API_KEY, API_KEY2

URL = "https://inference-api.nousresearch.com/v1/chat/completions"
HEADERS1 = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
HEADERS2 = {
    "Authorization": f"Bearer {API_KEY2}",
    "Content-Type": "application/json"
}
LOG_DIR = "chat_logs"
os.makedirs(LOG_DIR, exist_ok=True)


def save_chat(name, messages):
    try:
        with open(f"{LOG_DIR}/{name}.json", "w", encoding="utf-8") as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"❗ 대화 저장 에러: {e}")

def load_chat(name):
    try:
        with open(f"{LOG_DIR}/{name}.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"❗ 대화 불러오기 에러: {e}")
        return []

def list_chats():
    try:
        files = [f[:-5] for f in os.listdir(LOG_DIR) if f.endswith(".json")]
        return sorted(files)
    except Exception as e:
        print(f"❗ 채팅 목록 불러오기 에러: {e}")
        return []

def chat_loop(messages, chat_name):
    print("💬 Start chatting. Type 'exit' to quit.\n")
    while True:
        try:
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

            response = requests.post(URL, headers=HEADERS1, json=data)
            try:
                res = response.json()
                if "choices" not in res or not res["choices"]:
                    print("❗ AI 응답 오류 (choices 없음):", res)
                    continue
                reply = res["choices"][0]["message"]["content"]
            except Exception as e:
                print(f"❗ JSON 파싱 오류: {e}\n응답: {response.text}")
                continue

            print(f"🤖 Bot: {reply}\n")
            messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            print(f"❗ 예상치 못한 에러: {e}")
            break

def scripted_chat(messages, chat_name, prompts):
    print("🤖 Scripted chat started.\n")
    try:
        while 1:
            for user_input in prompts:
                print(f"👤 You: {user_input}")
                messages.append({"role": "user", "content": user_input})

                data = {
                    "model": "Hermes-3-Llama-3.1-70B",
                    "messages": messages,
                    "temperature": 0.7,
                    "max_tokens": 512
                }

                response = requests.post(URL, headers=HEADERS1, json=data)
                try:
                    res = response.json()
                    if "choices" not in res or not res["choices"]:
                        print("❗ AI 응답 오류 (choices 없음):", res)
                        continue
                    reply = res["choices"][0]["message"]["content"]
                except Exception as e:
                    print(f"❗ JSON 파싱 오류: {e}\n응답: {response.text}")
                    continue

                print(f"🤖 Bot: {reply}\n")
                messages.append({"role": "assistant", "content": reply})
    except Exception as e:
        print(f"❗ Scripted chat 에러: {e}")
    finally:
        save_chat(chat_name, messages)
        print("✅ Scripted chat finished and saved.\n")

def ai_vs_ai_chat(chat_name, first_prompt=None, num_turns=10, history_depth=3):
    print("🤖🤖 'AI 챗봇 ↔️ 사용자 역할 AI' 자동 대화를 시작합니다!\n")
    
    # 한글 프롬프트
    #system_ai_ko = {"role": "system", "content": "당신은 창의적이고 친절한 AI 어시스턴트입니다."}
    system_user_ko = {
        "role": "system",
        "content": (
        "진짜 사람 유저처럼 다양한 주제로 자유롭게 토론하세요. "
        "상대방의 의견에 공감하거나 반박할 수도 있고, 질문을 하거나 답해도 됩니다. "
        "토론이 한 쪽에서 마무리되는 분위기면 바로 다음 주제로 자연스럽게 전환하세요. "
        "절대 도움을 주는 어조(조언·정답·해결책 안내)는 삼가고, 가르치려 들지 말고, 친근하게 대화에 참여하세요. "
        "최대한 실제 토론방에서 두 사람이 대화하는 것처럼 자연스럽게, 다양한 관점·주제·리액션을 보여주세요. "
        "가끔은 파이썬, IT, 일상, 문화 등 다양한 범위의 주제를 스스로 꺼내도 좋고, 한 가지 주제에 너무 오래 머무르지 마세요. "                                                                                                             
        "정리, 요약, 마무리 멘트(‘이상으로 토론을 마치겠습니다’ 등)는 하지 말고, 대화가 길어져도 계속 새로운 주제로 이어가세요."
        "한국어만 사용하세요. 한자를 섞어쓰지말것."
        "상대는 한명입니다."
        )
    }
    first_prompt_ko = "토론하고 싶은 주제가 있나요?"

    #system_ai_en = {"role": "system", "content": "You are a helpful and creative assistant."}
    system_user_en = {
        "role": "system",
        "content": (
            "Engage in a discussion on a variety of topics as if you were a human user. "
            "Do NOT give advice, do NOT act as an assistant, and do NOT try to provide correct answers. "
            "If the current discussion seems to reach a conclusion or slow down, immediately start discussing another topic. "
            "Ask, answer, or respond as a real person would in a natural, casual debate. "
            "Do not summarize, close the conversation, or try to help. Change the topic often and keep the conversation lively."
            "Use English."
            "You have only one person to discuss."
        )
    }
    first_prompt_en = "Do you have any specific topic to discuss?"


    # 언어 선택
    print("언어를 선택하세요 / Choose language:")
    print("1. 한국어(Korean)")
    print("2. English")
    lang = input("번호 선택 (1/2): ").strip()
    if lang == "2":
        #system_ai = system_ai_en
        system_user = system_user_en
        if not first_prompt:
            #first_prompt = input(f"Enter first question (default: {first_prompt_en}): ").strip()
            #if not first_prompt:
            first_prompt = first_prompt_en
    else:
        #system_ai = system_ai_ko
        system_user = system_user_ko
        if not first_prompt:
            #first_prompt = input(f"첫 질문 입력 (기본: {first_prompt_ko}): ").strip()
            #if not first_prompt:
            first_prompt = first_prompt_ko

    conversation_history = []
    current_message = first_prompt

    for i in range(num_turns):
        try:
            if i % 2 == 0:

                messages = [system_user]
                for qa in conversation_history[-history_depth:]:
                    messages.append({"role": "user", "content": qa[0]})
                    messages.append({"role": "assistant", "content": qa[1]})
                messages.append({"role": "user", "content": current_message})

                response = requests.post(URL, headers=HEADERS1, json={
                    "model": "Hermes-3-Llama-3.1-405B",
                    "messages": messages,
                    "temperature": 0.9,
                    "max_tokens": 750
                })
                try:
                    res = response.json()
                    if "choices" not in res or not res["choices"]:
                        print("❗ AI1 응답 오류 (choices 없음):", res)
                        continue
                    reply = res["choices"][0]["message"]["content"]
                except Exception as e:
                    print(f"❗ AI1 JSON 파싱 오류: {e}\n응답: {response.text}")
                    continue

                print(f"🖥 AI1: {reply}\n")
                conversation_history.append((current_message, reply))
                current_message = reply

            else:
                # AI2(User)
                messages = [system_user]
                for qa in conversation_history[-history_depth:]:
                    messages.append({"role": "user", "content": qa[0]})
                    messages.append({"role": "assistant", "content": qa[1]})
                messages.append({"role": "user", "content": current_message})

                response = requests.post(URL, headers=HEADERS2, json={
                    "model": "Hermes-3-Llama-3.1-405B",
                    "messages": messages,
                    "temperature": 0.9,
                    "max_tokens": 750
                })
                try:
                    res = response.json()
                    if "choices" not in res or not res["choices"]:
                        print("❗ AI2 응답 오류 (choices 없음):", res)
                        continue
                    reply = res["choices"][0]["message"]["content"]
                except Exception as e:
                    print(f"❗ AI2 JSON 파싱 오류: {e}\n응답: {response.text}")
                    continue

                print(f"📡 AI2 : {reply}\n")
                conversation_history.append((current_message, reply))
                current_message = reply
        except Exception as e:
            print(f"❗ AI 챗봇 턴 진행 중 에러: {e}")

    print("✅ AI와 User AI간 대화가 완료되었습니다.\n")


def main_menu():
    while True:
        print("\n=== Nous Chat CLI ===")
        print("1. 🆕 Start New Chat")
        print("2. 📂 Load Existing Chat")
        print("3. ❌ Exit")
        print("4. 🤖 Run scripted chat")
        print("5. 🤖🤖 Run AI vs. AI chat")  # 추가 메뉴

        try:
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
                print("👋 Exiting.")
                break

            elif choice == "4":
                name = input("Enter a name for the scripted chat: ").strip()
                messages = [
                    {"role": "system", "content": "You are a helpful assistant."}
                ]
                prompts = [
                    "Give a fun python code",
                    "convert it to nodejs",
                    "convert it to rust",
                    "convert it to c++",
                    "make it more fun and complicated",
                ]
                scripted_chat(messages, name, prompts)
                
            elif choice == "5":
                name = input("Enter a name for the AI vs. AI chat: ").strip()
                ai_vs_ai_chat(name, num_turns=10000)

            else:
                print("❗ Invalid input.")
        except Exception as e:
            print(f"❗ 메뉴 처리 에러: {e}")

if __name__ == "__main__":
    main_menu()

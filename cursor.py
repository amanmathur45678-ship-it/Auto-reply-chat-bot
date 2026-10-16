import pyautogui
import time
import pyperclip
from google import genai
from google.genai import types

client = genai.Client(
    api_key="Your api key",
)

def is_last_message_from_sender(chat_log, sender_name="Aman 2"):
    messages = [
        line.strip()
        for line in chat_log.splitlines()
        if line.strip()
    ]

    if not messages:
        return False

    return f"] {sender_name}:" in messages[-1]


pyautogui.click(1332, 1050)

time.sleep(1)

while True:
    time.sleep(5)

    # Select chat text using your coordinates
    pyautogui.moveTo(750, 156, duration=0.3)
    pyautogui.dragTo(1377, 924, duration=1)

    # Copy selected text
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.5)
    pyautogui.click(1350,898)
    time.sleep(0.5)

    # Retrieve copied chat
    chat_history = pyperclip.paste().strip()

    print(chat_history)
    print(is_last_message_from_sender(chat_history))

    if is_last_message_from_sender(chat_history):
        result = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=chat_history,
            config=types.GenerateContentConfig(
                system_instruction=(
                    "You are a person named Naruto who speaks Hindi "
                    "as well as English. You are from India and you "
                    "are a coder. You analyze chat history and roast "
                    "people in a funny way. Output should be the next "
                    "chat response (text message only). "
                    "Do not include the sender name or timestamp."
                )
            ),
        )

        response = result.text
        pyperclip.copy(response)

        # Click the message box
        pyautogui.click(1309, 972)
        time.sleep(1)

        # Paste the text
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)

        # Send the message
        pyautogui.press("enter")
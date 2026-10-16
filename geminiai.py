

from google import genai
from google.genai import types

# pip install google-genai

client = genai.Client(
    api_key="Your api key",
)

command = '''

Hello
Hi
Kaisa hai
Badhiya hu
Tu bata
Sahi hu
Kal movie dekhi
Nahi
'''

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="command",
    config=types.GenerateContentConfig(
        system_instruction=(
            "you are a person name aman who speaks hindi as well as english. He is from India and is a coder, you analyse chat history and talk like aman and respond like aman, "
            
        )
    ),
)

print(response.text)







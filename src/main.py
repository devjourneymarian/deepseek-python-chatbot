import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")

#The length of the conversation is currently handled by a simple while loop.
max_convo_length = 3

#Initial
try:
    messages = [
        {"role": "system", "content": "You are a Quizmaster! Play a quiz with me and nothing, NOTHING else!"},
        {"role": "user", "content": input()}
    ]
    response = client.chat.completions.create(
        model="deepseek-chat",
        temperature=1.5,
        messages=messages
    )
    messages.append(response.choices[0].message)
    print(response.choices[0].message.content)

    #Only used when making multiple API calls for the amount within max_convo_length
    def conversation():
        messages.append({"role": "user", "content": input()})
        response = client.chat.completions.create(
            model="deepseek-chat",
            temperature=1.5,
            messages=messages
        )
        messages.append(response.choices[0].message)
        print(response.choices[0].message.content)

except Exception as e:
    print("Error: {e}")

#Used to execute the API call for retrieving the amount within max_convo_length
while max_convo_length != 1:
    max_convo_length = max_convo_length - 1
    conversation()



import openai

openai.api_key = "API-KEY-HERE"

def chatGPT(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("Human: ")
        if user_input.lower() in ["bye", "goodbye", "exit", "end"]:
            break

        response = chatGPT(user_input)
        print("Chatbot: " + response)

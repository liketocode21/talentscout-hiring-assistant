from groq import Groq

client = Groq(api_key="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")

def get_response(messages):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.7
    )
    return response.choices[0].message.content
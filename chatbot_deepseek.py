#!/usr/bin/env python3

"""
Simple chatbot with one role and one question, via openai class (request method).
Output in terminal.
"""

# import os, time
from openai import OpenAI


# Model setup
STEAM = True
MAX_TOKENS = 100
TEMPERATURE = 0.0

system_prompt = "Eres un asistente de IA útil y conciso Eres un asistente de IA útil y conciso, llamado Sebastian. Responde solo lo que se te pregunta."
user_prompt = "¿Cuáles son los 3 pasos principales para construir un agente de IA que consulte una base de datos?"

openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

# Chat with LLM
model_response = openai.chat.completions.create(
    model='deepseek-r1',
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    stream=STEAM,
    max_tokens=MAX_TOKENS,
    temperature=TEMPERATURE
)

print(f"{STEAM=}")


# Response result (in terminal)
if STEAM:
    response = ""
    for chunk in model_response:
        response += chunk.choices[0].delta.content or ''
        response = response.replace("```", "").replace(
            "markdown", "").replace("**", "")
        print(response)
        # time.sleep(0.3) # Comment this line for slow cpu
else:
    result = model_response.choices[0].message.content
    print(result)

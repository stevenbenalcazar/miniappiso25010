from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = """
Genera un caso de estudio único y original relacionado con fallas en un sistema de software, contextualizado dentro de una situación realista...
"""

try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un experto en calidad de software."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.9,
        max_tokens=350
    )
    generated_case = response.choices[0].message.content.strip()
except Exception as e:
    generated_case = f"Error al generar caso: {e}"

print(generated_case)

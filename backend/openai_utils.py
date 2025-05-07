import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Cliente nuevo

def analyze_case_with_ai(caso):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un experto en análisis de calidad de software."},
                {"role": "user", "content": f"Analiza este caso de falla en un sistema: {caso}"}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error al generar solución: {e}"

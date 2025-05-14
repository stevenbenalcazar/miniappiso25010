import openai
import os

# Simula que tienes la API key cargada desde .env
openai.api_key = os.getenv("OPENAI_API_KEY", "sk-your-test-key")

# Prompt para generar un caso de estudio con contexto y problemática, máx 200 palabras
prompt = """
Genera un caso de estudio único y original relacionado con fallas en un sistema de software, contextualizado dentro de una situación realista. El caso debe reflejar un problema que pueda ser analizado con la norma ISO/IEC 25010, incluyendo atributos como funcionalidad, fiabilidad, usabilidad, etc. Describe brevemente el contexto y luego la problemática. Limita la respuesta a un máximo de 200 palabras. No repitas casos previos y asegúrate de que el contenido sea coherente y diferente cada vez.
"""

# Simulación de una llamada a la API de OpenAI
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un experto en calidad de software."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.9,
        max_tokens=350
    )
    generated_case = response.choices[0].message["content"].strip()
except Exception as e:
    generated_case = f"Error al generar caso: {e}"

generated_case[:1000]  # Solo muestra los primeros 1000 caracteres (suficiente para verificar contenido)

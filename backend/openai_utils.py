import openai
import os

# Cargar clave API desde el entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_case_with_ai(case_text, iso_type):
    try:
        # Usamos la API correcta para chat completions con la nueva versión
        response = openai.ChatCompletion.create(
            model="gpt-4",  # o usa "gpt-3.5-turbo" si prefieres
            messages=[
                {"role": "system", "content": f"Estás ayudando a analizar un caso de estudio según ISO {iso_type}."},
                {"role": "user", "content": case_text}
            ],
            max_tokens=150,
            temperature=0.7,
        )
        return response['choices'][0]['message']['content'].strip()  # Obtener la respuesta correcta
    except Exception as e:
        return f"Error al generar solución: {str(e)}"

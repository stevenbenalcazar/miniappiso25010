import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Cliente actualizado con la API Key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def evaluate_solutions(caso, ia_solution, user_solution):
    prompt = f"""
Dado el siguiente caso de un fallo en un proceso de software:

{caso}

Se han propuesto dos soluciones:

Solución de la IA:
{ia_solution}

Solución del usuario:
{user_solution}

Evalúa cuál es mejor en base a la norma ISO/IEC 25010. Justifica tu decisión considerando los atributos: funcionalidad, rendimiento, compatibilidad, usabilidad, fiabilidad, seguridad, mantenibilidad y portabilidad.

Además, asigna una calificación del 1 al 10 a cada solución basada en su cumplimiento de la norma.
Ejemplo de salida:
- Solución IA: 8
- Solución Usuario: 6
Justificación: [explicación aquí]
"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=700
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error al evaluar soluciones: {str(e)}"

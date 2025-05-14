from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from openai_utils import analyze_case_with_ai
from evaluation import evaluate_solutions
import openai
import os

app = Flask(__name__, static_folder="../frontend", static_url_path="")
CORS(app)

# Configura la API key de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.json
    caso = data.get("caso")
    solucion_usuario = data.get("solucion_usuario")

    if not caso or not solucion_usuario:
        return jsonify({"error": "Faltan datos"}), 400

    solucion_ia = analyze_case_with_ai(caso)
    comparativa = evaluate_solutions(caso, solucion_ia, solucion_usuario)

    # Solicita calificación numérica
    try:
        score_prompt = f"""
Caso:
{caso}

Solución de la IA:
{solucion_ia}

Solución del usuario:
{solucion_usuario}

Del 0 al 100, ¿qué tan mejor es la solución del usuario comparada con la de la IA según la norma ISO/IEC 25010? Solo responde con un número entero.
"""
        score_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": score_prompt}],
            temperature=0,
            max_tokens=10
        )
        score = int("".join(filter(str.isdigit, score_response.choices[0].message["content"])))
    except:
        score = None

    return jsonify({
        "caso": caso,
        "solucion_ia": solucion_ia,
        "solucion_usuario": solucion_usuario,
        "evaluacion": comparativa,
        "calificacion_usuario_vs_ia": score
    })

@app.route("/api/generar-caso", methods=["GET"])
def generar_caso():
    prompt = """
Genera un caso de estudio original relacionado con un fallo de software, con contexto y problemática. Debe poder evaluarse con la norma ISO/IEC 25010. Usa máximo 200 palabras. Cada vez debe ser distinto.
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un experto en análisis de calidad de software."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.9,
            max_tokens=350
        )
        caso_generado = response.choices[0].message["content"].strip()
        return jsonify({"caso_generado": caso_generado})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

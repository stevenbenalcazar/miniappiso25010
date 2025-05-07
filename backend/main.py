from flask import Flask, request, jsonify
from flask_cors import CORS
from openai_utils import analyze_case_with_ai  # Asegúrate de que esta función esté bien definida
from evaluation import evaluate_solutions
import os

app = Flask(__name__)
CORS(app)  # Permite solicitudes desde frontend

@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.json
    caso = data.get("caso")
    solucion_usuario = data.get("solucion_usuario")

    if not caso or not solucion_usuario:
        return jsonify({"error": "Faltan datos"}), 400

    # ✅ Corrección: llama a la IA correctamente
    solucion_ia = analyze_case_with_ai(caso)

    # Evaluar comparativamente
    comparativa = evaluate_solutions(caso, solucion_ia, solucion_usuario)

    return jsonify({
        "caso": caso,
        "solucion_ia": solucion_ia,
        "solucion_usuario": solucion_usuario,
        "evaluacion": comparativa
    })

if __name__ == "__main__":
    app.run(debug=True)

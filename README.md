crear un archivo .env y colocar dentro:
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx

🚀 Instrucciones de instalación y uso
📦 Requisitos
Python 3.10+

Cuenta de OpenAI con una API Key válida

Navegador web moderno

🧰 Instalación
Clona el repositorio

bash
Copiar
Editar
git clone https://github.com/tuusuario/miniappiso25010.git
cd miniappiso25010
Crea un entorno virtual (opcional pero recomendado)

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
Instala las dependencias

bash
Copiar
Editar
pip install -r requirements.txt
Crea un archivo .env en la raíz del proyecto

ini
Copiar
Editar
OPENAI_API_KEY=tu_clave_secreta_aqui
⚠️ No compartas tu API Key públicamente.

▶️ Ejecución
Ejecuta el backend

bash
Copiar
Editar
python backend/main.py
Abre el archivo frontend/index.html en tu navegador.

🧪 Estructura del proyecto
bash
Copiar
Editar
miniappiso25010/
│
├── backend/
│   ├── main.py               # Servidor Flask
│   ├── evaluation.py         # Comparación con ISO/IEC 25010
│   ├── openai_utils.py       # Análisis con OpenAI
│
├── frontend/
│   ├── index.html            # Interfaz web
│   ├── script.js             # Lógica del frontend
│   └── style.css             # Estilos
│
├── .env                      # API Key de OpenAI
├── requirements.txt          # Dependencias
└── README.md

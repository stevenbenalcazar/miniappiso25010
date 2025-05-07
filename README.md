# 🧠 Evaluador ISO/IEC 25010

Este mini proyecto permite analizar fallos en procesos de software y compararlos con una solución generada por IA según los atributos de calidad definidos en la norma **ISO/IEC 25010**.

---

## 🚀 Instrucciones de instalación y uso

### 📦 Requisitos

- Python 3.10 o superior
- Cuenta de OpenAI con una API Key válida
- Navegador web moderno

---

### 🧰 Instalación

**Clona el repositorio**

```bash
- git clone https://github.com/tuusuario/miniappiso25010.git
- cd miniappiso25010

---

**(Opcional) Crea y activa un entorno virtual**

bash
Copiar
Editar
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate
Instala las dependencias

bash
Copiar
Editar
pip install -r requirements.txt
Configura tus variables de entorno

Crea un archivo .env en la raíz del proyecto y añade tu clave de OpenAI:

ini
Copiar
Editar
OPENAI_API_KEY=tu_clave_secreta
⚠️ No compartas tu API Key públicamente.

▶️ Ejecución del proyecto
Ejecuta el backend (Flask)

bash
Copiar
Editar
python backend/main.py
Abre el archivo frontend/index.html en tu navegador

Esto abrirá la interfaz para ingresar el caso, generar una solución IA y compararla con la solución del usuario.

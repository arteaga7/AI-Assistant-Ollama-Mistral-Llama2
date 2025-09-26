import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# --- 1. CONFIGURACIÓN DE OLLAMA ---
# Por defecto, Ollama se ejecuta en http://localhost:11434
# LangChain usa estas variables de entorno para saber dónde buscar el servidor OpenAI compatible.
# Asegúrate de que Ollama esté corriendo y Mistral esté cargado.
# Es una clave ficticia, no necesaria para Ollama local.
os.environ["OPENAI_API_KEY"] = "sk-ollama-local"
os.environ["OPENAI_API_BASE"] = "http://localhost:11434/v1"

# --- 2. INICIALIZAR EL MODELO LLM ---
# Usamos ChatOpenAI y le especificamos el modelo que descargaste.
# En este caso, el modelo 'mistral' que descargaste con 'ollama pull mistral'.
try:
    llm = ChatOpenAI(
        model="deepseek-r1",
        temperature=0.0  # Baja temperatura para respuestas más deterministas
    )
except Exception as e:
    print(f"Error al inicializar ChatOpenAI. Asegúrate de que Ollama está corriendo y el modelo 'mistral' está descargado.")
    print(f"Detalle del error: {e}")
    exit()

# --- 3. DEFINIR EL PROMPT Y LA CADENA ---
# Definimos la plantilla del prompt que enviaremos.
prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un asistente de IA útil y conciso, llamado Sebastian. Responde solo lo que se te pregunta."),
    ("user", "{pregunta}")
])

# Creamos una cadena simple: Prompt -> LLM -> Parser (para obtener la respuesta como string)
chain = prompt | llm | StrOutputParser()

# --- 4. HACER LA CONSULTA DE PRUEBA ---
pregunta_usuario = "¿Cuáles son los 3 pasos principales para construir un agente de IA que consulte una base de datos?"

print("--- Ejecutando Consulta ---")
print(f"Pregunta: {pregunta_usuario}")

# Invocar la cadena con la pregunta
respuesta = chain.invoke({"pregunta": pregunta_usuario})

print("\n--- Respuesta de Mistral (vía Ollama) ---")
print(respuesta)
print("---------------------------------------")

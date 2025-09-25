import os
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_agent

# --- 1. CONFIGURACIÓN DEL ENTORNO LOCAL ---

# 1.1. Configuración de Ollama (Mistral)
# Ollama expone un API compatible con OpenAI en localhost:11434/v1
# Clave ficticia para el conector de LangChain
os.environ["OPENAI_API_KEY"] = "sk-ollama-local"
os.environ["OPENAI_API_BASE"] = "http://localhost:11434/v1"

# 1.2. Configuración de PostgreSQL (AJUSTA ESTOS VALORES)
# Formato: postgresql://usuario:contraseña@host:puerto/nombre_base_de_datos
POSTGRES_USER = "tu_usuario"
POSTGRES_PASS = "tu_contraseña"
POSTGRES_HOST = "localhost"
POSTGRES_PORT = "5432"
POSTGRES_DB = "tu_base_de_datos"

DATABASE_URI = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

# 1.3. Tablas a exponer al LLM
TARGET_TABLES = ['dimSensors', 'dimDevices', 'factLecturas']


# --- 2. INICIALIZACIÓN DE COMPONENTES ---

# Inicializa el LLM local (Mistral)
print("Inicializando LLM Mistral (vía Ollama)...")
try:
    llm = ChatOpenAI(
        model="mistral",
        temperature=0.0
    )
except Exception as e:
    print(
        f"ERROR: No se pudo conectar a Ollama. Asegúrate de que está corriendo. Detalle: {e}")
    exit()

# Inicializa la conexión a PostgreSQL
print(f"Conectando a PostgreSQL en {POSTGRES_HOST}...")
try:
    db = SQLDatabase.from_uri(DATABASE_URI, include_tables=TARGET_TABLES)
    print(
        f"Conexión exitosa. Tablas disponibles para el LLM: {db.get_usable_table_names()}")
except Exception as e:
    print(
        f"ERROR: No se pudo conectar a la DB. Verifica la URI y el driver. Detalle: {e}")
    exit()

# --- 3. CREACIÓN DEL AGENTE SQL ---

# Crea el Agente SQL que orquesta el proceso
print("Creando el Agente SQL...")
agent_executor = create_sql_agent(
    llm=llm,
    db=db,
    agent_type="openai-tools",
    verbose=True  # Muestra el paso a paso: SQL generado, ejecución y resultado
)

# --- 4. EJECUCIÓN DE LA CONSULTA ---

pregunta_usuario = "muestra las primeras 5 filas de la tabla 'dimSensors'."

print("\n" + "="*50)
print(f"PREGUNTA AL AGENTE: {pregunta_usuario}")
print("="*50)

try:
    # Invocar el agente con la pregunta
    respuesta = agent_executor.invoke({"input": pregunta_usuario})

    print("\n" + "="*50)
    print("RESPUESTA FINAL DEL ASISTENTE:")
    print(respuesta['output'])
    print("="*50)

except Exception as e:
    print(f"\nOcurrió un error al ejecutar el agente: {e}")
    print("Verifica el log del Agente (si verbose=True) para ver la consulta SQL fallida.")

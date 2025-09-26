# AI-Assistant-Ollama-Mistral-Llama2
In this repository, an AI-Assistant is created, implementing Deepseek-r1, Mistral or Llama 2 models running locally on the Ollama server without internet connexion.

## Details

* "chatbot_deepseek.py": A simple chatbot with one role and one question, via openai class (request method). The output shows in terminal (script not tested).

* "agente_postgres.py": A simple chatbot with one role and performing one SQL query in table 'dimCities.csv', via openai class (request method). The output shows in terminal (script not tested).

## 🚀 Installation
1. Install Ollama:
```
curl -fsSL https://ollama.com/install.sh | sh
```
2. Download models (deepseek-r1, mistral or llama2). Notice that deepseek-r1 (size 1.1GB), mistral:7b (size 4.4GB), llama2:7b (size 3.8GB) and llama2:70b (size 39GB):
```
ollama pull deepseek-r1
```
3. Clone this repository:
```
git clone https://github.com/arteaga7/AI-Assistant-Ollama-Mistral-Llama2.git
```
4. Set virtual environment and install dependencies:
```
python3 -m venv env && source env/bin/activate && pip3 install -r requirements.txt
```

## How to run locally
1. Run deepseek-r1 model (Ollama server)
```
ollama run deepseek-r1
```
2. In another terminal, run the script "chatbot_deepseek.py":

```
python chatbot_deepseek.py
```
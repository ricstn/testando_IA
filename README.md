# 🥥 Avaliação de LLMs Locais: Gírias e Cultura de Salvador

Este projeto consiste em um conjunto de scripts em Python desenvolvidos para testar e avaliar a capacidade de Modelos de Linguagem (LLMs) locais em compreender e explicar gírias e expressões culturais de Salvador, Bahia.

O projeto compara o desempenho de inferência direta (via **Ollama**) contra inferência com contexto enriquecido (RAG via **AnythingLLM**), utilizando os modelos `deepseek-r1`, `qwen3.2` e `llama3.2`.

## 📂 Estrutura do Projeto

### 1. Geração de Dados
* **`gerar_perguntas.py`**: Script responsável por criar o dataset de testes.
    * Utiliza um banco de termos (gírias) pré-definido.
    * Filtra termos já utilizados.
    * Gera perguntas aleatórias com diferentes templates de prompts (ex: "Atue como um especialista...", "Qual o sentido de...").
    * **Output**: Gera arquivos `.md` (ex: `perguntas_246.md`).

### 2. Scripts de Execução
Existem três modos de interação com as IAs:

* **`1.script_ollama_teste.py`**:
    * *Objetivo:* Teste rápido de conectividade.
    * *Método:* Chamada simples à API do Ollama.
    
* **`2.script_ollama_Perguntas.py`**:
    * *Objetivo:* Teste de conhecimento base (Zero-shot/Few-shot).
    * *Método:* Lê o arquivo de perguntas gerado e consulta o Ollama diretamente.
    * *Output:* Salva as respostas em um arquivo Markdown formatado.

* **`3.script_ollama_RAG.py`**:
    * *Objetivo:* Teste de RAG (Retrieval-Augmented Generation).
    * *Método:* Envia as perguntas para a API do **AnythingLLM**, que utiliza documentos carregados no workspace para dar respostas mais precisas.
    * *Output:* Relatório Markdown contendo a pergunta e a resposta enriquecida.

### 3. Arquivos de Dados
* **`questionario_1.md` / `questionario_2.md`**: Arquivos de entrada contendo as perguntas formatadas, separadas por delimitadores (`---`).

---

## 🚀 Como Executar

### Pré-requisitos

1.  **Python 3.x** instalado.
2.  **Ollama** rodando localmente com os modelos baixados (`llama3.2:1b`, `deepseek-r1:1.5b`).
3.  **AnythingLLM** Desktop instalado e rodando (para o script de RAG).

### Instalação das Dependências

```bash
Instale as bibliotecas Python necessárias:

pip install requests ollama

Configuração
Para o script RAG (3.script_ollama_RAG.py):

Abra o AnythingLLM.

Vá em Settings -> Developer API e gere uma API Key.
Edite o arquivo 3.script_ollama_RAG.py e insira sua chave na variável API_KEY.
Certifique-se de que o WORKSPACE_SLUG corresponde ao nome do seu workspace no AnythingLLM.

Modelos:

Verifique se os modelos citados nos scripts estão instalados no seu Ollama:

Bash

ollama list
ollama pull <nome do modelo>
Executando os Testes
Passo 1: Gerar novas perguntas (Opcional)
  python gerar_perguntas.py

Passo 2: Rodar inferência direta no Ollama
  python 2.script_ollama_Perguntas.py

Passo 3: Rodar inferência via RAG (AnythingLLM)
  python 3.script_ollama_RAG.py

📊 Exemplos de Perguntas

O sistema gera variações de prompts para testar a robustez do modelo, como:
"Atue como um especialista em cultura popular da cidade de Salvador... O que significa a expressão 'Comer água'?"
"Defina a gíria 'Lá ele' de acordo com o vocabulário baiano."

🛠 Tecnologias Utilizadas
Python
Ollama
AnythingLLM

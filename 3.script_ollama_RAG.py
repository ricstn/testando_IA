import requests
import os
import time

# --- CONFIGURAÇÕES DE ARQUIVOS ---
ARQUIVO_ENTRADA = 'perguntas_1.md' # Certifique-se de o nome do arquivo de perguntas está correto
ARQUIVO_SAIDA = 'respostas3_deepseek-r1.md'

# --- CONFIGURAÇÕES DO ANYTHINGLLM ---
# URL base da API (padrão é localhost:3001)
BASE_URL = "http://localhost:3001/api/v1"

# Gere isso em: Settings -> Developer API -> Generate New API Key
API_KEY = "" # Adicione aqui a API Key

# O nome do seu workspace na URL (ex: se o link é .../workspace/projeto-teste, o slug é 'projeto-teste')
WORKSPACE_SLUG = "deepseek" 

def enviar_prompt_anythingllm(prompt_usuario):
    """
    Envia o prompt para a API do AnythingLLM via HTTP POST
    """
    url = f"{BASE_URL}/workspace/{WORKSPACE_SLUG}/chat"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "message": prompt_usuario,
        "mode": "chat" # Use 'chat' para manter contexto ou 'query' para pergunta isolada
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status() # Levanta erro se o status não for 200
        
        # A resposta do AnythingLLM geralmente vem no campo 'textResponse'
        dados = response.json()
        return dados.get('textResponse', 'Resposta vazia ou formato inesperado.')
        
    except requests.exceptions.RequestException as e:
        return f"Erro de conexão com AnythingLLM: {e}"
    except Exception as e:
        return f"Erro genérico: {e}"

def processar_arquivos():
    # 1. Verificar se arquivo de entrada existe
    if not os.path.exists(ARQUIVO_ENTRADA):
        print(f"Erro: O arquivo '{ARQUIVO_ENTRADA}' não foi encontrado.")
        return

    # 2. Ler as perguntas
    print(f"Lendo '{ARQUIVO_ENTRADA}'...")
    try:
        with open(ARQUIVO_ENTRADA, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return

    # Separa as perguntas usando o delimitador '---'
    lista_perguntas = [p.strip() for p in conteudo.split('---') if p.strip()]

    print(f"Encontradas {len(lista_perguntas)} perguntas. Iniciando processamento via AnythingLLM...\n")

    # 3. Processar e Gravar (Loop)
    with open(ARQUIVO_SAIDA, 'w', encoding='utf-8') as f_out:
        
        # Cabeçalho do arquivo de saída
        f_out.write(f"# Relatório de Perguntas e Respostas - RAG AnythingLLM\n")
        f_out.write(f"Workspace: {WORKSPACE_SLUG}\n\n")

        for i, pergunta in enumerate(lista_perguntas, 1):
            print(f"[{i}/{len(lista_perguntas)}] Enviando pergunta para o RAG...")
            
            # Chama a função adaptada para o AnythingLLM
            resposta = enviar_prompt_anythingllm(pergunta)
            
            # Formata a saída no estilo Markdown
            texto_formatado = (
                f"## Pergunta {i}\n"
                f"{pergunta}\n\n"
                f"### Resposta RAG\n"
                f"{resposta}\n\n"
                f"---\n\n"
            )
            
            # Escreve no arquivo imediatamente
            f_out.write(texto_formatado)
            
            print(f"   -> Resposta {i} salva.")
            
            # Pausa curta para evitar sobrecarga no servidor local (opcional)
            time.sleep(1)

    print(f"\nSucesso! Todas as respostas foram salvas em '{ARQUIVO_SAIDA}'.")

if __name__ == "__main__":
    processar_arquivos()
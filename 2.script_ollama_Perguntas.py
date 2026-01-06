import ollama
import os

# CONFIGURAÇÕES
ARQUIVO_ENTRADA = 'perguntas_246_2.md' # Certifique-se de o nome do arquivo de perguntas está correto
ARQUIVO_SAIDA = 'respostas2_3_deepseek-r1.md'
MODELO = 'deepseek-r1:1.5b'  # Certifique-se de que o modelo está baixado

def enviar_prompt_ia_local(prompt_usuario):
    try:
        response = ollama.chat(model=MODELO, messages=[
            {
                'role': 'user',
                'content': prompt_usuario,
            },
        ])
        return response['message']['content']
    except Exception as e:
        return f"Erro ao processar: {e}"

def processar_arquivos():
    # 1. Verificar se arquivo de entrada existe
    if not os.path.exists(ARQUIVO_ENTRADA):
        print(f"Erro: O arquivo '{ARQUIVO_ENTRADA}' não foi encontrado.")
        return

    # 2. Ler as perguntas
    print(f"Lendo '{ARQUIVO_ENTRADA}'...")
    with open(ARQUIVO_ENTRADA, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    # Separa as perguntas usando o delimitador '---'
    # O strip() remove espaços em branco extras no início/fim
    lista_perguntas = [p.strip() for p in conteudo.split('---') if p.strip()]

    print(f"Encontradas {len(lista_perguntas)} perguntas. Iniciando processamento...\n")

    # 3. Processar e Gravar (Loop)
    # Usamos 'w' para criar/sobrescrever o arquivo novo
    with open(ARQUIVO_SAIDA, 'w', encoding='utf-8') as f_out:
        
        # Cabeçalho do arquivo de saída
        f_out.write(f"# Relatório de Perguntas e Respostas - Modelo: {MODELO}\n\n")

        for i, pergunta in enumerate(lista_perguntas, 1):
            print(f"[{i}/{len(lista_perguntas)}] Enviando pergunta para IA...")
            
            # Chama a IA
            resposta = enviar_prompt_ia_local(pergunta)
            
            # Formata a saída no estilo Markdown
            texto_formatado = (
                f"## Pergunta {i}\n"
                f"{pergunta}\n\n"
                f"### Resposta IA\n"
                f"{resposta}\n\n"
                f"---\n\n"
            )
            
            # Escreve no arquivo imediatamente
            f_out.write(texto_formatado)
            
            print(f"   -> Resposta {i} salva.")

    print(f"\nSucesso! Todas as respostas foram salvas em '{ARQUIVO_SAIDA}'.")

if __name__ == "__main__":
    processar_arquivos()
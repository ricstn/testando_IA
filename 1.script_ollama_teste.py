import ollama

def enviar_prompt_ia_local(prompt_usuario):
    # O modelo deve estar instalado no seu Ollama
    # Certifique-se de indicar corretamente o nome do modelo na linha abaixo em "model="
    resposta = ollama.chat(model='llama3.2:1b', messages=[
        {
            'role': 'user',
            'content': prompt_usuario,
        },
    ])
    return resposta['message']['content']

# Exemplo de uso:
prompt = "Explique a diferença entre IA generativa e IA discriminativa em poucas palavras."
resposta_ia = enviar_prompt_ia_local(prompt)
print(f"Prompt: {prompt}")
print(f"Resposta da IA: {resposta_ia}")

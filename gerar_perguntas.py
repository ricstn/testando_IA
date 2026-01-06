import random

# 1. Termos que JÁ foram usados no exemplo anterior (serão ignorados)
termos_usados = [
    "teste"
]

# 2. Banco de Novos Termos extraídos do PDF (Gírias e expressões de salvador.pdf)
# Fonte: 
novos_termos = [
    # Letra A
    "A Migué", "Abafa-banca", "Abrir o Gás", "Abestalhado", "Acuendar", 
    "Água de salsicha", "Armengue", "Armengado", "Arretado", "A Pulso", "À Toa", "Abebinha", "Abecê", "Abeia", "Abusar", "Acaipora", "Ação", 
    "Acatar", "Afetado", "Agoniado", "Agourar", "Agreste", "Agrestia", "Água no chopp", 
    "Água-Dura", "Ai Fedeu", "Aimpim", "Alambrado", "Além da conta", "Alemão", "Amassado", 
    "Ameaçado", "Amerengado", "Amigo Secreto", "Amolado", "Andar na linha", "Andar no vacilo", 
    "Aonde", "Apavora", "Apertado", "Apertar o cinto", "Apontar", "Arabaca", "Arerê", 
    "Arraia", "Arreliar", "Arribar", "Arrodear", "Arroz de festa", "Assanhado", "Assento", 
    "Assistir (o jogo)", "Assuntar", "Atirado", "Atraque", "Atravessado", "Atravessar o sinal", 
    "Auê", "Ave Maria!", "Avexado", "Avionado", "Avoar", "Azeitado", "Azuado", "Azucrinar",
    
    # Letra B
    "Boca de 09", 
    "Baba", "Babado", "Barril", "Barril Dobrado", "Boca de me dê", 
    "Bolinho-de-estudante", "Brocou", "Badogue", "Bagunhar", "Bahêa", "Baita", "Baixar o santo", "Balaio de gato", "Baleado", 
    "Banca", "Banda", "Banho-de-Cuia", "Barão", "Baratino", "Barra", "Basqueteira", 
    "Bater no fundo", "Beinho", "Beleza", "Bestagem", "Bicho", "Bicho de sete cabeças", 
    "Bico", "Binga", "Birra", "Biscate", "Biscoito", "Boca-de-afofô", "Boca-de-lobo", 
    "Bocó", "Boiado", "Bolado", "Bom", "Bombom", "Bora", "Borboleta", "Borrão", 
    "Botar pilha", "Bozenga", "Bragueado", "Brau", "Brega", "Brenfa", "Brôco", 
    "Bronha", "Broto", "Bucha", "Bufa", "Bufento", "Bujão", "Bulir", "Bunda mole", "Buzu",
    
    # Letra C
    "Caceta", "Cacete armado", "Cacetinho", 
    "Cair a ficha", "Canetão", "Comer água", "Cabaré", "Cabeça-de-prego", "Cabrunco", "Cacareco", "Cachação", "Caco", "Café-com-leite", 
    "Cafona", "Cagar de sede", "Caguete", "Cair fora", "Cair Matando", "Cair na gandaia", 
    "Cair o pano", "Caixão e Vela", "Calçola", "Calmaí", "Camarão", "Cambada", "Cambito", 
    "Campado", "Canjica", "Cão chupando manga", "Capote", "Cara de fuinha", "Cara de paisagem", 
    "Cara de pum", "Carecer", "Caroara", "Carteira", "Carteirada", "Casa da porra", 
    "Casquinha", "Castelando", "Catiguria", "Certa feita", "Chamar Raul", "Checreté", 
    "Chegue", "Cheguei", "Cheio de guéri-guéri", "Cheio do pau", "Chelp", "Chiar", 
    "Chibata", "Chibiu", "Chibungo", "Chico", "Chifre", "Chororo", "Chouriçar", 
    "Chupa-molho", "Ciscar", "Classificador", "Coberta", "Cocada-de-amendoim", "Cocó", 
    "Colé", "Com certeza", "Comer barro", "Como quê", "Cordão", "Corrente", 
    "Correr a casa", "Correr atrás do prejuízo", "Corropio", "Couro comeu", "Cozinhar o galo", 
    "Creca", "Crendeuspai!", "Criar cabelo", "Criatura", "Crocodilagem", "Cucurute", 
    "Culhuda", "Curiar",
    
    # Letra D
    "Dar um zignal", "Dar um zig", "Dada", "Dalícia", "Daqui pra", "Dar (aula)", "Dar broca", "Dar lingua", "Dar no couro", 
    "Dar nome", "Dar ozadia", "Dar rasteira em cobra", "Dar testa", "Dar trela", 
    "Dar um agrado", "Dar um cheiro", "Dar um nó", "Dar um salto na cidade", "Dar um tiro", 
    "Dar uma dura", "Dar uma regulagem", "Dar uma roubada", "De bicuda", "De botuca", 
    "Dê cá", "De hoje", "De junto", "De marca", "De menor", "De prega", "Debaixo da saia", 
    "Defronte", "Deix'star", "Delegado", "Demorô!", "Desacerto", "Desapartar", 
    "Desassuntado", "Descaração", "Desembocar", "Desenchê", "Desmilinguido", "Despelar", 
    "Despirocado", "Destabocado", "Destrambelhado", "Deu revertério", "Deu zebra", 
    "Digaí!", "Dor de corno", "Doze horas da noite", "Dureza",
    
    # Letra E a Z (Seleção)
    "Lá ele", "Despongar", "Dor de facão", "Empata o baba", "Fatia-de-parida", 
    "Galalau", "Gastura", "Inhaca", "Jaburu", "Largar o doce", "Mão-de-figa", 
    "Na tora", "Não coma reggae", "Ó paí ó", "Oxente", "Oxe", "Peba", 
    "Pegar ar", "Perninha", "Plantado na testa", "Queixão", "Queixar", 
    "Receba", "Rodar a baiana", "Se pique", "Só você na fita", "Tabaréu", 
    "Talaricar", "Xaréu", "Zorra", "Canguinha", "É bala", "É ninhua", "É taca", "Eclér", "Em Comunicação", "Embecado", "Empesteado", 
    "Encanador", "Enfastiado", "Engarguelhar", "Enricar", "Enxame", "Esbuguelado", 
    "Espinha Mola", "Esporro", "Estabocar", "Estar na bruxa", "Fação", "Falapau", 
    "Farda", "Fazenda", "Filar aula", "Fren", "Fubua", "Gabiru", "Gala", "Garapa", 
    "Geladinho", "Gororoba", "Grade", "Grafite", "Héuris", "Humilhante", 
    "Interromper (o carro)", "Invasão", "Jante", "Jegue-manso", "Jogar um barro", 
    "Lá no jébi-jébi", "Laranjada", "Leseira", "Liso, leso e louco", "Mais eu", 
    "Malmente", "Mangar", "Massa", "Meu bom", "Migueloso", "Misse", "Mopai", 
    "Muriçoca", "Muvuca", "Na cocó", "Na intenção", "Na moral", "Na paleta", 
    "Nestante", "Nó-cego", "Painho", "Pandeiro", "Passado", "Passeio", "Pega a visão", 
    "Picado", "Pipocar", "Pongar", "Porreta", "Qual é a de mesmo?", "Renca", "Retado", 
    "Sinaleira", "Tá de calundu", "Tá mangaba", "Tolete", "Troncho", "Vá nessa", 
    "Viu", "Vixe", "Xeretar", "Zoiudo", "Zuada"
]

def gerar_arquivo_limpo():
    nome_arquivo = "perguntas_246.md"
    
    # 1. Filtragem: Remove duplicatas da lista de usados
    # Normalizamos para minúsculas para garantir que "Armengue" e "armengue" sejam vistos como iguais
    usados_lower = {t.lower() for t in termos_usados}
    lista_final = [t for t in novos_termos if t.lower() not in usados_lower]
    
    # Garante que não ultrapasse 200, mas tenta pegar o máximo possível
    limite = 500
    lista_final = lista_final[:limite]
    
    print(f"Termos disponíveis após filtragem: {len(lista_final)}")
    
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        # Cabeçalho opcional
        f.write("Quais são as principais características do dialeto soteropolitano? Responda de forma objetiva.\n---\n")
        
        count = 1
        total = len(lista_final)
        
        for i, termo in enumerate(lista_final):
            # Templates para variar a estrutura da pergunta
            templates = [
                f"Atue como um especialista em cultura popular da cidade de Salvador na Bahia. Responda à pergunta considerando EXCLUSIVAMENTE o contexto de gírias da cidade de Salvador. Não use definições matemáticas, físicas ou de política externa. Se a palavra tiver duplo sentido, priorize o sentido popular na Bahia. Responda em português brasileiro de forma objetiva. O que significa a expressão \"{termo}\" em Salvador?",
                f"Atue como um especialista em cultura popular da cidade de Salvador na Bahia. Responda à pergunta considerando EXCLUSIVAMENTE o contexto de gírias da cidade de Salvador. Não use definições matemáticas, físicas ou de política externa. Se a palavra tiver duplo sentido, priorize o sentido popular na Bahia. Responda em português brasileiro de forma objetiva. Defina a gíria \"{termo}\" de acordo com o vocabulário baiano.",
                f"Atue como um especialista em cultura popular da cidade de Salvador na Bahia. Responda à pergunta considerando EXCLUSIVAMENTE o contexto de gírias da cidade de Salvador. Não use definições matemáticas, físicas ou de política externa. Se a palavra tiver duplo sentido, priorize o sentido popular na Bahia. Responda em português brasileiro de forma objetiva. Qual o sentido de \"{termo}\" quando usado por um soteropolitano?",
                f"Atue como um especialista em cultura popular da cidade de Salvador na Bahia. Responda à pergunta considerando EXCLUSIVAMENTE o contexto de gírias da cidade de Salvador. Não use definições matemáticas, físicas ou de política externa. Se a palavra tiver duplo sentido, priorize o sentido popular na Bahia. Responda em português brasileiro de forma objetiva. Em que contexto se usa \"{termo}\" na Bahia?"
            ]
            pergunta = random.choice(templates)
            
            f.write(f"{pergunta}")
            
            # Adiciona separador se não for a última pergunta
            if i < total - 1:
                f.write("\n---\n")
            
            count += 1
            
    print(f"Arquivo '{nome_arquivo}' gerado com sucesso contendo {count} perguntas únicas!")

if __name__ == "__main__":
    gerar_arquivo_limpo()
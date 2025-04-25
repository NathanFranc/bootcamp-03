### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.


def verificar_dados(quantidade,preço) : 
    if quantidade > 0 and preço > 0:
        print("Dados Validos")            
        
    else:
            print("Dados invalidos")
            
verificar_dados(10, 25.99)
verificar_dados(-5, 15.50)
verificar_dados(0, 10.00)




### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

def classificar_temperatura(temperatura) :#valores abaixo de 10 são considerados "Baixos"
    if temperatura < 10:
        return "baixa"
    
    elif 10 <= temperatura <= 25: #valores enttre 10 e 25 são "Normal"
         return "normal"
    
    else:                       #valores acima de 25 são"Alta"
        return "alta"


print(classificar_temperatura(-10))
print(classificar_temperatura(15))
print(classificar_temperatura(30))


### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

def filtrar_log(log):
    if log['level'] == 'Error':
         print(log['message'])

log_exemplo = {
    'timestamp' : '2021-06-23 10:00:00',
    'level' : 'Error',
    'message':'falha na conexão'
}

filtrar_log(log_exemplo)




### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

def validar_usuario(usuario):
    # Validação de idade
    if not 18 <= usuario['idade'] <= 65:
        print("Erro: Idade deve estar entre 18 e 65 anos")
        return
    
    # Validação básica de email (contém @ e .)
    if '@' not in usuario['email'] or '.' not in usuario['email'].split('@')[-1]:
        print("Erro: Email inválido")
        return
    
    print("Dados de usuário válidos")

usuario1 = {'idade': 25, 'email': 'user@example.com'}
validar_usuario(usuario1)  # Válido

usuario2 = {'idade': 17, 'email': 'user@example.com'}
validar_usuario(usuario2)  # Erro de idade

usuario3 = {'idade': 30, 'email': 'invalido.com'}
validar_usuario(usuario3)  # Erro de email





### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

def transação_suspeita(transação) :
    valor_suspeito = transação['valor'] > 10000
    hora_suspeita = transação['hora'] < 9 or transação['hora'] > 18
    
    if valor_suspeito or hora_suspeita :
        return "transação suspeita"
    else :
        return "transaçâo normal"
    
transação1 = {'valor' : 12000, 'hora' : 20}  # suspeita (valor + hotario)
print(transação_suspeita(transação1))

transação2 = {'valor' : 5000, 'hora' : 20}   # suspeita (apenas horario)
print(transação_suspeita(transação2))

transaçâo3 = {'valor' : 12000, 'hora' : 12}  # suspeita (apenas valor)
print(transação_suspeita(transaçâo3))

transaçâo4 = {'valor' : 5000, 'hora' : 12}  # suspeita (normal)
print(transação_suspeita(transaçâo4))
        




### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.


def contar_palavras_simples(texto):
    texto = texto.lower()
    for char in '.,!?;:':
        texto = texto.replace(char, ' ')
    
    palavras = texto.split()
    contagem = {}
    
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    
    return contagem






### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.


def normalizar(lista):
    if not lista:
        return []
    
    min_val = min(lista)
    max_val = max(lista)
    
    # Evita divisão por zero quando todos valores são iguais
    if min_val == max_val:
        return [0.0 for _ in lista]
    
    return [(x - min_val) / (max_val - min_val) for x in lista]

# Exemplos de uso:
print(normalizar([10, 20, 30, 40]))  # [0.0, 0.333..., 0.666..., 1.0]
print(normalizar([5, 5, 5]))         # [0.0, 0.0, 0.0]
print(normalizar([-1, 0, 1]))        # [0.0, 0.5, 1.0]




### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando




def filtrar_faltantes(usuarios, campo):
    return [usuario for usuario in usuarios if campo not in usuario]

# Exemplo de uso:
usuarios = [
    {'nome': 'Alice', 'idade': 30, 'email': 'alice@example.com'},
    {'nome': 'Bob', 'idade': 25},  # Faltando 'email'
    {'email': 'charlie@example.com', 'cidade': 'São Paulo'}  # Faltando 'idade'
]

# Filtrar usuários sem 'email'
print(filtrar_faltantes(usuarios, 'email'))  
# Saída: [{'nome': 'Bob', 'idade': 25}]

# Filtrar usuários sem 'idade'
print(filtrar_faltantes(usuarios, 'idade'))  
# Saída: [{'email': 'charlie@example.com', 'cidade': 'São Paulo'}]




### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.




def extrair_pares(lista):
    return [num for num in lista if num % 2 == 0]

# Exemplos de uso:
print(extrair_pares([1, 2, 3, 4, 5]))       # Saída: [2, 4]
print(extrair_pares([-2, -3, 0, 7]))        # Saída: [-2, 0]
print(extrair_pares([2, 4, 6]))             # Saída: [2, 4, 6]
print(extrair_pares([]))                    # Saída: []





### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.





vendas = [
    {'categoria': 'eletrônicos', 'valor': 1200},
    {'categoria': 'livros', 'valor': 300},
    {'categoria': 'eletrônicos', 'valor': 800},
    {'categoria': 'roupas', 'valor': 450},
    {'categoria': 'livros', 'valor': 150}
]

def total_por_categoria(vendas):
    categorias = {}
    for venda in vendas:
        categoria = venda['categoria']
        valor = venda['valor']
        if categoria in categorias:
            categorias[categoria] += valor
        else:
            categorias[categoria] = valor
    return categorias

print(total_por_categoria(vendas))



# Saída: {'eletrônicos': 2000, 'livros': 450, 'roupas': 450}







### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

dados = []
entrada = ""

while entrada.lower() != "sair":
    entrada = input("Digite um valor (ou 'sair' para terminar): ")
    if entrada.lower() != "sair":
        dados.append(entrada)
        print("dados coletados:",  dados)


### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

numero = int(input("Digite um número entre 1 e 10: "))
while numero < 1 or numero > 10:
    print("Número fora do intervalo!")
    numero = int(input("Por favor, digite um número entre 1 e 10: "))

print("Número válido!")






### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.



pagina_atual = 1
paginas_totais = 5  

while pagina_atual <= paginas_totais:
    print(f"Processando página {pagina_atual} de {paginas_totais}")
  
    pagina_atual += 1

print("Todas as páginas foram processadas.")



### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.



tentativas_maximas = 5
tentativa = 1

while tentativa <= tentativas_maximas:
    print(f"Tentativa {tentativa} de {tentativas_maximas}")

    if True:  
        print("Conexão bem-sucedida!")
        break
    tentativa += 1
else:
    print("Falha ao conectar após várias tentativas.")




### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.



itens = [1, 2, 3, "parar", 4, 5]

i = 0
while i < len(itens):
    if itens[i] == "parar":
        print("Parada encontrada, encerrando o processamento.")
        break

    print(f"Processando item: {itens[i]}")
    i += 1
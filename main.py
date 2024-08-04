# FUNÇÕES
# Início de função dimensoesOjbjeto
def dimensoesObjeto():
    print('--------- Menu de dimensões do objeto --------- ') # Exibe menu de dimensões
    while True: # Loop de verificação
        try:
            altura = float(input('Digite a altura do objeto em CM: ')) # Pergunta a altura
            comprimento = float(input('Digite o comprimento do objeto em CM: ')) # Pergunta o comprimento
            largura = float(input('Digite a largura do objeto em CM: ')) # Pergunta a largura
            volume = float(altura * largura * comprimento) # Calcula o volume total
            print(f'O volume do objeto é de: {volume} cm³') # Imprime o volume total

            if volume < 1000: # Verifica as condições
                return 10.00
            elif 1000 <= volume < 10000:
                return 20.00
            elif 10000 <= volume < 30000:
                return 30.00
            elif 30000 <= volume < 100000:
                return 50.00
            else: # Valores fora dos indicados
                print('As dimensões do objeto não são aceitas.\n' +
                      'Digite as dimensões novamente.')
                continue
        except ValueError: # Valor não numérico foi digitado
            print('Digite um valor válido novamente.')
        continue
# Final da função dimensoesOjbeto

# Início da função pesoObjeto
def pesoObjeto():
    print('--------- Menu de peso do objeto --------- ') # Exibe menu de peso
    while True:
        try: # Loop de detecção
            peso = float(input('Digite o peso do objeto em KG: ')) # Pergunta o peso do produto
            if (peso <= 0.1): # Compara o peso com os outros valores anteriores
                return 1
            elif (0.1 <= peso < 1):
                return 1.5
            elif (1 <= peso < 10):
                return 2
            elif (10  <= peso < 30):
                return 3
            else: # Indica que o peso não é válido
                print('Este peso não é aceito.')
                continue

        except ValueError: # Valor não numérico foi digitado.
            print('Peso não válido, digite novamente.')
        continue
# Final da funçãp pesoObjeto

# Início da função rotaObjeto
def rotaObjeto():
    print('--------- Menu de rotas de transporte --------- ') # Exibe menu de rotas
    while True: # Loop de verificação
        try:
            rotas = input('Opções de rotas:\n' 'RS - Rio de Janeiro até São Paulo\n'
                         'SR - São Paulo até Rio de Janeiro\n' 'BS - Brasília até São Paulo\n'
                         'SB - São Paulo até Brasília\n' 'BR - Brasília até Rio de Janeiro\n'
                         'RB - Rio de Janeiro até Brasília\n' 'Dentre as opções acima, digite a sigla da rota desejada: ') # Opções de rotas
            if (rotas == 'RS') or (rotas == 'rs') or (rotas == 'SR') or (rotas == 'sr'): # Compara valores
                return 1
            elif (rotas == 'BS') or (rotas == 'bs') or (rotas == 'SB') or (rotas == 'sb'):
                return 1.2
            elif (rotas == 'BR') or (rotas == 'br') or (rotas == 'RB') or (rotas == 'br'):
                return 1.5
            else: # Caractere digitado não válido
                print('Rota inválida.')
                continue
        except ValueError: # Caractere não válido, pede para tentar de novo.
            print('Rota não válida, digite novamente.')
            continue
# Fim da função rotaObjeto

# Programa principal
print('Seja bem-vindo à empresa de logística de Geovanna Melo! RU: 4466904\n') # Apresentação da empresa

volumeObj = dimensoesObjeto() # Valor da função dimensoesObjeto
pesoObj = pesoObjeto() # Valor da função pesoObjeto
rotaObj = rotaObjeto() # Valor da função rotaObejeto
total = (volumeObj * pesoObj * rotaObj) # Cálculo do valor total

print(f'Especificações: Volume: {volumeObj} cm³, Peso: {pesoObj} KG, Rota: {rotaObj}\n' +
              f'Valor final do objeto é de R${total:.2f}.') # Imprime valor final com especificações do pedido.

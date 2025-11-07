"""
randomlib.py
------------

Uma biblioteca simples e independente para gerar números pseudoaleatórios
baseados no tempo atual do sistema (milissegundo, microsegundo, nanosegundo e timestamp).

Autor: [Sam Jamsh]
Licença: Apache License 2.0
Versão: 1.0
"""

import time
import datetime
from random import randrange
from collections import Counter


class generate_random():
   

    def __init__(self, a, b, s):
        self.a = a
        self.b = b
        self.s = s

        # Gera número aleatório
        self.all = self.generate_random_number(a, b, s)

        # Exibe resultado
        #print(f"\nNúmero aleatório gerado: {num}")
   


    def abs_custom(self, value):

        """
    Retorna o valor absoluto de 'value' sem usar a função abs() nativa.
    Se for negativo, multiplica por -1.
        """
        if value < 0:
            return value * -1
        else:
            return value


    def get_time(self):
        """
    Obtém o tempo atual do sistema e retorna os componentes necessários
    para geração do seed aleatório.
        """
        now = datetime.datetime.now()           # captura data e hora atuais
        hora = now.hour                         # extrai a hora
        minuto = now.minute                     # extrai o minuto
        segundo = now.second                    # extrai o segundo
        micro_segundo = now.microsecond         # extrai o microsegundo
        mili_segundo = micro_segundo // 1000    # converte micro → mili
        nano_segundo = int(time.time_ns() % 1e9)# captura os nanossegundos (resto de 1 segundo)
        timestamp = time.time_ns()              # timestamp total em nanossegundos (desde 1970)
        nnano = int(time.time_ns() % 1000000)   # uma versao do nano
        return hora, minuto, segundo, mili_segundo, micro_segundo, nano_segundo, timestamp, nnano




    def generate_random_number(self, a, b, x=31):

        """
        Gera um número pseudoaleatório dentro do intervalo [a, b],
        combinando o tempo do sistema e operações bit a bit.

        Parâmetros:
        - a (int): valor mínimo do intervalo
        - b (int): valor máximo do intervalo
        - x (int): fator multiplicador opcional (seed base), padrão = 10
        r"""
        if b < a:
            raise ValueError("O valor máximo 'b' deve ser maior ou igual ao mínimo 'a'.")


          # Captura todos os tempos necessários
        hora, minuto, segundo, mili, micro, nano, timestamp, nnano = self.get_time()

        x = mili

        # Cria o seed combinando os tempos e o parâmetro x
        seed = self.abs_custom(((nano * x + mili + nano) ^ nano) ^ timestamp)

        #print("seed:", seed)

        # Gera número pseudoaleatório no intervalo [a, b]
        random_number = ((seed * (nnano + nano + mili)) % (b - a + 1)) + a

        calc1 = (seed * (nnano + mili + nano) * nano + mili) 

        calc2 = ((b - a + 1) + a) - 1

        new = seed % calc2 + 1

        last = ((seed * calc1) % calc2) + 1

        original = randrange(a, b + 1)
        #print("calc1:", calc1)
        #print("calc2:", calc2)
        #print("new:", new)
        #print("random:", random_number)
        #print("last:", last)
        #print("original random func:", original)

        #return random_number
        return new, random_number, last, original
    
    def getall(self):
        return self.all



if __name__ == "__main__":

    print("=== RandomLib - Automatic Simulator ===\n")

    new_list = []          # lista para armazenar todos os resultados do algoritmo new
    random_list = []       # lista para armazenar todos os resultados do algoritmo random
    last_list = []         # lista para armazenar todos os resultados do algoritmo last
    original_list = []     # lista para armazenar todos os resultados do algoritmo original
    new, random_number, last, original = 0, 0, 0, 0

    simulations = 500   # how many simulations (simulations number/quantity)

    for i in range(simulations):
        # Define intervalo manualmente
        #a = int(input("Digite o valor mínimo do intervalo: "))
        #b = int(input("Digite o valor máximo do intervalo: "))
        a, b = 1, 10

        generator = generate_random(a, b, 31)      # realiza a simulacao (1x)
        new, random_number, last, original = generator.getall()  # obtem os resultados da simulacao realizada

        # adiciona nas respectivas listas os resultodos da simulacao realizada (de todos os algoritmos) 
        new_list.append(new)
        random_list.append(random_number)
        last_list.append(last)
        original_list.append(original)

        # calcula e imprime o percentual do progresso na tela
        percents = ((i + 1) / simulations) * 100
        progress = f" {percents:.1f}% "
        print(progress)

        time.sleep(0.2)   # espera por sec/milisec para cada simulacao executada


    NEW = Counter(new_list)
    RANDOM = Counter(random_list)
    LAST = Counter(last_list)
    ORIGINAL = Counter(original_list)

    most_new = NEW.most_common(1)[0]
    least_new = min(NEW.items(), key=lambda x: x[1])
    new_most_repeated = most_new[0]
    new_most_repeated_qty = most_new[1]
    new_least_repeated = least_new[0]
    new_least_repeated_qty = least_new[1]
    new_most_percent = (new_most_repeated_qty / simulations) * 100
    new_least_percent = (new_least_repeated_qty / simulations) * 100

    most_random = RANDOM.most_common(1)[0]
    least_random = min(RANDOM.items(), key=lambda x: x[1])
    random_most_repeated = most_random[0]
    random_most_repeated_qty = most_random[1]
    random_least_repeated = least_random[0]
    random_least_repeated_qty = least_random[1]
    random_most_percent = (random_most_repeated_qty / simulations) * 100
    random_least_percent = (random_least_repeated_qty / simulations) * 100

    most_last = LAST.most_common(1)[0]
    least_last = min(LAST.items(), key=lambda x: x[1])
    last_most_repeated = most_last[0]
    last_most_repeated_qty = most_last[1]
    last_least_repeated = least_last[0]
    last_least_repeated_qty = least_last[1]
    last_most_percent = (last_most_repeated_qty / simulations) * 100
    last_least_percent = (last_least_repeated_qty / simulations) * 100

    most_original = ORIGINAL.most_common(1)[0]
    least_original = min(ORIGINAL.items(), key=lambda x: x[1])
    original_most_repeated = most_original[0]
    original_most_repeated_qty = most_original[1]
    original_least_repeated = least_original[0]
    original_least_repeated_qty = least_original[1]
    original_most_percent = (original_most_repeated_qty / simulations) * 100
    original_least_percent = (original_least_repeated_qty / simulations) * 100


    print('\n')
    print("\nNew (most repeated | times repeated | percentage):", f"{new_most_repeated} | {new_most_repeated_qty} | {new_most_percent:.2f}%")
    print("\nNew (least repeated | times repeated | percentage):", f"{new_least_repeated} | {new_least_repeated_qty} | {new_least_percent:.2f}%")
    print('\n')
    print("\nRandom (most repeated | times repeated | percentage):", f"{random_most_repeated} | {random_most_repeated_qty} | {random_most_percent:.2f}%")
    print("\nRandom (least repeated | times repeated | percentage):", f"{random_least_repeated} | {random_least_repeated_qty} | {random_least_percent:.2f}%")
    print('\n')
    print("\nLast (most repeated | times repeated | percentage):", f"{last_most_repeated} | {last_most_repeated_qty} | {last_most_percent:.2f}%")
    print("\nLast (least repeated | times repeated | percentage):", f"{last_least_repeated} | {last_least_repeated_qty} | {last_least_percent:.2f}%")
    print('\n')
    print("\nOriginal (most repeated | times repeated | percentage):", f"{original_most_repeated} | {original_most_repeated_qty} | {original_most_percent:.2f}%")
    print("\nOriginal (least repeated | times repeated | percentage):", f"{original_least_repeated} | {original_least_repeated_qty} | {original_least_percent:.2f}%")
    print('\n')

    # codigos ansi
    RESET = "\033[0m"
    BOLD = "\033[1m"
    
    # cores basicas
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    ORANGE = "\033[38;5;214m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    
    # cores em negrito
    RED_BOLD = "\033[1;91m"
    GREEN_BOLD = "\033[1;92m"
    YELLOW_BOLD = "\033[1;93m"
    ORANGE_BOLD = "\033[1;38;5;214m"

    def get_most_score(value):
        if value <= 11.0:
            return f'{GREEN_BOLD}perfeito{RESET}'
        elif value <= 13.0:
            return f'{GREEN}otimo{RESET}'
        elif value <= 14.5:
            return f'{YELLOW}bom{RESET}'
        elif value < 17.5:
            return f'{ORANGE}aceitavel{RESET}'
        else:
            return f'{RED}nao aceitavel{RESET}'
        
    def get_least_score(value):
        if value >= 9.0:
            return f'{GREEN_BOLD}perfeito{RESET}'
        elif value >= 8.0:
            return f'{GREEN}otimo{RESET}'    
        elif value > 7.0:
            return f'{YELLOW}bom{RESET}'
        elif value >= 5.5:
            return f'{ORANGE}aceitavel{RESET}'
        else:
            return f'{RED}nao aceitavel{RESET}'

 

    info = get_most_score(new_most_percent)
    print(f"New Most: [{info}]")

    info = get_least_score(new_least_percent)
    print(f"New Least: [{info}]")


    print("\n")


    info = get_most_score(random_most_percent)
    print(f"Random Most: [{info}]")

    info = get_least_score(random_least_percent)
    print(f"Random Least: [{info}]")


    print("\n")


    info = get_most_score(last_most_percent)
    print(f"Last Most: [{info}]")

    info = get_least_score(last_least_percent)
    print(f"Last Least: [{info}]")


    print("\n")


    info = get_most_score(original_most_percent)
    print(f"Original Most: [{info}]")

    info = get_least_score(original_least_percent)
    print(f"Original Least: [{info}]")


    print("\n")


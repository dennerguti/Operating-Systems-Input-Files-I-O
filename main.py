import time
import random

nome_arquivo = 'entrada_ES.txt'
processos = []
processos_bloqueados = []
unidade_tempo_atual = 0
contador_global = 0

def gerar_informacao_aleatoria(chance_requisitar_ES):
    chance = random.randint(1, 100)
    if chance <= chance_requisitar_ES:
        tempo = random.randint(1, 9)
        dispositivo = random.choice(dispositivos)
        ponto_bloqueio = unidade_tempo_atual + tempo  
        print()
        return f"Chance | {chance} | Tempo | {tempo} | Dispositivo | {dispositivo[0]}", ponto_bloqueio
    else:
        print()
        return f"Chance | {chance} (Não requisitou ES)", None


with open(nome_arquivo, 'r') as arquivo:
    linhas = arquivo.readlines()

# Processar as informações dos dispositivos
dispositivos_info = linhas[0].strip().split('|')
numero_dispositivos = int(dispositivos_info[-1])

# Processa os dispositivos
dispositivos = []
for i in range(1, numero_dispositivos + 1):
    dispositivo_info = linhas[i].strip().split('|')
    nome_dispositivo = dispositivo_info[0]
    uso_simultaneo = int(dispositivo_info[1])
    tempo_operacao = int(dispositivo_info[2])
    dispositivos.append((nome_dispositivo, uso_simultaneo, tempo_operacao))

# Processa os dados
for linha in linhas[numero_dispositivos + 1:]:
    campos = linha.strip().split('|')
    nome_processo = campos[0]
    tempo_execucao = int(campos[2])
    chance_requisitar_ES = int(campos[-1])
    processos.append((nome_processo, tempo_execucao, chance_requisitar_ES))

#Escalonador resumido
while processos:
    processo_em_execucao = processos.pop(0)
    nome_processo, tempo_execucao, chance_requisitar_ES = processo_em_execucao
    ponto_bloqueio = None  

    informacao_aleatoria, ponto_bloqueio = gerar_informacao_aleatoria(chance_requisitar_ES)
    if informacao_aleatoria:
        print(informacao_aleatoria)
        contador_global = 0 
        tempo_execucao_atual = 0 

    while tempo_execucao > 0:
        if ponto_bloqueio is not None and unidade_tempo_atual == ponto_bloqueio:
            processos_bloqueados.append((nome_processo, dispositivos[2]))  
            break  

        print(f"Tempo {unidade_tempo_atual}: {nome_processo} | {tempo_execucao}")
        tempo_execucao -= 1
        unidade_tempo_atual += 1
        #time.sleep(1)

        contador_global += 1  
        tempo_execucao_atual += 1 

        if contador_global == 10 or tempo_execucao_atual == 10:
            break

    if tempo_execucao > 0:
        processos.append((nome_processo, tempo_execucao, chance_requisitar_ES))
    else:
        print(f"{nome_processo} concluído.")



print("Informações dos Dispositivos:")
for dispositivo in dispositivos:
    print("Nome do Dispositivo:", dispositivo[0])
    print("Uso Simultâneo:", dispositivo[1])
    print("Tempo de Operação:", dispositivo[2])
    print()

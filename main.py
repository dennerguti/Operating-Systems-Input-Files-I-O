import time
import random

class Dispositivo:
    def __init__(self, nome, uso_simultaneo, tempo_operacao):
        self.nome = nome
        self.uso_simultaneo = uso_simultaneo
        self.tempo_operacao = tempo_operacao

class Processo:
    def __init__(self, nome, tempo_execucao, chance_requisitar_ES):
        self.nome = nome
        self.tempo_execucao = tempo_execucao
        self.chance_requisitar_ES = chance_requisitar_ES
        self.ponto_bloqueio = None

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    return linhas

def processar_dispositivos(linhas):
    dispositivos_info = linhas[0].strip().split('|')
    numero_dispositivos = int(dispositivos_info[-1])
    dispositivos = []
    for i in range(1, numero_dispositivos + 1):
        dispositivo_info = linhas[i].strip().split('|')
        nome_dispositivo = dispositivo_info[0]
        uso_simultaneo = int(dispositivo_info[1])
        tempo_operacao = int(dispositivo_info[2])
        dispositivos.append(Dispositivo(nome_dispositivo, uso_simultaneo, tempo_operacao))
    return dispositivos

def processar_processos(linhas, numero_dispositivos):
    processos = []
    for linha in linhas[numero_dispositivos + 1:]:
        campos = linha.strip().split('|')
        nome_processo = campos[0]
        tempo_execucao = int(campos[2])
        chance_requisitar_ES = int(campos[-1])
        processos.append(Processo(nome_processo, tempo_execucao, chance_requisitar_ES))
    return processos

def gerar_informacao_aleatoria(processo, dispositivos, unidade_tempo_atual):
    chance = random.randint(1, 100)
    if chance <= processo.chance_requisitar_ES:
        tempo = random.randint(1, 9)
        dispositivo = random.choice(dispositivos)
        processo.ponto_bloqueio = unidade_tempo_atual + tempo  
        return f"Chance | {chance} | Tempo | {tempo} | Dispositivo | {dispositivo.nome}", processo.ponto_bloqueio
    else:
        return f"Chance | {chance} (Não requisitou ES)", None

def executar_processos(processos, dispositivos):
    processos_bloqueados = []
    unidade_tempo_atual = 0
    contador_global = 0
    while processos:
        processo_em_execucao = processos.pop(0)
        informacao_aleatoria, ponto_bloqueio = gerar_informacao_aleatoria(processo_em_execucao, dispositivos, unidade_tempo_atual)
        if informacao_aleatoria:
            print(informacao_aleatoria)
            contador_global = 0 
            tempo_execucao_atual = 0 
        while processo_em_execucao.tempo_execucao > 0:
            if ponto_bloqueio is not None and unidade_tempo_atual == ponto_bloqueio:
                processos_bloqueados.append((processo_em_execucao.nome, dispositivos[2]))  
                break  
            print(f"Tempo {unidade_tempo_atual}: {processo_em_execucao.nome} | {processo_em_execucao.tempo_execucao}")
            processo_em_execucao.tempo_execucao -= 1
            unidade_tempo_atual += 1
            contador_global += 1  
            tempo_execucao_atual += 1 
            if contador_global == 10 or tempo_execucao_atual == 10:
                break
        if processo_em_execucao.tempo_execucao > 0:
            processos.append(processo_em_execucao)
        else:
            print(f"{processo_em_execucao.nome} concluído.")

def imprimir_informacoes_dispositivos(dispositivos):
    print("Informações dos Dispositivos:")
    for dispositivo in dispositivos:
        print("Nome do Dispositivo:", dispositivo.nome)
        print("Uso Simultâneo:", dispositivo.uso_simultaneo)
        print("Tempo de Operação:", dispositivo.tempo_operacao)
        print()

def main():
    nome_arquivo = 'entrada_ES.txt'
    linhas = ler_arquivo(nome_arquivo)
    dispositivos = processar_dispositivos(linhas)
    processos = processar_processos(linhas, len(dispositivos))
    executar_processos(processos, dispositivos)
    imprimir_informacoes_dispositivos(dispositivos)

if __name__ == "__main__":
    main()
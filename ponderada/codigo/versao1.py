"""A4 versão 1: buffer sem nenhuma sincronização (tem condição de corrida).

Executar: python3 versao1.py   (opcional: --rodada 2)
"""
import threading
import time
from comum import N, TOTAL, ler_rodada, relatorio

buffer = [None] * N
ocupadas = 0  # contador compartilhado, alterado pelas duas threads sem proteção
recebidas = []
produtor_terminou = False


def produtor():
    global ocupadas, produtor_terminou
    escrita = 0
    for amostra in range(TOTAL):
        while ocupadas >= N:  # espera ocupada: fica testando até ter vaga
            time.sleep(0)
        buffer[escrita] = amostra
        escrita = (escrita + 1) % N
        # Região crítica: ler, esperar e gravar o contador não é atômico.
        valor = ocupadas
        time.sleep(0)  # abre espaço para a outra thread rodar no meio
        ocupadas = valor + 1
    produtor_terminou = True


def consumidor():
    global ocupadas
    leitura = 0
    while not produtor_terminou or ocupadas > 0:
        if ocupadas <= 0:
            time.sleep(0)
            continue
        amostra = buffer[leitura]
        buffer[leitura] = None
        leitura = (leitura + 1) % N
        if amostra is not None:
            recebidas.append(amostra)
        valor = ocupadas
        time.sleep(0)
        ocupadas = valor - 1


p = threading.Thread(target=produtor, daemon=True)
c = threading.Thread(target=consumidor, daemon=True)
p.start()
c.start()
p.join(timeout=10)
c.join(timeout=10)
travou = p.is_alive() or c.is_alive()
relatorio("v1", ler_rodada(), recebidas, travou)

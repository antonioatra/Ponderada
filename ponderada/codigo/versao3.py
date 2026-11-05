"""A4 versão 3: igual à versão 2, mas o produtor pega o mutex antes de vazio.

Executar: python3 versao3.py   (opcional: --rodada 2)
"""
import threading
import time
from comum import N, TOTAL, ler_rodada, relatorio

buffer = [None] * N
vazio = threading.Semaphore(N)
cheio = threading.Semaphore(0)
mutex = threading.Semaphore(1)
recebidas = []


def produtor():
    escrita = 0
    for amostra in range(TOTAL):
        mutex.acquire()   # ordem trocada: pega o mutex primeiro...
        vazio.acquire()   # ...e, com o buffer cheio, fica preso aqui segurando o mutex
        buffer[escrita] = amostra
        escrita = (escrita + 1) % N
        mutex.release()
        cheio.release()


def consumidor():
    # Começa um pouco depois, para o produtor encher o buffer antes.
    # Assim o deadlock acontece em toda execução.
    time.sleep(0.1)
    leitura = 0
    for _ in range(TOTAL):
        cheio.acquire()
        mutex.acquire()   # nunca consegue: o produtor está com o mutex
        amostra = buffer[leitura]
        leitura = (leitura + 1) % N
        mutex.release()
        vazio.release()
        recebidas.append(amostra)


p = threading.Thread(target=produtor, daemon=True)
c = threading.Thread(target=consumidor, daemon=True)
p.start()
c.start()
p.join(timeout=1)  # se depois de 1 s ainda não terminou, travou
c.join(timeout=0.1)
travou = p.is_alive() or c.is_alive()
relatorio("v3", ler_rodada(), recebidas, travou)

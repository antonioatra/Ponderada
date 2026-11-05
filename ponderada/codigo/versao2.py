"""A4 versão 2: buffer protegido por três semáforos, na ordem correta.

Executar: python3 versao2.py   (opcional: --rodada 2)
"""
import threading
from comum import N, TOTAL, ler_rodada, relatorio

buffer = [None] * N
vazio = threading.Semaphore(N)  # vagas livres
cheio = threading.Semaphore(0)  # amostras prontas para consumir
mutex = threading.Semaphore(1)  # só uma thread mexe no buffer por vez
recebidas = []


def produtor():
    escrita = 0
    for amostra in range(TOTAL):
        vazio.acquire()   # wait(vazio): espera uma vaga
        mutex.acquire()   # wait(mutex)
        buffer[escrita] = amostra
        escrita = (escrita + 1) % N
        mutex.release()   # signal(mutex)
        cheio.release()   # signal(cheio): avisa que há amostra nova


def consumidor():
    leitura = 0
    for _ in range(TOTAL):
        cheio.acquire()   # wait(cheio): espera uma amostra
        mutex.acquire()   # wait(mutex)
        amostra = buffer[leitura]
        leitura = (leitura + 1) % N
        mutex.release()   # signal(mutex)
        vazio.release()   # signal(vazio): libera a vaga
        recebidas.append(amostra)


p = threading.Thread(target=produtor, daemon=True)
c = threading.Thread(target=consumidor, daemon=True)
p.start()
c.start()
p.join(timeout=10)
c.join(timeout=10)
travou = p.is_alive() or c.is_alive()
relatorio("v2", ler_rodada(), recebidas, travou)

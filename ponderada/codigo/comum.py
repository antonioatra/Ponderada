"""Constantes e funções usadas pelas três versões da A4."""
import sys

TOTAL = 20_000  # amostras produzidas
N = 6           # tamanho do buffer: 3 + (D2 mod 5), com D2 = 3


def ler_rodada():
    """Lê o número da rodada do comando: python3 versaoX.py --rodada 2"""
    if len(sys.argv) == 3 and sys.argv[1] == "--rodada":
        return int(sys.argv[2])
    return 1


def relatorio(versao, rodada, recebidas, travou):
    """Imprime consumidas, perdidas, duplicadas e se travou."""
    diferentes = set(recebidas)
    perdidas = TOTAL - len(diferentes)
    duplicadas = len(recebidas) - len(diferentes)
    print(f"{versao} rodada={rodada} consumidas={len(recebidas)} "
          f"perdidas={perdidas} duplicadas={duplicadas} "
          f"travou={'SIM' if travou else 'NAO'}")

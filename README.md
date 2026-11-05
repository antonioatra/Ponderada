# Ponderada CC08 

**Aluno:** Antonio Augusto Tavares Ribeiro André.

Análise de arquitetura, pipeline, sincronização e deadlock de uma pulseira sensorial; código reproduzível da questão A4.

## Requisitos

Python 3.10+; somente biblioteca padrão. Buffer com `N=6`, total `20.000` amostras.

## Execução (um comando por versão)

Na raiz do repositório:

```bash
python3 ponderada/codigo/versao1.py
python3 ponderada/codigo/versao2.py
python3 ponderada/codigo/versao3.py
```

Cada comando executa **uma** rodada; para registrar a segunda e a terceira, acrescente `--rodada 2` e `--rodada 3`, respectivamente. Os três programas imprimem consumidas, perdidas, duplicadas e indicador de travamento. `versao3.py` controla o escalonamento para reproduzir o deadlock, e sua detecção pode levar um pouco mais de um segundo. A primeira versão depende do escalonamento e os valores podem variar.

O relatório completo está em [ponderada/ponderada-tato.md](ponderada/ponderada-tato.md). Os prints (caches da máquina e execução das três versões no Terminal) estão em `ponderada/img`.

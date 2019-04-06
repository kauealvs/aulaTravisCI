import jogovelha
import sys

ErroInicializar = False

jogo = jogovelha.inicializar()

if len(jogo) != 3:
    ErroInicializar = True
else:
    for linha in jogo:
        if len(linha) != 3:
            ErroInicializar = True
        else:
            for elemento in linha:
                if elemento != '.':
                    ErroInicializar = True
if ErroInicializar:
    sys.exit(1)
else:
    sys.exit(0)

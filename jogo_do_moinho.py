# Goncalo Botelho Mateus, 99225

# TAD posicao
def cria_posicao(c,l):
    #verificar a len
    if not isinstance(c, str) or c not in ("a", "b", "c") or not isinstance(l, str) or l not in ("1", "2", "3"):
        raise ValueError("cria_posicao: argumentos invalidos")
    return [c, l]

def eh_posicao(arg):
    return isinstance(arg, list) and arg[0] in ("a", "b", "c") and arg[1] in ("1", "2", "3") and len(arg) == 2

def cria_copia_posicao(p):
    #ESTÁ MAL
    if not eh_posicao(p):
        raise ValueError("cria_copia_posicao: argumento invalido")
    return [str(p[0]), str(p[1])]

def obter_pos_c(p):
    return p[0]

def obter_pos_l(p):
    return p[1]

def posicoes_iguais(p1, p2):
    return eh_posicao(p1) and eh_posicao(p2) and p1 == p2

def posicao_para_str(p):
    return obter_pos_c(p) + obter_pos_l(p)

#incompleta
def obter_posicoes_adjacentes(p):
    pos_adj = ()
    c = obter_pos_c(p)
    l = int(obter_pos_l(p))
    if l == 1 or l == 2:
        pos = cria_posicao(c, str(l + 1))
        if eh_posicao(pos):
            pos_adj += (posicao_para_str(pos), )
    if l == 2 or l == 3:
        pos1 = cria_posicao(c, str(l - 1))
        if eh_posicao(pos1):
            pos_adj += (posicao_para_str(pos1), )

#TAD peca
def cria_peca(s):
    if not isinstance(s, str) or s not in ("X", "O", " "):
        raise ValueError("cria_peca: argumento invalido")
    return [s]

def eh_peca(arg):
    return isinstance(arg, list) and arg[0] in ("X", "O", " ") and len(arg) == 1

def cria_copia_peca(j):
        #ESTÁ MAL
    if not eh_peca(j):
        raise ValueError("cria_copia_posicao: argumento invalido")
    return [str(j[0])]

def pecas_iguais(j1, j2):
    return eh_peca(j1) and eh_peca(j2) and j1 == j2

def peca_para_str(j):
    return "[" + j[0] + "]"
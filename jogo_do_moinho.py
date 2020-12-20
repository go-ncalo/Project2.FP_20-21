def cria_posicao(c,l):
    if not isinstance(c, str) or c not in ("a", "b", "c") or not isinstance(l, str) or l not in ("1", "2", "3"):
        raise ValueError("cria_posicao: argumentos invalidos")
    return [c, l]

def cria_copia_posicao(p):
    if not isinstance(p, list) or p[0] not in ("a", "b", "c") or p[1] not in ("1", "2", "3"):
        raise ValueError("cria_copia_posicao: argumento invalido")
    return p

def obter_pos_c(p):
    return p[0]

def obter_pos_l(p):
    return p[1]

def eh_posicao(arg):
    return isinstance(arg, list) and arg[0] in ("a", "b", "c") and arg[1] in ("1", "2", "3")

def posicoes_iguais(p1, p2):
    return p1[0] == p2[0] and p1[1] == p2[1]

def posicao_para_str(p):
    return p[0] + p[1]

def obter_posicoes_adjacentes(p)
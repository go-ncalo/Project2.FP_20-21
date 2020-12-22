# Goncalo Botelho Mateus, 99225

# TAD posicao
def cria_posicao(c, l):
    # verificar a len
    if not isinstance(c, str) or c not in ("a", "b", "c") or not isinstance(l, str) or l not in ("1", "2", "3"):
        raise ValueError("cria_posicao: argumentos invalidos")
    return [c, l]


def eh_posicao(arg):
    return isinstance(arg, list) and arg[0] in ("a", "b", "c") and arg[1] in ("1", "2", "3") and len(arg) == 2


def cria_copia_posicao(p):
    # ESTÁ MAL
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


# incompleta
def obter_posicoes_adjacentes(p):
    pos_adj = ()
    c = obter_pos_c(p)
    l = int(obter_pos_l(p))
    if l == 1 or l == 2:
        pos = cria_posicao(c, str(l + 1))
        if eh_posicao(pos):
            pos_adj += (posicao_para_str(pos),)
    if l == 2 or l == 3:
        pos1 = cria_posicao(c, str(l - 1))
        if eh_posicao(pos1):
            pos_adj += (posicao_para_str(pos1),)


# TAD peca
def cria_peca(s):
    if not isinstance(s, str) or s not in ("X", "O", " "):
        raise ValueError("cria_peca: argumento invalido")
    return [s]


def eh_peca(arg):
    return isinstance(arg, list) and arg[0] in ("X", "O", " ") and len(arg) == 1


def cria_copia_peca(j):
    # ESTÁ MAL
    if not eh_peca(j):
        raise ValueError("cria_copia_posicao: argumento invalido")
    return [str(j[0])]


def pecas_iguais(j1, j2):
    return eh_peca(j1) and eh_peca(j2) and j1 == j2


def peca_para_str(j):
    return "[" + str(j[0]) + "]"


def peca_para_inteiro(j):
    if peca_para_str(j) == "[X]":
        return 1
    elif peca_para_str(j) == "[O]":
        return -1
    else:
        return 0

def inteiro_para_peca(int):
    if int == -1:
        j = cria_peca("O")
    elif int == 0:
        j = cria_peca(" ")
    else:
        j = cria_peca("X")
    return j

# TAD tabuleiro
def cria_tabuleiro():
    return {"a": [[" "], [" "], [" "]], "b": [[" "], [" "], [" "]], "c": [[" "], [" "], [" "]]}


def cria_copia_tabuleiro():
    return "hello"


def obter_peca(t, p):
    c = obter_pos_c(p)
    l = int(obter_pos_l(p))

    return t[c][l - 1]


def obter_vetor(t, s): # ESTÁ MAL
    vetor = ()
    if s in ["1", "2", "3"]:
        for i in ["a", "b", "c"]:
            vetor += (t[i][int(s) - 1], )
    elif s in ["a", "b", "c"]:
            vetor += (t[s], )
    
    return vetor

def coloca_peca(t, j, p):
    c = obter_pos_c(p)
    l = int(obter_pos_l(p))
    t[c][l - 1] = j

    return t

# FUNCAO AUXILIAR ?

def remove_peca(t, p):
    c = obter_pos_c(p)
    l = int(obter_pos_l(p))
    t[c][l - 1] = [" "]

    return t


def move_peca(t, p1, p2):
    c1 = obter_pos_c(p1)
    l1 = int(obter_pos_l(p1))
    c2 = obter_pos_c(p2)
    l2 = int(obter_pos_l(p2))

    t[c2][l2 - 1] = t[c1][l1 - 1]
    t[c1][l1 - 1] = [" "]
    return t


def eh_tabuleiro(arg):
    return "hello world"


def eh_posicao_livre(t, p):
    c = obter_pos_c(p)
    l = int(obter_pos_l(p))

    return t[c][l - 1] == [" "]


def tabuleiros_iguais(t1, t2):
    return "hello world"


def tabuleiro_para_str(t):
    list = []
    for i in ("a", "b", "c"):
        for j in range(0, 3):
            if peca_para_inteiro(t[i][j]) == -1:
                list.append("[O]")
            if peca_para_inteiro(t[i][j]) == 0:
                list.append("[ ]")
            if peca_para_inteiro(t[i][j]) == 1:
                list.append("[X]")
    return \
        "   a   b   c" + "\n\
1 " + list[0] + "-" + list[3] + "-" + list[6] + "\n\
   | \ | / |\n\
2 " + list[1] + "-" + list[4] + "-" + list[7] + "\n\
   | / | \ |\n\
3 " + list[2] + "-" + list[5] + "-" + list[8]

def tuplo_para_tabuleiro(t):
    tab = cria_tabuleiro()
    for i in range(0, 3):
        tab["a"][i] = inteiro_para_peca(t[i][0])
        tab["b"][i] = inteiro_para_peca(t[i][1])
        tab["c"][i] = inteiro_para_peca(t[i][2])
    
    return tab

t = tuplo_para_tabuleiro(((0,1,-1),(-0,1,-1),(1,0,-1)))
print(tabuleiro_para_str(t))
# Goncalo Botelho Mateus, 99225

# TAD posicao
# fazer comentario com todos as operacoes basicas
# Representacao interna: ['coluna', 'linha']
def cria_posicao(c, l):
    if not isinstance(c, str) or c not in ("a", "b", "c") or not isinstance(l, str) or l not in ("1", "2", "3"):
        raise ValueError("cria_posicao: argumentos invalidos")
    return [c, l]

def eh_posicao(arg):
    return isinstance(arg, list) and arg[0] in ("a", "b", "c") and arg[1] in ("1", "2", "3") and len(arg) == 2

def cria_copia_posicao(p):
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

def obter_posicoes_adjacentes(p):
    c = obter_pos_c(p)
    l = obter_pos_l(p)
    if l == "1":
        if c == "a":
            pos_adj = (cria_posicao("b", "1"), cria_posicao("a", "2"), cria_posicao("b", "2"))
        if c == "b":
            pos_adj = (cria_posicao("a", "1"), cria_posicao("c", "1"), cria_posicao("b", "2"))
        if c == "c":
            pos_adj = (cria_posicao("b", "1"), cria_posicao("b", "2"), cria_posicao("c", "2"))
    if l == "2":
        if c == "a":
            pos_adj = (cria_posicao("a", "1"), cria_posicao("b", "2"), cria_posicao("a", "3"))
        if c == "b":
            pos_adj = (cria_posicao("a", "1"), cria_posicao("b", "1"), cria_posicao("c", "1"),
                    cria_posicao("a", "2"), cria_posicao("c", "2"),
                    cria_posicao("a", "3"), cria_posicao("b", "3"), cria_posicao("c", "3"))
        if c == "c":
            pos_adj = (cria_posicao("c", "1"), cria_posicao("b", "2"), cria_posicao("c", "3"))
    if l == "3":
        if c == "a":
            pos_adj = (cria_posicao("a", "2"), cria_posicao("b", "2"), cria_posicao("b", "3"))
        if c == "b":
            pos_adj = (cria_posicao("b", "2"), cria_posicao("a", "3"), cria_posicao("c", "3"))
        if c == "c":
            pos_adj = (cria_posicao("b", "2"), cria_posicao("c", "2"), cria_posicao("b", "3"))

    return pos_adj

# TAD peca
# fazer comentario com todos as opercaoes basicas
# Representacao interna: ['peca']
def cria_peca(s):
    if not isinstance(s, str) or s not in ("X", "O", " "):
        raise ValueError("cria_peca: argumento invalido")
    return [s]

def eh_peca(arg):
    return isinstance(arg, list) and arg[0] in ("X", "O", " ") and len(arg) == 1

def cria_copia_peca(j):
    if not eh_peca(j):
        raise ValueError("cria_copia_posicao: argumento invalido")
    return [str(j[0])]

def pecas_iguais(j1, j2):
    return eh_peca(j1) and eh_peca(j2) and j1 == j2

def peca_para_str(j):
    return "[" + str(j[0]) + "]"

def peca_para_inteiro(j):
    if pecas_iguais(j, cria_peca("X")):
        return 1
    elif pecas_iguais(j, cria_peca("O")):
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
# fazer comentario com todos as operacoes basicas
# Representacao interna: {"a": [peca, peca, peca], "b": [peca, peca, peca], "c": [peca, peca, peca]}
def cria_tabuleiro():
    tab = {}
    for i in ("a", "b", "c"):
        tab[i] = [cria_peca(" "), cria_peca(" "), cria_peca(" ")]
    return tab

def cria_copia_tabuleiro(t):
    return dict(t)

def obter_peca(t, p):
    c = obter_pos_c(p)
    l = int(obter_pos_l(p))

    return t[c][l - 1]

def obter_vetor(t, s):
    vetor = ()
    if s in ["1", "2", "3"]:
        for i in ["a", "b", "c"]:
            vetor += (t[i][int(s) - 1], )
    elif s in ["a", "b", "c"]:
            vetor = tuple(t[s])
    
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
    t[c][l - 1] = cria_peca(" ")

    return t

def move_peca(t, p1, p2):
    c1 = obter_pos_c(p1)
    l1 = int(obter_pos_l(p1))
    c2 = obter_pos_c(p2)
    l2 = int(obter_pos_l(p2))
    
    if posicoes_iguais(p1, p2):
        return t
    else:
        t[c2][l2 - 1] = t[c1][l1 - 1]
        t[c1][l1 - 1] = cria_peca(" ")
        return t

def eh_tabuleiro(arg):
    vencedor_x = [['X'], ['X'], ['X']]
    vencedor_o = [['O'], ['O'], ['O']]
    vazio = [[' '], [' '], [' ']]

    cont_x = 0
    cont_o = 0
    if isinstance(arg, dict) and len(arg) == 3:
        for i in ("a", "b", "c"):
            for j in range(3):
                if pecas_iguais(arg[i][j], cria_peca("X")):
                    cont_x += 1
                elif pecas_iguais(arg[i][j], cria_peca("O")):
                    cont_o += 1

        dif = abs(cont_x - cont_o)

        if 0 <= cont_x <= 3 and 0 <= cont_o <= 3:
            if dif == 1 or dif == 0:
                for k in ("a", "b", "c"):
                    if arg[k] == vazio:
                        return True
                    elif arg[k] != vencedor_x or arg[k] != vencedor_o:
                        if arg["a"] != arg["b"] != arg["c"]:
                            for l in ("1", "2", "3"):
                                if obter_vetor(arg, l) == vazio:
                                    return True
                                elif obter_vetor(arg, l) != vencedor_x or obter_vetor(arg, l) != vencedor_o:
                                    if obter_vetor(arg, "1") != obter_vetor(arg, "2") != obter_vetor(arg, "3"):
                                        return True
                                    else:
                                        return False  
                                else:
                                    return False  
                        else:
                            return False  
                    else:
                        return False
            else:
                return False
        else:
            return False
    else:
        return False

def eh_posicao_livre(t, p):
    c = obter_pos_c(p)
    l = int(obter_pos_l(p))

    return t[c][l - 1] == cria_peca(" ")

def tabuleiros_iguais(t1, t2):
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and t1 == t2

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

    return "   a   b   c\n"\
    "1 " + list[0] + "-" + list[3] + "-" + list[6] + "\n   | \ | / |\n"\
    "2 " + list[1] + "-" + list[4] + "-" + list[7] + "\n   | / | \ |\n"\
    "3 " + list[2] + "-" + list[5] + "-" + list[8]

def tuplo_para_tabuleiro(t):
    tab = cria_tabuleiro()
    for i in range(0, 3):
        tab["a"][i] = inteiro_para_peca(t[i][0])
        tab["b"][i] = inteiro_para_peca(t[i][1])
        tab["c"][i] = inteiro_para_peca(t[i][2])
    
    return tab

def in_pos(j, pos):
    tup = ()
    for i in pos:
        tup += (posicoes_iguais(i, j), )
    if True in tup:
        return True
    else:
        return False

def vetores_iguais(v1, v2):
    tup = ()
    for i in range(3):
        tup += (pecas_iguais(v1[i], v2[i]), )
    return tup == (True, True, True)

def obter_ganhador(t):
    vencedor_x = ()
    vencedor_o = ()
    for i in range(3):
        vencedor_x += (cria_peca("X"), )
        vencedor_o += (cria_peca("O"), )

    for j in ("a", "b", "c", "1", "2", "3"):
        if vetores_iguais(obter_vetor(t, j), vencedor_x):
            return cria_peca("X")
        elif vetores_iguais(obter_vetor(t, j), vencedor_o):
            return cria_peca("O")

    return cria_peca(" ")

def obter_posicoes_livres(t):
    pos_livres = ()
    for i in ("1", "2", "3"):
        for j in ("a", "b", "c"):
            pos = cria_posicao(j, i)
            if pecas_iguais(obter_peca(t, pos), cria_peca(" ")):
                pos_livres += (pos, )
    
    return pos_livres

def obter_posicoes_jogador(t, j):
    pos_jogador = ()
    for i in ("1", "2", "3"):
        for k in ("a", "b", "c"):
            pos = cria_posicao(k, i)
            if pecas_iguais(obter_peca(t, pos), j):
                pos_jogador += (pos, )
    
    return pos_jogador

def fase_movimento(t):
    cont_x = 0
    cont_o = 0
    for i in ("1", "2", "3"):
        for k in ("a", "b", "c"):
            pos = cria_posicao(k, i)
            if pecas_iguais(obter_peca(t, pos), cria_peca("X")):
                cont_x += 1
            elif pecas_iguais(obter_peca(t,pos), cria_peca("O")):
                cont_o += 1
    return cont_x == 3 and cont_o == 3

def obter_movimento_manual(t, j):
    pos_liv = obter_posicoes_livres(t)
    if fase_movimento(3):
        mov = input("Turno do jogador. Escolha um movimento: ")
        orig = cria_posicao(mov[0], mov[1])
        dest = cria_posicao(mov[2], mov[3])
        pos_adj = obter_posicoes_adjacentes(orig)
        if not posicoes_iguais(orig, dest):
            if not in_pos(dest, pos_adj) or not in_pos(dest, pos_liv) or not pecas_iguais(obter_peca(t, orig), j):
                raise ValueError("obter_movimento_manual: escolha invalida")
            else:
                return (orig, dest)
        else:
            return (orig, dest)
    else:
        pos = input("Turno do jogador. Escolha uma posicao: ")
        posicao = cria_posicao(pos[0], pos[1])
        if not in_pos(posicao, pos_liv):
            raise ValueError("obter_movimento_manual: escolha invalida")
        else:
            return (posicao, )

def pos_vazia(t, j, tup):
    ganhador1 = (cria_peca(" "), j, j)
    ganhador2 = (j, cria_peca(" "), j)
    ganhador3 = (j, j, cria_peca(" "))

    for i in tup:
        vet = obter_vetor(t, i)
        if vetores_iguais(vet, ganhador1) or\
           vetores_iguais(vet, ganhador2) or\
           vetores_iguais(vet, ganhador3):
           vazio = vet.index(cria_peca(" "))
           return (i, vazio)


def vitoria(t, j):
    vazio = pos_vazia(t, j, ("a", "b", "c"))
    if vazio:
        return (cria_posicao(vazio[0], str(vazio[1] + 1)))

    vazio1 = pos_vazia(t, j, ("1", "2", "3"))
    
    if vazio1[1] == 0:
        ch = "a"
    elif vazio1[1] == 1:
        ch = "b"
    elif vazio1[1] == 2:
        ch = "c"
    return(cria_posicao(ch, vazio1[0]))

def bloqueio(t, j):
    j = inteiro_para_peca(-peca_para_inteiro(j))
    return vitoria(t, j)

def centro(t):
    pos_livre = obter_posicoes_livres(t)
    if in_pos(cria_posicao("b", "2"), pos_livre):
        return (cria_posicao("b", "2"), )

def canto_vazio(t):
    pos_livre = obter_posicoes_livres(t)
    for i in ("1", "3"):
        for j in ("a", "c"):
            if in_pos(cria_posicao(j, i), pos_livre):
                return (cria_posicao(j, i), )

def lateral_vazio(t):
    pos_livre = obter_posicoes_livres(t)
    if in_pos(cria_posicao("b", "1"), pos_livre):
        return (cria_posicao("b", "1"), )
    for i in ("a", "c"):
        if in_pos(cria_posicao(i, "2"), pos_livre):
            return cria_posicao(i, "2")
    if in_pos(cria_posicao("b", "3"), pos_livre):
        return (cria_posicao("b", "3"), )

def minimax(t, j, prof, seq = ()):
    if peca_para_inteiro(obter_ganhador(t)) != 0 or prof == 0:
        return (peca_para_inteiro(obter_ganhador(t)), seq)
    else:
        melhor_resultado = -peca_para_inteiro(j)
        pos = obter_posicoes_jogador(t, j)
        for i in pos:
            adj = obter_posicoes_adjacentes(i)
            for k in adj:
                if eh_posicao_livre(t, k):
                    (novo_resultado, nova_seq_movimentos) = minimax(move_peca(cria_copia_tabuleiro(t), i, k), inteiro_para_peca(-peca_para_inteiro(j)), prof - 1, seq + (i, k))
                    if ("melhor_seq_movimentos" not in locals()) or (pecas_iguais(j, cria_peca("X")) and novo_resultado > melhor_resultado) or\
                            (pecas_iguais(j, cria_peca("O")) and novo_resultado < melhor_resultado):
                        melhor_resultado = novo_resultado
                        melhor_seq_movimentos = nova_seq_movimentos
        return melhor_resultado, melhor_seq_movimentos

def obter_movimento_auto(t, j, str):
    if not fase_movimento(t):



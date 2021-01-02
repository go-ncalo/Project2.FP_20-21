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
    return isinstance(arg, list) and len(arg) == 1 and arg[0] in ("X", "O", " ")

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
    return t.copy()

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
                if arg == cria_tabuleiro():
                    return True
                else:
                    for k in ("a", "b", "c"):
                        if arg[k] != vencedor_x or arg[k] != vencedor_o:
                            if arg["a"] != arg["b"] or arg["a"] != arg["c"]:
                                for l in ("1", "2", "3"):
                                    if obter_vetor(arg, l) != vencedor_x or obter_vetor(arg, l) != vencedor_o:
                                        if obter_vetor(arg, "1") != obter_vetor(arg, "2") or obter_vetor(arg, "1") != obter_vetor(arg, "3"):
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

def eh_posicao_livre(t, p):
    c = obter_pos_c(p)
    l = int(obter_pos_l(p))

    return t[c][l - 1] == cria_peca(" ")

def vetores_iguais(v1, v2):
    tup = ()
    for i in range(3):
        tup += (pecas_iguais(v1[i], v2[i]), )
    return tup == (True, True, True)

def tabuleiros_iguais(t1, t2): # ESTA MAL
    if eh_tabuleiro(t1) and eh_tabuleiro(t2):
        veta1 = obter_vetor(t1, "a")
        vetb1 = obter_vetor(t1, "b")
        vetc1 = obter_vetor(t1, "c")
        veta2 = obter_vetor(t2, "a")
        vetb2 = obter_vetor(t2, "b")
        vetc2 = obter_vetor(t2, "c")
        return vetores_iguais(veta1, veta2) and vetores_iguais(vetb1, vetb2) and vetores_iguais(vetc1, vetc2)
    else:
        return False

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
    if fase_movimento(t):
        mov = input("Turno do jogador. Escolha um movimento: ")
        if isinstance(mov, str) and len(mov) == 4 and mov[0] and mov[2] in ("a", "b", "c") and mov[1] and mov[3] in ("1", "2", "3"):
            orig = cria_posicao(mov[0], mov[1])
            dest = cria_posicao(mov[2], mov[3])
            pos_adj = obter_posicoes_adjacentes(orig)

            if not posicoes_iguais(orig, dest):
                if not in_pos(dest, pos_adj) or not in_pos(dest, pos_liv) or not pecas_iguais(obter_peca(t, orig), j):
                    raise ValueError("obter_movimento_manual: escolha invalida")
                else:
                    return (orig, dest)
            else:
                for i in pos_adj:
                    if in_pos(i, pos_liv):
                        raise ValueError("obter_movimento_manual: escolha invalida")
            return (orig, dest)
        else:
            raise ValueError("obter_movimento_manual: escolha invalida")
    else:
        pos = input("Turno do jogador. Escolha uma posicao: ")
        if isinstance(pos, str) and len(pos) == 2 and pos[0] in ("a", "b", "c") and pos[1] in ("1", "2", "3"):
            posicao = cria_posicao(pos[0], pos[1])
            if not in_pos(posicao, pos_liv):
                raise ValueError("obter_movimento_manual: escolha invalida")
            else:
                return (posicao, )
        else:
            raise ValueError("obter_movimento_manual: escolha invalida")

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
        return (cria_posicao(vazio[0], str(vazio[1] + 1)), )

    vazio1 = pos_vazia(t, j, ("1", "2", "3"))
    if vazio1:
        if vazio1[1] == 0:
            ch = "a"
        elif vazio1[1] == 1:
            ch = "b"
        elif vazio1[1] == 2:
            ch = "c"
        return(cria_posicao(ch, vazio1[0]), )

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

def movimento_auto_coloc(t, j):
    if vitoria(t, j):
        return vitoria(t, j)
    elif bloqueio(t, j):
        return bloqueio(t, j)
    elif centro(t):
        return centro(t)
    elif canto_vazio(t):
        return canto_vazio(t)
    elif lateral_vazio(t):
        return lateral_vazio(t)

def obter_movimento_auto(t, j, str):
    if not fase_movimento(t):
        return movimento_auto_coloc(t, j)
    else:
        if str == "facil":
            pos_jog = obter_posicoes_jogador(t, j)
            pos_livres = obter_posicoes_livres(t)
            for i in pos_jog:
                pos_adj = obter_posicoes_adjacentes(i)
                for j in pos_adj:
                    if in_pos(j, pos_livres):
                        return (i, j)
        elif str == "normal":
            return minimax(t, j, 1)[1]
        elif str == "dificil":
            return minimax(t, j, 5)[1]

def moinho_jog(jog, st):
    t = cria_tabuleiro()
    i = 3
    j = cria_peca("X")
    while i != 0:
        pos = obter_movimento_manual(t, j)
        t = coloca_peca(t, j, pos[0])
        print(tabuleiro_para_str(t))
        poscomp = obter_movimento_auto(t, cria_peca("O"), st)
        t = coloca_peca(t, cria_peca("O"), poscomp[0])
        print("Turno do computador (" + st + "):")
        print(tabuleiro_para_str(t))
        i -= 1
    if not pecas_iguais(obter_ganhador(t), cria_peca(" ")):
        return obter_ganhador(t)
    else:
        while pecas_iguais(obter_ganhador(t), cria_peca(" ")):
            mov = obter_movimento_manual(t, j)
            t = move_peca(t, mov[0], mov[1])
            print(tabuleiro_para_str(t))
            if not pecas_iguais(obter_ganhador(t), cria_peca(" ")):
                return peca_para_str(obter_ganhador(t))
            movcomp = obter_movimento_auto(t, cria_peca("O"), st)
            t = move_peca(t, movcomp[0], movcomp[1])
            print("Turno do computador (" + st + "):")
            print(tabuleiro_para_str(t))
        return peca_para_str(obter_ganhador(t))

def moinho_comp(jog, st):
    t = cria_tabuleiro()
    i = 3
    j = cria_peca("O")
    while i != 0:
        poscomp = obter_movimento_auto(t, cria_peca("X"), st)
        t = coloca_peca(t, cria_peca("X"), poscomp[0])
        print("Turno do computador (" + st + "):")
        print(tabuleiro_para_str(t))
        pos = obter_movimento_manual(t, j)
        t = coloca_peca(t, j, pos[0])
        print(tabuleiro_para_str(t))
        i -= 1
    if not pecas_iguais(obter_ganhador(t), cria_peca(" ")):
        return obter_ganhador(t)
    else:
        while pecas_iguais(obter_ganhador(t), cria_peca(" ")):
            movcomp = obter_movimento_auto(t, cria_peca("X"), st)
            t = move_peca(t, movcomp[0], movcomp[1])
            print("Turno do computador (" + st + "):")
            print(tabuleiro_para_str(t))
            if not pecas_iguais(obter_ganhador(t), cria_peca(" ")):
                return peca_para_str(obter_ganhador(t))
            mov = obter_movimento_manual(t, j)
            t = move_peca(t, mov[0], mov[1])
            print(tabuleiro_para_str(t))
        return peca_para_str(obter_ganhador(t))

def moinho(jog, st):
    if not isinstance(jog, str) and (jog == "[X]" or jog == "[O]") or\
    not isinstance(st, str) and (st == "facil" or st == "normal" or st == "dificil"):
        raise ValueError("moinho: argumentos invalidos")
    print("Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade " + st + ".")
    t = cria_tabuleiro()
    print(tabuleiro_para_str(t))
    if jog == "[X]":
        return moinho_jog(jog, st)
    else:
        return moinho_comp(jog, st)
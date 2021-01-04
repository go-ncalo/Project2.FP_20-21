# Goncalo Botelho Mateus, 99225

# TAD posicao

# Representacao interna: ['coluna', 'linha']
# cria_posicao: str x str -> posicao
# cria_copia_posicao: posicao -> posicao
# obter_pos_c: posicao -> str
# obter_pos_l: posicao -> str
# eh_posicao: universal -> booelano
# posicoes_iguais: posicao x posicao -> booleano
# posicao_para_str: posicao -> str
# obter_posicoes_adjacentes: posicao -> tuplo de posicoes

def cria_posicao(c, l):
    # cria_posicao: str x str -> posicao
    """
    A funcao recebe duas cadeias de caracteres correspondentes a coluna c e a
    linha l de uma posicao e devolve a respetiva posicao.
    Se um dos argumentos for invalido gera um erro.
    """
    if (not isinstance(c, str) or c not in ("a", "b", "c")
       or not isinstance(l, str) or l not in ("1", "2", "3")):
        raise ValueError("cria_posicao: argumentos invalidos")
    return [c, l]

def eh_posicao(arg):
    # eh_posicao: universal -> booelano
    """
    A funcao recebe um argumento de qualquer tipo e devolve True se for um
    TAD posicao e False caso contrario, sem nunca gerar erros.
    """
    return (isinstance(arg, list) and len(arg) == 2 and arg[0] in
           ("a", "b", "c") and arg[1] in ("1", "2", "3"))

def cria_copia_posicao(p):
    # cria_copia_posicao: posicao -> posicao
    """
    A funcao recebe uma posicao e devolve uma copia nova da posicao.
    """
    if not eh_posicao(p):
        raise ValueError("cria_copia_posicao: argumento invalido")
    return [p[0], p[1]]

def obter_pos_c(p):
    # obter_pos_c: posicao -> str
    """
    A funcao recebe uma posicao e devolve a componente coluna dessa posicao.
    """
    return p[0]

def obter_pos_l(p):
    # obter_pos_l: posicao -> str
    """
    A funcao recebe uma posicao e devolve a componente linha dessa posicao.
    """
    return p[1]

def posicoes_iguais(p1, p2):
    # posicoes_iguais: posicao x posicao -> booleano
    """
    A funcao recebe duas posicoes e devolve True apenas se p1 e p2 sao posicoes
    e sao iguais.
    """
    return eh_posicao(p1) and eh_posicao(p2) and p1 == p2

def posicao_para_str(p):
    # posicao_para_str: posicao -> str
    """
    A funcao recebe uma posicao e devolve a cadeia de carateres "cl" que
    representa o seu argumento.
    """
    return obter_pos_c(p) + obter_pos_l(p)

def obter_posicoes_adjacentes(p):
    # obter_posicoes_adjacentes: posicao -> tuplo de posicoes
    """
    A funcao recebe uma posicao e devolve um tuplo com as posicoes adjacentes a
    posicao p de acordo com a ordem de leitura do tabuleiro.
    """
    c = obter_pos_c(p)
    l = obter_pos_l(p)
    if l == "1":
        if c == "a":
            return (cria_posicao("b", "1"), cria_posicao("a", "2"),
                       cria_posicao("b", "2"))
        elif c == "b":
            return (cria_posicao("a", "1"), cria_posicao("c", "1"),
                       cria_posicao("b", "2"))
        elif c == "c":
            return (cria_posicao("b", "1"), cria_posicao("b", "2"),
                       cria_posicao("c", "2"))
    elif l == "2":
        if c == "a":
            return (cria_posicao("a", "1"), cria_posicao("b", "2"),
                       cria_posicao("a", "3"))
        elif c == "b":
            return (cria_posicao("a", "1"), cria_posicao("b", "1"),
                       cria_posicao("c", "1"), cria_posicao("a", "2"),
                       cria_posicao("c", "2"), cria_posicao("a", "3"),
                       cria_posicao("b", "3"), cria_posicao("c", "3"))
        elif c == "c":
            return (cria_posicao("c", "1"), cria_posicao("b", "2"),
                       cria_posicao("c", "3"))
    elif l == "3":
        if c == "a":
            return (cria_posicao("a", "2"), cria_posicao("b", "2"),
                       cria_posicao("b", "3"))
        elif c == "b":
            return (cria_posicao("b", "2"), cria_posicao("a", "3"),
                       cria_posicao("c", "3"))
        elif c == "c":
            return (cria_posicao("b", "2"), cria_posicao("c", "2"),
                       cria_posicao("b", "3"))


# TAD peca

# Representacao interna: ['peca']
# cria_peca: str -> peca
# cria_copia_peca: peca -> peca
# eh_peca: universal -> booelano
# pecas_iguais: peca x peca -> booleano
# peca_para_str: peca -> str
# peca_para_inteiro: peca -> inteiro

def cria_peca(s):
    # cria_peca: str -> peca
    """
    A funcao recebe uma cadeias de caracteres correspondentes ao identificador
    de um dos jogadores ("X" ou "O") ou a uma peca livre (" ") e devolve a
    respetiva peca.
    Se o argumento for invalido gera um erro.
    """
    if not isinstance(s, str) or not s in ("X", "O", " "):
        raise ValueError("cria_peca: argumento invalido")
    return [s]

def eh_peca(arg):
    # eh_peca: universal -> booelano
    """
    A funcao recebe um argumento de qualquer tipo e devolve True se for um
    TAD peca e False caso contrario, sem nunca gerar erros.
    """
    return (isinstance(arg, list) and len(arg) == 1 and
        arg in (["X"], ["O"], [" "]))

def cria_copia_peca(j):
    # cria_copia_peca: peca -> peca
    """
    A funcao recebe uma peca e devolve uma copia nova da peca.
    """
    if not eh_peca(j):
        raise ValueError("cria_copia_posicao: argumento invalido")
    return [j[0]]

def pecas_iguais(j1, j2):
    # pecas_iguais: peca x peca -> booleano
    """
    A funcao recebe duas pecas e devolve True apenas se j1 e j2 sao pecas e sao
    iguais.
    """
    return eh_peca(j1) and eh_peca(j2) and j1 == j2

def peca_para_str(j):
    # peca_para_str: peca -> str
    """
    A funcao recebe uma peca e devolve a cadeia de carateres que representa o
    seu jogador dono da peca("[X]", "[O]" ou "[ ]").
    """
    return "[" + str(j[0]) + "]"

def peca_para_inteiro(j):
    # peca_para_inteiro: peca -> inteiro
    """
    A funcao recebe uma peca e devolve um inteiro 1, -1 ou 0 dependedo de que
    jogador e a peca (1: 'X', -1: 'O', 0: livre)
    """
    if pecas_iguais(j, cria_peca("X")):
        return 1
    elif pecas_iguais(j, cria_peca("O")):
        return -1
    elif pecas_iguais(j, cria_peca(" ")):
        return 0

def inteiro_para_peca(int):
    # inteiro_para_peca: peca -> inteiro
    """
    A funcao recebe um inteiro e devolve uma peca dependedo de que jogador
    representa o inteiro (1: 'X', -1: 'O', 0: livre)
    """
    if int == -1:
        return cria_peca("O")
    elif int == 0:
        return cria_peca(" ")
    elif int == 1:
        return cria_peca("X")

# TAD tabuleiro

# Representacao interna: 
#   {"a": [peca, peca, peca], "b": [peca, peca, peca], "c": [peca, peca, peca]}
# cria_tabuleiro: {} -> tabuleiro
# cria_copia_tabuleiro: tabuleiro -> tabuleiro
# obter_peca: tabuleiro x posicao -> peca
# obter_vetor: tabuleiro x str -> tuplo de pecas
# coloca_peca: tabuleiro x peca x posicao -> tabuleiro
# remove_peca: tabuleiro x posicao -> tabuleiro
# move_peca: tabuleiro x posicao x posicao -> tabuleiro
# eh_tabuleiro: universal -> booelano
# eh_posicao_livre: tabuleiro x posicao -> booleano
# tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
# tabuleiro_para_str: tabuleiro -> str
# tuplo_para_tabuleiro: tuplo -> tabuleiro
# obter_ganhador: tabuleiro -> peca
# obter_posicoes_livres: tabuleiro -> tuplo de posicoes
# obter_posicoes_jogador: tabuleiro x peca -> tuplo de posicoes

def cria_tabuleiro():
    # cria_tabuleiro: {} -> tabuleiro
    """
    A funcao nao recebe argumentos e devolve um tabuleiro de jogo de 3x3 sem
    posicoes ocupadas por pecas.
    """
    tab = {}
    for i in ("a", "b", "c"):
        tab[i] = [cria_peca(" "), cria_peca(" "), cria_peca(" ")]
    return tab

def cria_copia_tabuleiro(t):
    # cria_copia_tabuleiro: tabuleiro -> tabuleiro
    """
    A funcao recebe um tabuleiro e devolve uma copia nova do tabuleiro.
    """
    # esta funcao efetua uma deepcopy do tabuleiro t
    dict = {"a": [], "b": [], "c": []}
    for i in ("a", "b", "c"):
        for j in range(3):
            dict[i] += [t[i][j]]

    return dict

def obter_peca(t, p):
    # obter_peca: tabuleiro x posicao -> peca
    """
    A funcao recebe um tabuleiro e uma posicao e devolve a peca que se encontra
    na posicao p do tabuleiro. Se nao estiver ocupada, devolve uma peca livre.
    """
    col = obter_pos_c(p)
    lin = int(obter_pos_l(p)) - 1

    return t[col][lin]

def obter_vetor(t, s):
    # obter_vetor: tabuleiro x str -> tuplo de pecas
    """
    A funcao recebe um tabuleiro e uma string que representa uma linha ou coluna
    do tabuleiro e devolve todas as pecas daquela linha ou coluna.
    """
    vetor = ()
    if s in ["1", "2", "3"]:
        for i in ["a", "b", "c"]:
            vetor += (t[i][int(s) - 1], )
    elif s in ["a", "b", "c"]:
        vetor = tuple(t[s])

    return vetor

def coloca_peca(t, j, p):
    # coloca_peca: tabuleiro x peca x posicao -> tabuleiro
    """
    A funcao recebe um tabuleiro, uma peca e uma posicao e modifica
    destrutivamente o tabuleiro colocando a peca j na posicao p e devolve o
    proprio tabuleiro.
    """
    col = obter_pos_c(p)
    lin = int(obter_pos_l(p)) - 1
    t[col][lin] = j

    return t

def remove_peca(t, p):
    # remove_peca: tabuleiro x posicao -> tabuleiro
    """
    A funcao recebe um tabuleiro e uma posicao e modifica destrutivamente o
    tabuleiro removendo a peca da posicao p, e devolve o proprio tabuleiro
    """
    return coloca_peca(t, cria_peca(" "), p)

def move_peca(t, p1, p2):
    # move_peca: tabuleiro x posicao x posicao -> tabuleiro
    """
    A funcao recebe um tabuleiro e duas posicoes e modifica destrutivamente o
    tabuleiro movendo a peca que se encontra na posicao p1 para a posicao p2 e
    devolve o proprio tabuleiro.
    """
    j = obter_peca(t, p1)
    return coloca_peca(remove_peca(t, p1), j, p2)

def eh_tabuleiro(arg):
    # eh_tabuleiro: universal -> booelano
    """
    A funcao recebe um argumento de qualquer tipo e devolve True se for um
    TAD tabuleiro e False caso contrario, sem nunca gerar erros.
    """
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
            if dif == 1 or dif == 0: # verifica se um jogador tem mais de uma
                                     # peca a mais do que o outro jogador
                if arg == cria_tabuleiro():
                    return True
                else:
                    for k in ("a", "b", "c"):
                        if arg[k] != vencedor_x or arg[k] != vencedor_o:
                            if arg["a"] != arg["b"] or arg["a"] != arg["c"]:
                                for l in ("1", "2", "3"):
                                    if (obter_vetor(arg, l) != vencedor_x or
                                    obter_vetor(arg, l) != vencedor_o):
                                        if (obter_vetor(arg, "1")
                                        != obter_vetor(arg, "2") or
                                        obter_vetor(arg, "1") !=
                                        obter_vetor(arg, "3")):
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
    # eh_posicao_livre: tabuleiro x posicao -> booleano
    """
    A funcao recebe um tabuleiro e uma posicao e devolve True caso a posicao p
    do tabuleiro corresponder a uma posicao livre e False, caso contrario, sem
    nunca gerar erros.
    """
    return pecas_iguais(obter_peca(t, p), cria_peca(" "))

def vetores_iguais(v1, v2):
    # vetores_iguais: vetor x vetor -> booleano
    """
    A funcao recebe dois vetores e devolve True casos sejam iguais e False, caso
    contrario, sem nunca gerar erros.
    """
    tup = ()
    for i in range(3):
        tup += (pecas_iguais(v1[i], v2[i]), )
    return tup == (True, True, True)

def tabuleiros_iguais(t1, t2):
    # tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
    """
    A funcao recebe dois tabuleiros e devolve True caso t1 e t2 sao tabuleiros e
    sao iguais e False, caso contrario, sem nunca gerar erros.
    """
    if eh_tabuleiro(t1) and eh_tabuleiro(t2):
        veta1 = obter_vetor(t1, "a")
        vetb1 = obter_vetor(t1, "b")
        vetc1 = obter_vetor(t1, "c")
        veta2 = obter_vetor(t2, "a")
        vetb2 = obter_vetor(t2, "b")
        vetc2 = obter_vetor(t2, "c")
        return (vetores_iguais(veta1, veta2) and vetores_iguais(vetb1, vetb2)
                and vetores_iguais(vetc1, vetc2))
    else:
        return False

def tabuleiro_para_str(t):
    # tabuleiro_para_str: tabuleiro -> str
    """
    A funcao recebe um tabuleiro e devolve uma cadeia de caracteres que
    representa o tabuleiro.
    """
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
    # tuplo_para_tabuleiro: tuplo -> tabuleiro
    """
    A funcao recebe um tuplo e devolve o tabuleiro que e representado pelo tuplo
    t.
    """
    tab = cria_tabuleiro()
    for i in range(0, 3):
        tab["a"][i] = inteiro_para_peca(t[i][0])
        tab["b"][i] = inteiro_para_peca(t[i][1])
        tab["c"][i] = inteiro_para_peca(t[i][2])

    return tab

def in_pos(p, pos):
    # in_pos: posicao x tuplo de posicoes -> booleano
    """
    A funcao recebe uma posicao e um tuplo de posicoes e devolve True caso a
    posicao p esteja contido no tuplo pos e False, caso contrario, sem nunca
    gerar erros. 
    """
    tup = ()
    for i in pos:
        tup += (posicoes_iguais(i, p), )
    if True in tup:
        return True
    else:
        return False

def obter_ganhador(t):
    # obter_ganhador: tabuleiro -> peca
    """
    A funcao recebe um tabuleiro e devolve a peca do jogador que tenha ganho, se
    nao existir ganhador, devolve uma peca livre.
    """
    i = 3
    vencedor_x = ()
    vencedor_o = ()
    while i != 0:
        vencedor_x += (cria_peca("X"), )
        vencedor_o += (cria_peca("O"), )
        i -= 1

    for j in ("a", "b", "c", "1", "2", "3"):
        if vetores_iguais(obter_vetor(t, j), vencedor_x):
            return cria_peca("X")
        elif vetores_iguais(obter_vetor(t, j), vencedor_o):
            return cria_peca("O")

    return cria_peca(" ")

def obter_posicoes(t, j):
    # obter_posicoes: tabuleiro x peca -> tuplo de posicoes
    """
    A funcao recebe um tabuleiro e uma peca e devole
    um tuplo com as posicoes ocupadas por essas pecas.
    """
    posicoes = ()
    for i in ("1", "2", "3"):
        for k in ("a", "b", "c"):
            pos = cria_posicao(k, i)
            if pecas_iguais(obter_peca(t, pos), j):
                posicoes += (pos, )

    return posicoes

def obter_posicoes_livres(t):
    # obter_posicoes_livres: tabuleiro -> tuplo de posicoes
    """
    A funcao recebe um tabuleiro e devolve um tuplo com as posicoes nao ocupadas
    por pecas de qualquer um dos dois jogadores.
    """
    return obter_posicoes(t, cria_peca(" "))

def obter_posicoes_jogador(t, j):
    # obter_posicoes_jogador: tabuleiro x peca -> tuplo de posicoes
    """
    A funcao recebe um tabuleiro e uma peca que representa um jogador e devole
    um tuplo com as posicoes ocupadas pelas pecas j de um dos dois jogadores.
    """
    return obter_posicoes(t, j)

def fase_movimento(t):
    # fase_movimento: tabuleiro -> booleano
    """
    A funcao recebe um tabuleiro e devolve True caso o jogo esteja na fase de
    movimento e False, caso contrario, sem nunca gerar erros.
    """
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
    # obter_movimento_manual: tabuleiro x peca -> tuplo de posicoes
    """
    A funcao recebe um tabuleiro e uma peca que representa um jogador e devolve
    um tuplo com uma ou duas posicoes que representam uma posicao ou um 
    introduzido manualmente pelo jogador.
    Se um dos argumentos for invalido gera um erro.
    """
    pos_liv = obter_posicoes_livres(t)
    if fase_movimento(t):
        mov = input("Turno do jogador. Escolha um movimento: ")
        if (isinstance(mov, str) and len(mov) == 4 and mov[0] and mov[2] in
            ("a", "b", "c") and mov[1] and mov[3] in ("1", "2", "3")):
            orig = cria_posicao(mov[0], mov[1])
            dest = cria_posicao(mov[2], mov[3])
            pos_adj = obter_posicoes_adjacentes(orig)

            if not posicoes_iguais(orig, dest):
                if (not in_pos(dest, pos_adj) or not in_pos(dest, pos_liv) or
                    not pecas_iguais(obter_peca(t, orig), j)):
                    raise ValueError("obter_movimento_manual: escolha invalida")
                else:
                    return (orig, dest)
            else:
                for i in pos_adj:
                    if in_pos(i, pos_liv):
                        raise (
                        ValueError("obter_movimento_manual: escolha invalida"))
            return (orig, dest)
        else:
            raise ValueError("obter_movimento_manual: escolha invalida")
    else:
        pos = input("Turno do jogador. Escolha uma posicao: ")
        if (isinstance(pos, str) and len(pos) == 2 and pos[0] in ("a", "b", "c")
            and pos[1] in ("1", "2", "3")):
            posicao = cria_posicao(pos[0], pos[1])
            if not in_pos(posicao, pos_liv):
                raise ValueError("obter_movimento_manual: escolha invalida")
            else:
                return (posicao, )
        else:
            raise ValueError("obter_movimento_manual: escolha invalida")

def pos_vazia(t, j, tup):
    # pos_vazia: tabuleiro x peca x tuplo -> tuplo
    """
    A funcao recebe um tabuleiro, uma peca que representa um jogador e um tuplo
    e devolve um tuplo com a posicao vazia de um certo vetor.
    """
    ganhador1 = (cria_peca(" "), j, j)
    ganhador2 = (j, cria_peca(" "), j)
    ganhador3 = (j, j, cria_peca(" "))

    for i in tup:
        vet = obter_vetor(t, i)
        if (vetores_iguais(vet, ganhador1) or
        vetores_iguais(vet, ganhador2) or
        vetores_iguais(vet, ganhador3)):
           vazio = vet.index(cria_peca(" "))
           return (i, vazio)

def vitoria(t, j):
    # vitoria - tabuleiro x peca -> tuplo de posicoes
    """
    A funcao recebe um tabuleiro e uma peca que representa um jogador e devolve
    uma posicao livre caso o jogador tenha
    duas das suas pecas e uma posicao livre na mesma linha.
    """
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
        return cria_posicao(ch, vazio1[0]),

def bloqueio(t, j):
    # bloqueio - tabuleiro x peca -> tuplo de posicoes
    """
    A funcao recebe um tabuleiro e uma peca que representa um jogador e devolve
    uma posicao livre caso o adversario tenha
    duas das suas pecas e uma posicao livre na mesma linha.
    """
    # Visto que a vitoria e o bloqueio sao muito similares pude reaproveitar
    # o codigo da funcao vitoria
    j = inteiro_para_peca(-peca_para_inteiro(j))
    return vitoria(t, j)

def centro(t):
    # centro: tabuleiro -> tuplo de posicoes
    """
    A funcao recebe um tabuleiro e devolve a posicao livre que equivale
    ao centro do tabuleiro(b2).
    """
    pos_livre = obter_posicoes_livres(t)
    if in_pos(cria_posicao("b", "2"), pos_livre):
        return (cria_posicao("b", "2"), )

def canto_vazio(t):
    # canto_vazio: tabuleiro -> tuplo de posicoes
    """
    A funcao recebe um tabuleiro e devole a posicao livre que equivale
    ao primeiro dos cantos vazios do tabuleiro.
    """
    pos_livre = obter_posicoes_livres(t)
    for i in ("1", "3"):
        for j in ("a", "c"):
            if in_pos(cria_posicao(j, i), pos_livre):
                return (cria_posicao(j, i), )

def lateral_vazio(t):
    # lateral_vazio: tabuleiro -> tuplo de posicoes
    """
    A funcao recebe um tabuleiro e devole a posicao livre que equivale
    a primeira das laterais vazias do tabuleiro.
    """
    pos_livre = obter_posicoes_livres(t)
    if in_pos(cria_posicao("b", "1"), pos_livre):
        return (cria_posicao("b", "1"), )

    for i in ("a", "c"):
        if in_pos(cria_posicao(i, "2"), pos_livre):
            return cria_posicao(i, "2")

    if in_pos(cria_posicao("b", "3"), pos_livre):
        return (cria_posicao("b", "3"), )

def minimax(t, j, prof, seq):
    # minimax: tabuleiro x peca x inteiro(profundidade) x tuplo -> tuplo
    """
    A funcao representa um algoritmo recursivo que consiste na escolha do melhor
    movimento para um proprio assumindo que o adversario ira escolher a pior
    possivel.
    """
    melhor_seq_movimentos = ()
    if peca_para_inteiro(obter_ganhador(t)) != 0 or prof == 0:
        return peca_para_inteiro(obter_ganhador(t)), seq
    else:
        melhor_resultado = - peca_para_inteiro(j)
        for i in obter_posicoes_jogador(t, j):
            for k in obter_posicoes_adjacentes(i):
                if eh_posicao_livre(t, k):
                    (novo_resultado, nova_seq_movimentos) = \
                        minimax(move_peca(cria_copia_tabuleiro(t), i, k),
                                inteiro_para_peca(-peca_para_inteiro(j)),
                                prof - 1, seq + (i, k))
                    if (not melhor_seq_movimentos or
                    (pecas_iguais(j, cria_peca("X")) and
                     novo_resultado > melhor_resultado) or
                    (pecas_iguais(j, cria_peca("O")) and
                     novo_resultado < melhor_resultado)):
                        melhor_resultado, melhor_seq_movimentos = \
                            novo_resultado, nova_seq_movimentos
    return melhor_resultado, melhor_seq_movimentos[0:2]

def movimento_auto_coloc(t, j):
    # movimento_auto_coloc: tabuleiro x peca -> tuplo de posicoes
    """
    A funcao recebe um tabuleiro e uma peca que representa um jogador e devolve
    uma posicao escolhida automaticamente de acordo com a estrategia.
    """
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
    # obter_movimento_auto: tabuleiro x peca x str -> tuplo de posicoes
    """
    A funcao recebe um tabuleiro uma peca que representa um jogador e uma cadeia
    de caracteres que indica a dificuldade do jogo e devolve um tuplo de
    posicoes (que representa um movimento) escolhido automaticamente.
    """
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
            return minimax(t, j, 1, ())[1]
        elif str == "dificil":
            return minimax(t, j, 5, ())[1]

def moinho_jogador(st):
    # moinho_jogador: str -> str
    """
    A funcao recebe uma cadeia de caracteres que indica a dificuldade do
    jogo e devolve uma cadeia de caracteres que representa o vencedor
    do jogo. Esta funcao ira imprimir os sucessivos tabuleiros de jogo
    conforme as jogadas.
    A funcao e utilizada quando o jogador e o primeiro a jogar.
    """
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
        return peca_para_str(obter_ganhador(t))

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

def moinho_computador(st):
    # moinho_computador: str -> str
    """
    A funcao recebe uma cadeia de caracteres que indica a dificuldade do
    jogo e devolve uma cadeia de caracteres que representa o vencedor
    do jogo. Esta funcao ira imprimir os sucessivos tabuleiros de jogo
    conforme as jogadas.
    A funcao e utilizada quando o computador e o primeiro a jogar.
    """
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
        return peca_para_str(obter_ganhador(t))

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
    # moinho: str x str -> str
    """
    Funcao principal que permite jogar um jogo completo do Jogo do Moinho.
    A funcao recebe uma cadeia de caracteres que representa um jogador e outra
    que indica a dificuldade do jogo e devolve uma cadeia de caracteres que
    representa o vencedor do jogo.
    Se um dos argumentos for invalido gera um erro.
    """
    if (not isinstance(jog, str) and (jog == "[X]" or jog == "[O]") or
    not isinstance(st, str) and (st == "facil" or st == "normal" or
    st == "dificil")):
        raise ValueError("moinho: argumentos invalidos")

    print("Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade " + st + ".")

    t = cria_tabuleiro()
    print(tabuleiro_para_str(t))

    if jog == "[X]":
        return moinho_jogador(st)
    else:
        return moinho_computador(st)
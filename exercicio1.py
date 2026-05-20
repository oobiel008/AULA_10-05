def acao_semaforo(cor: str):
    pass 
    cor = cor.lower()

    if cor== 'vermelho':
        return "Pare"
    elif cor== 'amarelo':
        return "Atenção"
    elif cor== 'verde':
        return "Siga"
    return 'Cor inválida'
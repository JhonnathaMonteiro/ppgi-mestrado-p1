def f_avaliacao(VS, M):
    soma = 0
    for i in range(1, len(VS)):
        soma += M[VS[i-1]][VS[i]]
    # Retorno pra origem
    soma += M[VS[-1]][VS[0]]
    return soma

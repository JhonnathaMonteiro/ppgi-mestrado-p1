# Testes para os algoritmos Selection sort e Insertion sort

from algoritmos.insertion_sort import insertionSort
from algoritmos.selection_sort import selectionSort
import timeit
import random
import os

def test_arbitrario(algoritmo, entrada):
    
    t0 = timeit.default_timer()
    saida = algoritmo(entrada)
    t1 = timeit.default_timer()

    tempo = t1-t0

    return saida, tempo

def test_estudo_de_caso(algoritmo):
    # Teste com 3 ordens de listas com 3 tamanhos diferentes n=10, n=100, n=1000
    # Ordem 1: lista ordenada em ordem crescente
    # Ordem 2: lista ordenada em ordem decrescente
    # Ordem 3: lista ordenada em ordem aleatoria
      
    tempos = [[],[],[]]

    for i, n in enumerate([10, 100, 1000]):

        # Ordem 1 - crescente
        entrada1 = [j for j in range(n)]

        # Ordem 2 - decrescente
        entrada2 = entrada1[::-1]

        # Ordem 3 - aleatoria
        entrada3 = [random.randint(0,1000) for _ in range(n)]

        
        for entrada in [entrada1, entrada2, entrada3]:
            
            t0 = timeit.default_timer()
            algoritmo(entrada)
            t1 = timeit.default_timer()

            tempos[i].append(t1-t0)

    return tempos

def test_instancias_numericas():
    folder_inp = os.path.join(os.path.dirname(__file__), 'instancias_numericas')
    folder_out_IS = os.path.join(os.path.dirname(__file__), 'resultados', "insertion_sort")
    folder_out_SS = os.path.join(os.path.dirname(__file__), 'resultados', "selection_sort")
    file_names = ["num.1000.1.in",
                # "num.1000.2.in",
                "num.1000.3.in",
                # "num.1000.4.in",
                "num.10000.1.in",]
                # "num.10000.2.in",
                # "num.10000.3.in",
                # "num.10000.4.in",
                # "num.100000.1.in",
                # "num.100000.2.in",
                # "num.100000.3.in",
                # "num.100000.4.in"]

    for f in file_names:
        file_in_path = os.path.join(folder_inp, f)
        file_out_path_IS = os.path.join(folder_out_IS, f)
        file_out_path_SS = os.path.join(folder_out_SS, f)


        entrada = []

        with open(file_in_path, "r") as inpfile:
            for line in inpfile:
                entrada.append(int(line.strip("\n")))
        
        t0 = timeit.default_timer()
        saida_IS = insertionSort(entrada[:])
        t1 = timeit.default_timer()
        tempo_IS = t1-t0

        t0 = timeit.default_timer()
        saida_SS = selectionSort(entrada[:])
        t1 = timeit.default_timer()
        tempo_SS=t1-t0

        print("Instancia: {}    Algoritmo: Insertion Sort    Tempo (s): {:.4e}".format(f, tempo_IS))
        print("Instancia: {}    Algoritmo: Selection Sort    Tempo (s): {:.4e}".format(f, tempo_SS))

        with open(file_out_path_IS, "w") as outfile:
            for item in saida_IS:
                outfile.write("%s\n" % item)

        with open(file_out_path_SS, "w") as outfile:
            for item in saida_SS:
                outfile.write("%s\n" % item)

# Saida de dados
print ('{:=^50}\n'.format('TESTE INSTANCIAS NUMERICAS'))
test_instancias_numericas()

entrada = [21, 43, 55, 2, 18, 98, 10]
print ('\n{:=^50}\n'.format('TESTE ARBITRARIO'))
print('{:-^50}'.format("Insertion Sort"))
print("Entrada: ", entrada[:])
saida, tempo = test_arbitrario(insertionSort, entrada)
print("Saida: ", saida)
print("Tempo: {:.4e}".format(tempo), "segundos\n")

print('{:-^50}'.format("Selection Sort"))
print("Entrada: ", entrada[:])
saida, tempo = test_arbitrario(selectionSort, entrada)
print("Saida: ", saida)
print("Tempo: {:.4e}".format(tempo), "segundos\n")

print ('{:=^50}\n'.format('ESTUDO DE CASO'))
tempos_IS = test_estudo_de_caso(insertionSort) # Tempos do Insertion Sort
tempos_SS = test_estudo_de_caso(selectionSort) # Tempos do Selection Sort

print("PARA n = 10            ______________Ordem do Vetor de Entrada_____________")
print("---------------------- Crescente --------- Decrescente ---------- Aleatoria")
print("Insertion Sort        {:.4e}            {:.4e}           {:.4e}".format(tempos_IS[0][0], tempos_IS[0][1], tempos_IS[0][2]))
print("Selection Sort        {:.4e}            {:.4e}           {:.4e}\n\n".format(tempos_SS[0][0], tempos_SS[0][1], tempos_SS[0][2]))


print("PARA n = 100           ______________Ordem do Vetor de Entrada_____________")
print("---------------------- Crescente --------- Decrescente ---------- Aleatoria")
print("Insertion Sort        {:.4e}            {:.4e}           {:.4e}".format(tempos_IS[1][0], tempos_IS[1][1], tempos_IS[1][2]))
print("Selection Sort        {:.4e}            {:.4e}           {:.4e}\n\n".format(tempos_SS[1][0], tempos_SS[1][1], tempos_SS[1][2]))

print("PARA n = 1000          ______________Ordem do Vetor de Entrada_____________")
print("---------------------- Crescente --------- Decrescente ---------- Aleatoria")
print("Insertion Sort        {:.4e}            {:.4e}           {:.4e}".format(tempos_IS[2][0], tempos_IS[2][1], tempos_IS[2][2]))
print("Selection Sort        {:.4e}            {:.4e}           {:.4e}\n\n".format(tempos_SS[2][0], tempos_SS[2][1], tempos_SS[2][2]))

import numpy as np
import matplotlib.pyplot as plt
from hill_climbing import HillClimbing
from local_random_search import LocalRandomSearch
from global_random_search import GlobalRandomSearch
from time import time
from statistics import multimode

def f(x, y):
    return x * np.sin(4 * np.pi * x) - y * np.sin(4 * np.pi * y) + 1

lim_inf = -1
lim_sup = 3

while True:
    print(
        "Escolha o modelo para ser testado:\n" \
        "1. Hill Climbing\n" \
        "2. Local Random Search\n" \
        "3. Global Random Search\n" \
        "0. Sair"
    )

    escolha = int(input("Digite sua escolha: "))

    if escolha not in [0, 1, 2, 3]:
        print("Escolha inválida. Tente novamente.\n")
        continue
    else:
        if escolha == 0:
            print("Saindo...")
            break

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        x_axis = np.linspace(lim_inf, lim_sup, 500)
        X, Y = np.meshgrid(x_axis, x_axis)

        ax.plot_surface(X, Y, f(X, Y), rstride=20, cstride=20, alpha=.3, edgecolor='k')

        R = 100
        resultados = []

        ti = time()

        if escolha == 1:
            for i in range(R):
                hc = HillClimbing(
                    func=f, 
                    goal='max', 
                    epsilon=1.3,
                    max_it=1_000,
                    max_vizinhos=30, 
                    lim_inf=lim_inf, 
                    lim_sup=lim_sup,
                    t=300
                )

                x_opt, f_opt, _ = hc.climb()

                resultados.append((round(x_opt[0], 3), round(x_opt[1], 3)))

        elif escolha == 2:
            for i in range(R):
                lrs = LocalRandomSearch(
                    func=f,
                    goal='max',
                    sigma=0.5,
                    max_it=1_000,
                    lim_inf=lim_inf,
                    lim_sup=lim_sup,
                    t=300
                )

                x_opt, f_opt, _ = lrs.search()

                resultados.append((round(x_opt[0], 2), round(x_opt[1], 2)))

        else:
            for i in range(R):
                grs = GlobalRandomSearch(
                    func=f,
                    goal='max',
                    max_it=1_000,
                    lim_inf=lim_inf,
                    lim_sup=lim_sup,
                    t=1_000
                )

                x_opt, f_opt, _ = grs.search()

                resultados.append((round(x_opt[0], 1), round(x_opt[1], 1)))

        tf = time()

        modas = multimode(resultados)
        moda_solucao = modas[0]
        freq = resultados.count(moda_solucao)

        print("\n---------- Resultados ----------")
        print(f"Tempo de execução: {tf - ti:.5f} s")
        print(f"Moda das {R} rodadas: {moda_solucao}")
        print(f"Quantidade de vezes que apareceu: {freq}")

        ax.scatter(*moda_solucao, f(*moda_solucao), c='g', s=200, marker='X')

        plt.show()

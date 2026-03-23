from simulated_annealing import SA8Rainhas
from time import time

def achar_uma_solucao():
    sa = SA8Rainhas()
    x, f_val, it, t = sa.rodar()
    print("\nSolução encontrada:", x)
    print("Conflitos (f):", f_val)
    print("Iterações usadas:", it)
    print(f"Tempo de execução: {t:.4f} s\n")


def achar_92_solucoes(mostrar_progresso=False):
    solucoes = set()
    total_iters = 0
    total_runs = 0
    tempos = []

    print("\nIniciando busca pelas 92 soluções únicas...")

    ti = time()
    while len(solucoes) < 92:
        total_runs += 1
        sa = SA8Rainhas()
        x, f_val, it, t_run = sa.rodar()

        if f_val == 0:
            solucoes.add(tuple(x))
            total_iters += it
            tempos.append(t_run)

            if mostrar_progresso and len(solucoes) % 5 == 0:
                print(f"{len(solucoes)} soluções encontradas...", end="\r")

    tf = time()
    tempo_total = tf - ti
    qtd = len(solucoes)

    print("\n\n---------- RESULTADOS ----------")
    print("Soluções únicas encontradas:", qtd)
    print(f"Tempo total: {tempo_total:.2f} s")
    print(f"Total de execuções do SA: {total_runs}")
    print(f"Iterações totais consumidas: {total_iters}")
    if qtd > 0:
        print(f"Tempo médio por solução: {sum(tempos)/len(tempos):.4f} s")
        print(f"It. média por solução: {total_iters / qtd:.2f}")
        print(f"Runs por solução média: {total_runs / max(1, qtd):.2f}")
    print("--------------------------------\n")

    return solucoes, {
        "tempo_total": tempo_total,
        "total_runs": total_runs,
        "total_iters": total_iters,
        "tempo_medio_por_sol": (sum(tempos)/len(tempos)) if tempos else None
    }



while True:
    print(
        "Faça sua escolha:\n"
        "1 - Achar uma solução\n"
        "2 - Achar 92 soluções distintas + métricas\n"
        "0 - Sair"
    )

    try:
        choice = int(input("Sua escolha: "))
    except ValueError:
        print("Entrada inválida. Digite um número.\n")
        continue

    if choice not in [0, 1, 2]:
        print("Escolha inválida. Tente novamente.\n")
        continue

    elif choice == 1:
        achar_uma_solucao()

    elif choice == 2:
        achar_92_solucoes(mostrar_progresso=True)

    else:
        print("Saindo...")
        break

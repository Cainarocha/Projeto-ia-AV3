import numpy as np
from time import time

class SA8Rainhas:

    def __init__(self, max_it=5000, T=10, sigma=1, alpha=0.99):
        self.max_it = max_it
        self.T0 = T
        self.sigma = sigma
        self.alpha = alpha

    def f(self, x):
        conflitos = 0
        
        for i in range(8):
            for j in range(i + 1, 8):
                if x[i] == x[j] or abs(i - j) == abs(x[i] - x[j]):
                    conflitos += 1
    
        return conflitos

    def vizinho(self, x):
        x_cand = x.copy()
        col = np.random.randint(0, 8)
        nova_linha = np.random.randint(1, 9)
        
        while nova_linha == x_cand[col]:
            nova_linha = np.random.randint(1, 9)

        x_cand[col] = nova_linha

        return x_cand

    def escalona(self, T):
        return T * self.alpha

    def rodar(self):
        t0 = time()

        x_opt = np.random.randint(1, 9, size=8)
        f_opt = self.f(x_opt)

        T = self.T0
        it = 0

        for i in range(self.max_it):
            it += 1
            x_cand = self.vizinho(x_opt)
            f_cand = self.f(x_cand)

            delta = f_cand - f_opt
            P = np.exp(-delta / T) if delta > 0 else 1.0

            if f_cand < f_opt or P >= np.random.random():
                x_opt = x_cand
                f_opt = f_cand

            T = self.escalona(T)

            if f_opt == 0:
                break

        tf = time()

        return x_opt.tolist(), int(f_opt), it, (tf - t0)

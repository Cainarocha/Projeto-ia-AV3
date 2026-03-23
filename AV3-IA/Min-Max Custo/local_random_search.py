import numpy as np
import matplotlib.pyplot as plt

class LocalRandomSearch:
    def __init__(self, func, goal, sigma, max_it, lim_inf, lim_sup, t):
        self.func = func
        self.goal = goal # 'max' ou 'min'
        self.sigma = sigma
        self.max_it = max_it
        self.lim_inf = lim_inf
        self.lim_sup = lim_sup
        self.t = t

        self.x_opt = np.random.uniform(lim_inf, lim_sup, size=2)
        self.f_opt = self.func(*self.x_opt)

        self.historico = []

    def perturb(self):
        x_cand = self.x_opt + np.random.normal(0, self.sigma, size=2)

        for i, x in enumerate(x_cand):
            if x < self.lim_inf:
                x_cand[i] = self.lim_inf
            if x > self.lim_sup:
                x_cand[i] = self.lim_sup

        return x_cand
    
    def search(self):
        it = 0
        sem_melhoria = 0

        while it < self.max_it and sem_melhoria < self.t:
            x_cand = self.perturb()
            f_cand = self.func(*x_cand)
            self.historico.append(self.f_opt)

            melhorou = (
                (self.goal == 'max' and f_cand > self.f_opt)
                or
                (self.goal == 'min' and f_cand < self.f_opt)
            )

            if melhorou:
                self.x_opt = x_cand
                self.f_opt = f_cand
                sem_melhoria = 0
            else:
                sem_melhoria += 1

            it += 1

        return self.x_opt, self.f_opt, self.historico
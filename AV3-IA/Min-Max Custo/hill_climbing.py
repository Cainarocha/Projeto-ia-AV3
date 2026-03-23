import numpy as np
import matplotlib.pyplot as plt

class HillClimbing:
    def __init__(self, func, goal, epsilon, max_it, max_vizinhos, lim_inf, lim_sup, t, ax=None):
        self.func = func
        self.goal = goal # 'max' ou 'min'
        self.epsilon = epsilon
        self.max_it = max_it
        self.max_vizinhos = max_vizinhos
        self.lim_inf = lim_inf
        self.lim_sup = lim_sup
        self.t = t

        self.ax = ax

        self.historico = []
        self.x_opt = None
        self.f_opt = None

    def climb(self):
        self.x_opt = np.array([self.lim_inf, self.lim_inf], dtype=float)
        self.f_opt = self.func(*self.x_opt)
        self.historico = [self.f_opt]

        if self.ax is not None:
            self.ax.scatter(*self.x_opt, self.f_opt, c='r',s=40)

        it = 0
        sem_melhoria = 0

        while it < self.max_it and sem_melhoria < self.t:
            melhorou_iteracao = False

            for j in range(self.max_vizinhos):
                # Pertubação
                x_cand = np.random.uniform(-self.epsilon, self.epsilon, size=2) + self.x_opt

                for i, x in enumerate(x_cand):
                    if x < self.lim_inf:
                        x_cand[i] = self.lim_inf
                    if x > self.lim_sup:
                        x_cand[i] = self.lim_sup

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
                    melhorou_iteracao = True
                    break

            if melhorou_iteracao:
                sem_melhoria = 0
            else:
                sem_melhoria += 1

            it += 1

        if self.ax is not None:
            self.ax.scatter(*self.x_opt, self.f_opt, c='g', s=200, marker='*')

        return self.x_opt, self.f_opt, self.historico

        



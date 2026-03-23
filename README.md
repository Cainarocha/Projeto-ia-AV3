# 🤖 Busca e Otimização Meta-Heurística (IA)

## 📖 Descrição
Este projeto foi desenvolvido para a disciplina de **Inteligência Artificial**, com o objetivo de resolver problemas de **busca e otimização** utilizando **algoritmos meta-heurísticos**.

O trabalho aborda tanto problemas de **domínio contínuo** quanto **domínio discreto**, aplicando diferentes estratégias para encontrar soluções ótimas ou subótimas em espaços de busca complexos.

---

## 🎯 Objetivos
- Aplicar algoritmos de busca e otimização meta-heurística  
- Resolver problemas contínuos e discretos  
- Comparar desempenho entre diferentes algoritmos  
- Analisar resultados estatísticos das execuções  

---

## 🧠 Algoritmos Implementados

### 🔹 Parte 1 – Problemas Contínuos
- Hill Climbing (Subida de Encosta)  
- Local Random Search (LRS)  
- Global Random Search (GRS)  

📌 Características:
- Execução de **100 rodadas por algoritmo**  
- Máximo de **1000 iterações por execução**  
- Parada antecipada baseada em ausência de melhoria  
- Respeito às restrições de domínio das variáveis  

---

### 🔹 Parte 2 – Problemas Discretos

#### ♟️ Problema das 8 Rainhas
- Resolvido com **Simulated Annealing (Têmpera Simulada)**  
- Representação por vetor de posições  
- Função objetivo baseada no número de conflitos  

#### 🚚 Problema do Caixeiro Viajante (TSP)
- Resolvido com **Algoritmo Genético (GA)**  
- Representação cromossômica de rotas  
- Operadores implementados:
  - Seleção por torneio  
  - Crossover (adaptado para permutação)  
  - Mutação (troca de genes)  
- Probabilidade de mutação: **1%**  

---

## 📊 Problemas Resolvidos

### 🔸 Otimização Contínua
- Minimização:  
  - f(x₁, x₂) = x₁² + x₂²  
- Maximização e minimização de funções não lineares complexas  
- Funções com múltiplos mínimos locais (ex: Rastrigin, Ackley)  

### 🔸 Otimização Discreta
- 8 Rainhas (92 soluções possíveis)  
- Caixeiro Viajante com pontos gerados aleatoriamente  

---

## 🧬 Metodologia
- Execução repetida dos algoritmos para análise estatística  
- Armazenamento dos resultados a cada rodada  
- Cálculo da **moda das soluções obtidas**  
- Ajuste de hiperparâmetros (ε, σ, temperatura, etc.)  


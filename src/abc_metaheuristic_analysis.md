# Análise de Desempenho: Artificial Bee Colony (ABC) no JSSP

Este documento resume os resultados obtidos pela meta-heurística Artificial Bee Colony (ABC) na resolução do problema de Job Shop Scheduling (JSSP), comparando-a com outras técnicas implementadas.

## 1. Resumo da Meta-heurística
A meta-heurística **Artificial Bee Colony (ABC)** simula o comportamento de forrageamento de abelhas. No contexto do JSSP, ela utiliza três tipos de agentes:
- **Abelhas Operárias:** Exploram soluções vizinhas às fontes de alimento conhecidas.
- **Abelhas Observadoras:** Escolhem fontes de alimento com base na qualidade (fitness).
- **Abelhas Exploradoras:** Abandonam soluções estagnadas para encontrar novas áreas do espaço de busca.

## 2. Resultados dos Testes (Caso TC_001)
Baseado no arquivo [src/all_metaheuristics_results_1.csv](src/all_metaheuristics_results_1.csv):

| Métrica | Valor Médio / Comportamento |
| :--- | :--- |
| **Fitness (Makespan)** | **1.0** (Atingiu o ótimo/referência em todas as rodadas) |
| **Taxa de Acerto (Hit Rate)** | **100%** |
| **Tempo de Execução Médio** | **~18.73 segundos** |
| **Variabilidade Temporal** | Alta (mín: 16.54s, máx: 23.93s) |

## 3. Comparativo com Outras Meta-heurísticas
| Algoritmo | Tempo Médio (s) | Acurácia (Fitness) |
| :--- | :--- | :--- |
| **Genetic Algorithm (GA)** | ~0.15s | 1.0 |
| **Simulated Annealing (SA)**| ~0.15s | 1.0 |
| **Artificial Bee Colony (ABC)** | **~18.73s** | **1.0** |
| **PSO** | ~7.5s | 1.0 |

## 4. Pontos Importantes e Conclusões

### Pontos Fortes
- **Robustez Extrema:** Garantiu a convergência para a melhor solução (fitness 1.0) em 100% dos casos de teste analisados.
- **Exploração e Explotação:** O equilíbrio entre as fases de abelhas operárias e observadoras permite escapar de ótimos locais com eficácia.

### Pontos Fracos
- **Baixa Eficiência Computacional:** É a meta-heurística mais lenta do conjunto (aproximadamente 120 vezes mais lenta que o algoritmo Genético).
- **Custo Operacional:** Devido ao seu processo iterativo tripartido, o ABC demanda muito mais poder de processamento para entregar o mesmo resultado que técnicas mais leves.

### Recomendação de Uso
O **ABC** é recomendado exclusivamente para cenários onde a qualidade da solução é crítica e o tempo de processamento não é um fator limitante (planejamento *long-term* ou instâncias extremamente complexas onde outras técnicas falham em convergir). Para agendamentos dinâmicos ou de tempo real, o algoritmo **Genético** ou **Simulated Annealing** são preferíveis.

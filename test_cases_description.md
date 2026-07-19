# Documentação dos Casos de Teste (Benchmark Brandimarte 1993)

Este documento descreve a origem, estrutura e as adaptações aplicadas aos casos de teste utilizados neste projeto de avaliação de meta-heurísticas para o JSSP Flexível.

---

## 1. Origem: Benchmark de Brandimarte (1993)

Os casos de teste identificados pelo prefixo `MK` (ex: `TC_MK01`, `TC_MK07`) são baseados no artigo clássico de **Paolo Brandimarte (1993)**: *"Routing and scheduling in a flexible job shop by Tabu Search"*. 

Este benchmark é amplamente utilizado na literatura de otimização para testar problemas de **Flexible Job Shop Scheduling (FJSSP)**, onde:
- Cada tarefa (*Job*) possui uma sequência de operações.
- Cada operação pode ser processada em mais de uma máquina (Flexibilidade de Rota).
- O objetivo original é minimizar o *makespan* (Cmax).

---

## 2. Estrutura dos Dados no Projeto

As instâncias em [tests/test.py](tests/test.py) estão organizadas em dicionários Python com a seguinte estrutura:

```python
'job_X': [ ([máquinas_compatíveis], [equipamentos_necessários], duração), ... ]
```

### Componentes:
*   **Flexibilidade**: A lista de máquinas compatíveis permite que a meta-heurística escolha o melhor recurso para cada operação.
*   **Tempos de Processamento**: Duração fixa para a operação, independentemente da máquina escolhida (conforme a simplificação comum de algumas variações do benchmark).
*   **Timespan de Referência**: O campo `timespan` no dicionário representa o **Best Known Result (BKR)** ou o limite superior reportado na literatura para aquela instância específica.

---

## 3. Variações: NORMAL vs ADAPTADO

Para aumentar a complexidade e o realismo do estudo, cada instância de Brandimarte foi implementada em duas versões:

### A. Versão NORMAL (Benchmark Puro)
*   Representa a instância original de 1993.
*   **Restrições**: Apenas precedência entre operações do mesmo Job e capacidade das máquinas (uma operação por vez).
*   **Downtimes**: Dicionário de interrupções vazio.
*   **Equipamentos**: Nenhuma operação exige equipamentos secundários.

### B. Versão ADAPTADA (Extensão do Problema)
Esta versão transforma o problema clássico em um **SJSSP (Scheduled JSSP)** com restrições do mundo real:
*   **Machine Downtimes**: Introduz períodos de indisponibilidade programada para as máquinas (ex: manutenção, trocas de turno). As operações não podem ocorrer durante esses intervalos.
*   **Equipamentos Compartilhados**: Operações agora podem exigir um ou mais equipamentos secundários (ferramentas, moldes, dispositivos). Isso cria um gargalo adicional, pois um equipamento pode ser necessário em diferentes máquinas simultaneamente.
*   **Maior Complexidade**: O *makespan* de referência é significativamente maior devido às janelas de tempo perdidas e espera por equipamentos.

---

## 4. Resumo das Instâncias Utilizadas

| Instância | Tarefas (n) | Máquinas (m) | Operações (total) | Nível de Flexibilidade |
| :--- | :---: | :---: | :---: | :--- |
| **MK01** | 10 | 6 | 70 | Baixa |
| **MK02** | 10 | 6 | 58 | Média |
| **MK07** | 20 | 5 | 100 | Alta |

*Nota: Os detalhes completos de máquinas e tempos por operação podem ser consultados diretamente no arquivo [tests/test.py](tests/test.py).*

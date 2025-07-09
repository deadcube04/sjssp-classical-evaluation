# obs.: esse arquivo serve pra testar muita coisa, não leve ele em consideração

import numpy as np
from classes.jssp import jssp
from mealpy import SA
from mealpy.utils.space import FloatVar
import matplotlib.pyplot as plt

def decode_solution(solution_vec, operations):
    import numpy as np
    order = np.argsort(solution_vec)

    machine_available = {}
    job_available = {}

    print("Ordem com máquina usada:")

    for i, idx in enumerate(order):
        op = operations[idx]
        job = op["job"]

        # Se quiser a regra de escolha original, substitua esta linha:
        # machine = op["machines"][0]

        # Exemplo: escolher a máquina que fica disponível primeiro
        machine = min(op["machines"], key=lambda m: machine_available.get(m, 0)) # verificar com pamela

        start_time = max(machine_available.get(machine, 0), job_available.get(job, 0))
        end_time = start_time + op["duration"]

        machine_available[machine] = end_time
        job_available[job] = end_time

        print(f"{i+1}: {op['job']}, Máquina {machine}, Duração {op['duration']}, Início {start_time}, Fim {end_time}")


# Função que retorna uma função de avaliação (fitness) personalizada
# baseada na instância do JSSP que você criou com suas classes
def make_fitness_function(instance: jssp):

    # Gera uma lista de dicionários com informações sobre cada operação
    # Isso é feito uma única vez fora da função fitness por eficiência
    operations = instance.get_flattened_operations()

    # Esta é a função que o mealpy usará para avaliar cada solução
    def fitness(solution):
        import numpy as np

        # Ordena os índices das operações com base nos valores do vetor de entrada
        # Isso define a ordem de execução das operações
        priority_order = np.argsort(solution)

        # Dicionários para acompanhar quando cada máquina e cada job estarão disponíveis
        machine_available = {}  # ex: {1: 5} → máquina 1 estará livre no tempo 5
        job_available = {}      # ex: {"job_1": 4} → job_1 pode iniciar próxima operação no tempo 4
        end_times = []          # armazenará o tempo de término de cada operação

        # Executa as operações na ordem definida pelo vetor de prioridade
        for idx in priority_order:
            op = operations[idx]  # Recupera a operação pelo índice

            job = op["job"]               # Nome do job (ex: "job_1")
            machine = min(op["machines"], key=lambda m: machine_available.get(m, 0)) # Seleciona a máquina disponível mais cedo
            duration = op["duration"]     # Duração da operação

            # O início da operação depende da disponibilidade da máquina e do job
            start_time = max(
                machine_available.get(machine, 0),  # se máquina não usada ainda, começa em 0
                job_available.get(job, 0)           # se job ainda não iniciou, começa em 0
            )

            end_time = start_time + duration  # Tempo em que a operação termina

            # Atualiza os dicionários com a nova disponibilidade após a operação
            machine_available[machine] = end_time
            job_available[job] = end_time

            end_times.append(end_time)  # Salva o tempo final da operação

        # O makespan é o tempo máximo de término entre todas as operações
        return max(end_times),  # Retorna como tupla, como o mealpy exige

    # Retorna a função de fitness já configurada com os dados da instância
    return fitness

def simulate_schedule(solution_vec, operations):
    order = np.argsort(solution_vec)
    machine_available = {}
    job_available = {}
    schedule = []

    for idx in order:
        op = operations[idx]
        job = op["job"]
        machine = min(op["machines"], key=lambda m: machine_available.get(m, 0))

        start_time = max(machine_available.get(machine, 0), job_available.get(job, 0))
        end_time = start_time + op["duration"]

        machine_available[machine] = end_time
        job_available[job] = end_time

        schedule.append({
            "job": job,
            "machine": machine,
            "start": start_time,
            "end": end_time,
            "duration": op["duration"],
            "op_index": idx
        })

    return schedule

def plot_gantt(schedule):
    machines = sorted(set(op['machine'] for op in schedule))
    machine_to_y = {m: i for i, m in enumerate(machines)}

    fig, ax = plt.subplots(figsize=(10, 6))

    for op in schedule:
        start = op["start"]
        duration = op["duration"]
        machine = op["machine"]
        y = machine_to_y[machine]

        ax.barh(y, duration, left=start, height=0.4, align='center', edgecolor='black')

        ax.text(start + duration / 2, y, f"{op['job']}", 
                va='center', ha='center', color='white', fontsize=9)

    ax.set_yticks(range(len(machines)))
    ax.set_yticklabels([f"Máquina {m}" for m in machines])
    ax.set_xlabel("Tempo")
    ax.set_title("Gráfico de Gantt - Escalonamento JSSP")

    plt.grid(True, axis='x')
    plt.show()


data = {
    "jobs": {
        "job_1": [([1], [], 1)],
        "job_2": [([2], [], 1)],
        "job_3": [([1, 2], [], 1)],
        "job_4": [([1, 2], [], 1)],
        "job_5": [([1, 2], [], 1)],
        "job_6": [([1, 2], [], 1)],
        "job_7": [([1, 2], [], 1)],
    },
    "machine_downtimes": {},
    "timespan": 2
}

# Instância do problema
instance = jssp(data)
fitness_func = make_fitness_function(instance)
num_ops = len(instance.get_flattened_operations())

# Definindo o problema
problem = {
    "obj_func": fitness_func,
    "bounds": [FloatVar(lb=0.0, ub=1.0) for _ in range(num_ops)],  # ✅ lista de objetos FloatVar
    "minmax": "min",
}

# Rodando uma heurística
model = SA.OriginalSA(epoch=1000)
g_best = model.solve(problem)


print("Melhor vetor:", g_best.solution)
print("Melhor makespan:", g_best.target.fitness)
decode_solution(g_best.solution, instance.get_flattened_operations())

schedule = simulate_schedule(g_best.solution, instance.get_flattened_operations())
plot_gantt(schedule)


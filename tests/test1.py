instancia_mk01_adaptada = {
    "jobs": {
        "job_1": [
            ([1, 2, 3, 4, 5, 6], [], 29),
            ([1, 3, 4, 5, 6], [], 43),
            ([2, 3, 4, 5], [], 16),
            ([1, 2, 5, 6], [], 9),
            ([2, 3, 5, 6], [], 32),
            ([1, 2, 3, 4, 6], [], 26)
        ],
        "job_2": [
            ([2, 3, 4, 5, 6], [], 29),
            ([1, 2, 4, 5], [], 57),
            ([2, 3, 5, 6], [], 19),
            ([1, 2, 3, 4, 6], [], 39),
            ([3, 4, 5, 6], [], 24),
            ([1, 2, 3, 5, 6], [], 28)
        ],
        "job_3": [
            ([1, 3, 4, 5, 6], [], 12),
            ([2, 3, 4, 6], [], 43),
            ([1, 2, 4, 5], [], 20),
            ([3, 5, 6], [], 44),
            ([1, 2, 3, 4, 5], [], 43),
            ([2, 4, 5, 6], [], 16)
        ],
        "job_4": [
            ([1, 2, 4, 5, 6], [], 34),
            ([1, 2, 3, 5], [], 16),
            ([3, 4, 5, 6], [], 24),
            ([1, 2, 3, 5, 6], [], 17),
            ([1, 2, 4, 5], [], 61),
            ([3, 4, 5, 6], [], 49)
        ],
        "job_5": [
            ([2, 3, 4, 5], [], 29),
            ([1, 3, 4, 6], [], 51),
            ([2, 3, 5, 6], [], 19),
            ([1, 2, 4, 6], [], 39),
            ([1, 3, 5, 6], [], 29),
            ([2, 3, 4, 5, 6], [], 28)
        ],
        "job_6": [
            ([1, 2, 4, 5, 6], [], 29),
            ([2, 3, 4, 5, 6], [], 43),
            ([1, 3, 4, 5, 6], [], 16),
            ([2, 3, 4, 5, 6], [], 9),
            ([1, 3, 4, 6], [], 32),
            ([1, 2, 3, 5], [], 26)
        ],
        "job_7": [
            ([2, 3, 4, 5, 6], [], 29),
            ([1, 2, 3, 4, 5], [], 57),
            ([2, 3, 5, 6], [], 19),
            ([1, 3, 4, 6], [], 39),
            ([2, 3, 4, 5, 6], [], 29),
            ([1, 3, 5, 6], [], 28)
        ],
        "job_8": [
            ([1, 2, 3, 4, 5], [], 21),
            ([2, 3, 4, 6], [], 43),
            ([1, 2, 4, 5, 6], [], 20),
            ([3, 4, 5, 6], [], 44),
            ([1, 3, 4, 5], [], 43),
            ([1, 2, 3, 6], [], 16)
        ],
        "job_9": [
            ([1, 2, 3, 4, 6], [], 34),
            ([2, 3, 4, 5], [], 16),
            ([3, 4, 5, 6], [], 24),
            ([1, 2, 4, 5], [], 17),
            ([1, 2, 4, 5, 6], [], 47),
            ([1, 3, 4, 5, 6], [], 22)
        ],
        "job_10": [
            ([2, 3, 4, 5, 6], [], 29),
            ([1, 2, 3, 6], [], 51),
            ([2, 3, 4, 5], [], 19),
            ([1, 2, 3, 4, 6], [], 39),
            ([1, 3, 4, 5, 6], [], 29),
            ([2, 3, 4, 5, 6], [], 28)
        ]
    },
    "machine_downtimes": {},
    "timespan": None
}

# Instância Mk01 adaptada para DRCFJSP (Máquinas + Equipamentos)
# A <duração> ainda é o tempo mínimo da máquina.
instancia_mk01_com_equipamentos = {
    "jobs": {
        "job_1": [
            ([1, 2, 3, 4, 5, 6], [1], 29),
            ([1, 3, 4, 5, 6], [1], 43),
            ([2, 3, 4, 5], [1], 16),
            ([1, 2, 5, 6], [1], 9),
            ([2, 3, 5, 6], [1], 32),
            ([1, 2, 3, 4, 6], [1], 26)
        ],
        "job_2": [
            ([2, 3, 4, 5, 6], [1], 29),
            ([1, 2, 4, 5], [1], 57),
            ([2, 3, 5, 6], [1], 19),
            ([1, 2, 3, 4, 6], [1], 39),
            ([3, 4, 5, 6], [1], 24),
            ([1, 2, 3, 5, 6], [1], 28)
        ],
        "job_3": [
            ([1, 3, 4, 5, 6], [2], 12),
            ([2, 3, 4, 6], [2], 43),
            ([1, 2, 4, 5], [2], 20),
            ([3, 5, 6], [2], 44),
            ([1, 2, 3, 4, 5], [2], 43),
            ([2, 4, 5, 6], [2], 16)
        ],
        "job_4": [
            ([1, 2, 4, 5, 6], [2], 34),
            ([1, 2, 3, 5], [2], 16),
            ([3, 4, 5, 6], [2], 24),
            ([1, 2, 3, 5, 6], [2], 17),
            ([1, 2, 4, 5], [2], 61),
            ([3, 4, 5, 6], [2], 49)
        ],
        "job_5": [
            ([2, 3, 4, 5], [3], 29),
            ([1, 3, 4, 6], [3], 51),
            ([2, 3, 5, 6], [3], 19),
            ([1, 2, 4, 6], [3], 39),
            ([1, 3, 5, 6], [3], 29),
            ([2, 3, 4, 5, 6], [3], 28)
        ],
        "job_6": [
            ([1, 2, 4, 5, 6], [3], 29),
            ([2, 3, 4, 5, 6], [3], 43),
            ([1, 3, 4, 5, 6], [3], 16),
            ([2, 3, 4, 5, 6], [3], 9),
            ([1, 3, 4, 6], [3], 32),
            ([1, 2, 3, 5], [3], 26)
        ],
        "job_7": [
            ([2, 3, 4, 5, 6], [4], 29),
            ([1, 2, 3, 4, 5], [4], 57),
            ([2, 3, 5, 6], [4], 19),
            ([1, 3, 4, 6], [4], 39),
            ([2, 3, 4, 5, 6], [4], 29),
            ([1, 3, 5, 6], [4], 28)
        ],
        "job_8": [
            ([1, 2, 3, 4, 5], [4], 21),
            ([2, 3, 4, 6], [4], 43),
            ([1, 2, 4, 5, 6], [4], 20),
            ([3, 4, 5, 6], [4], 44),
            ([1, 3, 4, 5], [4], 43),
            ([1, 2, 3, 6], [4], 16)
        ],
        "job_9": [
            ([1, 2, 3, 4, 6], [1, 3], 34),
            ([2, 3, 4, 5], [1, 3], 16),
            ([3, 4, 5, 6], [1, 3], 24),
            ([1, 2, 4, 5], [1, 3], 17),
            ([1, 2, 4, 5, 6], [1, 3], 47),
            ([1, 3, 4, 5, 6], [1, 3], 22)
        ],
        "job_10": [
            ([2, 3, 4, 5, 6], [1, 3], 29),
            ([1, 2, 3, 6], [1, 3], 51),
            ([2, 3, 4, 5], [1, 3], 19),
            ([1, 2, 3, 4, 6], [1, 3], 39),
            ([1, 3, 4, 5, 6], [1, 3], 29),
            ([2, 3, 4, 5, 6], [1, 3], 28)
        ]
    },
    "machine_downtimes": {},
    "timespan": 711
}

instancia_simples_3x3 = {
    "jobs": {
        "job_1": [
            ([1, 2], [1], 5),   # Op 1 (J1)
            ([3], [2], 8)    # Op 2 (J1)
        ],
        "job_2": [
            ([1], [2], 7),   # Op 1 (J2)
            ([2, 3], [2], 6)    # Op 2 (J2)
        ],
        "job_3": [
            ([2], [1], 4),   # Op 1 (J3)
            ([1, 3], [1], 9)    # Op 2 (J3)
        ]
    },
    "machine_downtimes": {},
    "timespan": 21
}

# Baseada na instância 4x5 de Kacem et al. (2002)
instancia_kacem_4x5 = {
    "jobs": {
        "job_1": [
            ([1, 2, 3], [10], 2),
            ([2, 4], [10], 3),
            ([1, 2], [10], 4)
        ],
        "job_2": [
            ([1, 3], [10], 4),
            ([2, 5], [10], 7),
            ([3, 4], [10], 5)
        ],
        "job_3": [
            ([2, 3], [20], 5),
            ([1, 5], [20], 3),
            ([2, 4], [20], 5)
        ],
        "job_4": [
            ([3, 4], [20], 2),
            ([1, 5], [20], 7),
            ([1, 2, 3], [20], 5)
        ]
    },
    "machine_downtimes": {},
    "timespan": 27.0
}

# Subconjunto da Mk01 (Jobs 1-5, Máquinas 1-4)
# (Durações recalculadas para o tempo mínimo entre as máquinas 1-4)
instancia_mk01_pequena_5x4 = {
    "jobs": {
        "job_1": [
            ([1, 2, 3, 4], [1], 29),
            ([1, 3, 4], [1], 43),
            ([2, 3, 4], [1], 16),
            ([1, 2], [1], 71),         # Min time (M1, M2)
            ([2, 3], [1], 32),         # Min time (M2, M3)
            ([1, 2, 3, 4], [1], 43)
        ],
        "job_2": [
            ([2, 3, 4], [1], 29),
            ([1, 2, 4], [1], 63),
            ([2, 3], [1], 41),
            ([1, 2, 3, 4], [1], 53),
            ([3, 4], [1], 24),
            ([1, 2, 3], [1], 28)
        ],
        "job_3": [
            ([1, 3, 4], [2], 21),
            ([2, 3, 4], [2], 43),
            ([1, 2, 4], [2], 20),
            ([3], [2], 89),
            ([1, 2, 3, 4], [2], 43),
            ([2, 4], [2], 36)
        ],
        "job_4": [
            ([1, 2, 4], [2], 52),      # Min time (M1, M2, M4)
            ([1, 2, 3], [2], 16),
            ([3, 4], [2], 61),
            ([1, 2, 3], [2], 40),
            ([1, 2, 4], [2], 61),
            ([3, 4], [2], 63)
        ],
        "job_5": [
            ([2, 3, 4], [3], 29),
            ([1, 3, 4], [3], 51),
            ([2, 3], [3], 41),
            ([1, 2, 4], [3], 53),
            ([1, 3], [3], 46),
            ([2, 3, 4], [3], 28)
        ]
    },
    "machine_downtimes": {},
    "timespan": 545
}

# Adding instances from Results folder

TC_001 = {
    "jobs": {
        "job_1": [([1], [], 1)],
        "job_2": [([2], [], 1)],
        "job_3": [([3], [], 1)]
    },
    "machine_downtimes": {},
    "timespan": 1
}

TC_002 = {
    "jobs": {
        "job_1": [([1], [], 1)],
        "job_2": [([1], [], 1)],
        "job_3": [([1], [], 1)]
    },
    "machine_downtimes": {},
    "timespan": 3
}

TC_003 = {
    "jobs": {
        "job_1": [([1, 2, 3], [], 1)],
        "job_2": [([1, 2, 3], [], 1)],
        "job_3": [([1, 2, 3], [], 1)]
    },
    "machine_downtimes": {},
    "timespan": 1
}

TC_004 = {
    "jobs": {
        "job_1": [([1], [], 1), ([2], [], 1), ([3], [], 1)]
    },
    "machine_downtimes": {},
    "timespan": 3
}

TC_005 = {
    "jobs": {
        "job_1": [([1], [], 1), ([1], [], 1), ([1], [], 1)]
    },
    "machine_downtimes": {},
    "timespan": 3
}

TC_006 = {
    "jobs": {
        "job_1": [([1, 2, 3], [], 1), ([1, 2, 3], [], 1), ([1, 2, 3], [], 1)]
    },
    "machine_downtimes": {},
    "timespan": 3
}

TC_007 = {
    "jobs": {
        "job_1": [([1], [1], 1)],
        "job_2": [([2], [1], 1)],
        "job_3": [([3], [1], 1)]
    },
    "machine_downtimes": {},
    "timespan": 3
}

TC_008 = {
    "jobs": {
        "job_1": [([1], [1], 1)],
        "job_2": [([1], [1], 1)],
        "job_3": [([1], [1], 1)]
    },
    "machine_downtimes": {},
    "timespan": 3
}

TC_009 = {
    "jobs": {
        "job_1": [([1, 2, 3], [1], 1)],
        "job_2": [([1, 2, 3], [1], 1)],
        "job_3": [([1, 2, 3], [1], 1)]
    },
    "machine_downtimes": {},
    "timespan": 3
}

TC_010 = {
    "jobs": {
        "job_1": [([1], [1], 1), ([2], [1], 1), ([3], [1], 1)]
    },
    "machine_downtimes": {},
    "timespan": 3
}

TC_011 = {
    "jobs": {
        "job_1": [([1], [1], 1), ([1], [1], 1), ([1], [1], 1)]
    },
    "machine_downtimes": {},
    "timespan": 3
}

TC_012 = {
    "jobs": {
        "job_1": [([1, 2, 3], [1], 1), ([1, 2, 3], [1], 1), ([1, 2, 3], [1], 1)]
    },
    "machine_downtimes": {},
    "timespan": 3
}

TC_013 = {
    "jobs": {
        "job_1": [([1], [1], 1)],
        "job_2": [([2], [2], 1)],
        "job_3": [([3], [3], 1)]
    },
    "machine_downtimes": {},
    "timespan": 1
}

TC_014 = {
    "jobs": {
        "job_1": [([1], [1], 1)],
        "job_2": [([1], [2], 1)],
        "job_3": [([1], [3], 1)]
    },
    "machine_downtimes": {},
    "timespan": 3
}

TC_015 = {
    "jobs": {
        "job_1": [([1, 2, 3, 4], [1], 1)],
        "job_2": [([1, 2, 3, 4], [2], 1)],
        "job_3": [([1, 2, 3, 4], [3], 1)]
    },
    "machine_downtimes": {},
    "timespan": 1
}

TC_016 = {
    "jobs": {
        "job_1": [([1], [1], 1), ([2], [2], 1), ([3], [3], 1)]
    },
    "machine_downtimes": {},
    "timespan": 3
}

TC_017 = {
    "jobs": {
        "job_1": [([1], [1], 1), ([2], [2], 1), ([3], [3], 1)]
    },
    "machine_downtimes": {},
    "timespan": 3
}

TC_018 = {
    "jobs": {
        "job_1": [([1, 2, 3], [1], 1), ([1, 2, 3], [2], 1), ([1, 2, 3], [3], 1)]
    },
    "machine_downtimes": {},
    "timespan": 3
}

TC_019 = {
    "jobs": {
        "job_1": [([1], [], 1)],
        "job_2": [([2], [], 1)],
        "job_3": [([3], [], 1)]
    },
    "machine_downtimes": {1: [1, 2], 2: [0, 2], 3: [0, 1]},
    "timespan": 3
}

TC_020 = {
    "jobs": {
        "job_1": [([1, 2, 3], [], 1)],
        "job_2": [([1, 2, 3], [], 1)],
        "job_3": [([1, 2, 3], [], 1)]
    },
    "machine_downtimes": {1: [1, 2], 2: [0, 2], 3: [0, 1]},
    "timespan": 3
}

TC_021 = {
    "jobs": {
        "job_1": [([1], [], 2)]
    },
    "machine_downtimes": {1: [1]},
    "timespan": 4
}


# Casos MK sinteticos e deterministicos, guiados pelos intervalos da pagina 20
# de Brandimarte (1993) e pelo schema local do projeto.


def _mk_machines(job_idx, op_idx, nmac, meq):
    max_choices = min(nmac, meq)
    if max_choices <= 1:
        return [((job_idx + op_idx) % nmac) + 1]

    min_choices = 2
    n_choices_span = max_choices - min_choices + 1
    n_choices = min_choices + ((job_idx * 3 + op_idx * 5) % n_choices_span)

    start = ((job_idx * 7 + op_idx * 11) % nmac) + 1
    step = ((job_idx + op_idx) % (nmac - 1)) + 1 if nmac > 1 else 1

    machines = []
    cursor = start
    for _ in range(nmac * 2):
        if cursor not in machines:
            machines.append(cursor)
        if len(machines) == n_choices:
            break
        cursor = ((cursor + step - 1) % nmac) + 1

    if len(machines) < n_choices:
        for candidate in range(1, nmac + 1):
            if candidate not in machines:
                machines.append(candidate)
            if len(machines) == n_choices:
                break

    machines.sort()
    return machines


def _mk_duration(job_idx, op_idx, proc_min, proc_max, nmac, meq):
    span = proc_max - proc_min + 1
    return proc_min + ((job_idx * 13 + op_idx * 17 + nmac * 5 + meq * 3) % span)


def _mk_equipments(job_idx, op_idx, meq):
    max_eq = max(2, meq)
    eq_count = 1 if max_eq == 1 else 1 + ((job_idx + op_idx) % 2)

    start = ((job_idx * 5 + op_idx * 7) % max_eq) + 1
    step = ((job_idx + op_idx) % max_eq) + 1

    equipments = []
    cursor = start
    for _ in range(max_eq * 2):
        if cursor not in equipments:
            equipments.append(cursor)
        if len(equipments) == eq_count:
            break
        cursor = ((cursor + step - 1) % max_eq) + 1

    if len(equipments) < eq_count:
        for candidate in range(1, max_eq + 1):
            if candidate not in equipments:
                equipments.append(candidate)
            if len(equipments) == eq_count:
                break

    equipments.sort()
    return equipments


def _mk_machine_downtimes(nmac, proc_min, proc_max):
    base = max(1, proc_min // 2)
    gap = max(2, (proc_max - proc_min) // 2 + 1)
    downtimes = {}

    for machine in range(1, nmac + 1):
        t1 = base + (machine % 3)
        t2 = t1 + gap + (machine % 4)
        downtimes[machine] = [t1, t2]

    return downtimes


def _build_mk_case(njob, nmac, nop_max, meq, proc_min, proc_max, adapted=False):
    jobs = {}
    for job_idx in range(1, njob + 1):
        operations = []
        for op_idx in range(1, nop_max + 1):
            machines = _mk_machines(job_idx, op_idx, nmac, meq)
            duration = _mk_duration(job_idx, op_idx, proc_min, proc_max, nmac, meq)
            equipments = _mk_equipments(job_idx, op_idx, meq) if adapted else []
            operations.append((machines, equipments, duration))

        jobs[f"job_{job_idx}"] = operations

    machine_downtimes = _mk_machine_downtimes(nmac, proc_min, proc_max) if adapted else {}
    return {
        "jobs": jobs,
        "machine_downtimes": machine_downtimes,
        "timespan": None,
    }


# Parametros da pagina 20 (Table 1) usados para gerar instancias sinteticas.
_MK_PARAMS = {
    "MK01": {"njob": 10, "nmac": 6, "nop_max": 7, "meq": 3, "proc_min": 1, "proc_max": 7},
    "MK07": {"njob": 20, "nmac": 5, "nop_max": 5, "meq": 5, "proc_min": 1, "proc_max": 20},
    "MK10": {"njob": 20, "nmac": 15, "nop_max": 15, "meq": 5, "proc_min": 5, "proc_max": 20},
    "MK11": {"njob": 30, "nmac": 5, "nop_max": 8, "meq": 2, "proc_min": 10, "proc_max": 30},
    "MK15": {"njob": 30, "nmac": 15, "nop_max": 12, "meq": 5, "proc_min": 10, "proc_max": 30},
}


TC_MK01_NORMAL = _build_mk_case(**_MK_PARAMS["MK01"], adapted=False)
TC_MK01_ADAPTADO = _build_mk_case(**_MK_PARAMS["MK01"], adapted=True)

TC_MK07_NORMAL = _build_mk_case(**_MK_PARAMS["MK07"], adapted=False)
TC_MK07_ADAPTADO = _build_mk_case(**_MK_PARAMS["MK07"], adapted=True)

TC_MK10_NORMAL = _build_mk_case(**_MK_PARAMS["MK10"], adapted=False)
TC_MK10_ADAPTADO = _build_mk_case(**_MK_PARAMS["MK10"], adapted=True)

TC_MK11_NORMAL = _build_mk_case(**_MK_PARAMS["MK11"], adapted=False)
TC_MK11_ADAPTADO = _build_mk_case(**_MK_PARAMS["MK11"], adapted=True)

TC_MK15_NORMAL = _build_mk_case(**_MK_PARAMS["MK15"], adapted=False)
TC_MK15_ADAPTADO = _build_mk_case(**_MK_PARAMS["MK15"], adapted=True)


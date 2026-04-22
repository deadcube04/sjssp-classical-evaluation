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


# # Casos MK sinteticos e deterministicos, guiados pelos intervalos da pagina 20
# # de Brandimarte (1993) e pelo schema local do projeto.


# def _mk_machines(job_idx, op_idx, nmac, meq):
#     max_choices = min(nmac, meq)
#     if max_choices <= 1:
#         return [((job_idx + op_idx) % nmac) + 1]

#     min_choices = 2
#     n_choices_span = max_choices - min_choices + 1
#     n_choices = min_choices + ((job_idx * 3 + op_idx * 5) % n_choices_span)

#     start = ((job_idx * 7 + op_idx * 11) % nmac) + 1
#     step = ((job_idx + op_idx) % (nmac - 1)) + 1 if nmac > 1 else 1

#     machines = []
#     cursor = start
#     for _ in range(nmac * 2):
#         if cursor not in machines:
#             machines.append(cursor)
#         if len(machines) == n_choices:
#             break
#         cursor = ((cursor + step - 1) % nmac) + 1

#     if len(machines) < n_choices:
#         for candidate in range(1, nmac + 1):
#             if candidate not in machines:
#                 machines.append(candidate)
#             if len(machines) == n_choices:
#                 break

#     machines.sort()
#     return machines


# def _mk_duration(job_idx, op_idx, proc_min, proc_max, nmac, meq):
#     span = proc_max - proc_min + 1
#     return proc_min + ((job_idx * 13 + op_idx * 17 + nmac * 5 + meq * 3) % span)


# def _mk_equipments(job_idx, op_idx, meq):
#     max_eq = max(2, meq)
#     eq_count = 1 if max_eq == 1 else 1 + ((job_idx + op_idx) % 2)

#     start = ((job_idx * 5 + op_idx * 7) % max_eq) + 1
#     step = ((job_idx + op_idx) % max_eq) + 1

#     equipments = []
#     cursor = start
#     for _ in range(max_eq * 2):
#         if cursor not in equipments:
#             equipments.append(cursor)
#         if len(equipments) == eq_count:
#             break
#         cursor = ((cursor + step - 1) % max_eq) + 1

#     if len(equipments) < eq_count:
#         for candidate in range(1, max_eq + 1):
#             if candidate not in equipments:
#                 equipments.append(candidate)
#             if len(equipments) == eq_count:
#                 break

#     equipments.sort()
#     return equipments


# def _mk_machine_downtimes(nmac, proc_min, proc_max):
#     base = max(1, proc_min // 2)
#     gap = max(2, (proc_max - proc_min) // 2 + 1)
#     downtimes = {}

#     for machine in range(1, nmac + 1):
#         t1 = base + (machine % 3)
#         t2 = t1 + gap + (machine % 4)
#         downtimes[machine] = [t1, t2]

#     return downtimes


# def _build_mk_case(njob, nmac, nop_max, meq, proc_min, proc_max, adapted=False):
#     jobs = {}
#     for job_idx in range(1, njob + 1):
#         operations = []
#         for op_idx in range(1, nop_max + 1):
#             machines = _mk_machines(job_idx, op_idx, nmac, meq)
#             duration = _mk_duration(job_idx, op_idx, proc_min, proc_max, nmac, meq)
#             equipments = _mk_equipments(job_idx, op_idx, meq) if adapted else []
#             operations.append((machines, equipments, duration))

#         jobs[f"job_{job_idx}"] = operations

#     machine_downtimes = _mk_machine_downtimes(nmac, proc_min, proc_max) if adapted else {}
#     return {
#         "jobs": jobs,
#         "machine_downtimes": machine_downtimes,
#         "timespan": None,
#     }


# # Parametros da pagina 20 (Table 1) usados para gerar instancias sinteticas.
# _MK_PARAMS = {
#     "MK01": {"njob": 10, "nmac": 6, "nop_max": 7, "meq": 3, "proc_min": 1, "proc_max": 7},
#     "MK07": {"njob": 20, "nmac": 5, "nop_max": 5, "meq": 5, "proc_min": 1, "proc_max": 20},
#     "MK10": {"njob": 20, "nmac": 15, "nop_max": 15, "meq": 5, "proc_min": 5, "proc_max": 20},
#     "MK11": {"njob": 30, "nmac": 5, "nop_max": 8, "meq": 2, "proc_min": 10, "proc_max": 30},
#     "MK15": {"njob": 30, "nmac": 15, "nop_max": 12, "meq": 5, "proc_min": 10, "proc_max": 30},
# }


# TC_MK01_NORMAL = _build_mk_case(**_MK_PARAMS["MK01"], adapted=False)
# TC_MK01_ADAPTADO = _build_mk_case(**_MK_PARAMS["MK01"], adapted=True)

# TC_MK07_NORMAL = _build_mk_case(**_MK_PARAMS["MK07"], adapted=False)
# TC_MK07_ADAPTADO = _build_mk_case(**_MK_PARAMS["MK07"], adapted=True)

# TC_MK10_NORMAL = _build_mk_case(**_MK_PARAMS["MK10"], adapted=False)
# TC_MK10_ADAPTADO = _build_mk_case(**_MK_PARAMS["MK10"], adapted=True)

# TC_MK11_NORMAL = _build_mk_case(**_MK_PARAMS["MK11"], adapted=False)
# TC_MK11_ADAPTADO = _build_mk_case(**_MK_PARAMS["MK11"], adapted=True)

# TC_MK15_NORMAL = _build_mk_case(**_MK_PARAMS["MK15"], adapted=False)
# TC_MK15_ADAPTADO = _build_mk_case(**_MK_PARAMS["MK15"], adapted=True)


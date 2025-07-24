import json
from ortools.sat.python import cp_model


def solve_jssp(instance_json):
    jobs_data = instance_json["jobs"]

    model = cp_model.CpModel()

    all_machines = set()
    for job_ops in jobs_data.values():
        for (machines, _, _) in job_ops:
            all_machines.update(machines)
    all_machines = sorted(all_machines)

    horizon = instance_json.get("timespan", 1000)  # fallback horizon

    # Variables to store task intervals
    task_intervals = {}
    machine_to_intervals = {m: [] for m in all_machines}

    # Create variables
    for job_id, job_ops in jobs_data.items():
        for op_id, (machines, _, duration) in enumerate(job_ops):
            suffix = f"_{job_id}_{op_id}"
            start_var = model.NewIntVar(0, horizon, "start" + suffix)
            end_var = model.NewIntVar(0, horizon, "end" + suffix)
            interval_vars = []

            # Create optional intervals for alternative machines
            for m in machines:
                is_present = model.NewBoolVar(f"is_present{suffix}_m{m}")
                interval = model.NewOptionalIntervalVar(
                    start_var, duration, end_var, is_present, f"interval{suffix}_m{m}")
                interval_vars.append((m, interval, is_present))

            task_intervals[(job_id, op_id)] = (start_var, end_var, interval_vars, duration)

    # Constraints for alternative machines: exactly one machine chosen per operation
    for (job_id, op_id), (start_var, end_var, interval_vars, duration) in task_intervals.items():
        model.AddExactlyOne(is_present for (_, _, is_present) in interval_vars)

    # No overlap on machines
    for m in all_machines:
        intervals = []
        presences = []
        for (job_id, op_id), (start_var, end_var, interval_vars, duration) in task_intervals.items():
            for (mm, interval, is_present) in interval_vars:
                if mm == m:
                    intervals.append(interval)
                    presences.append(is_present)
        model.AddNoOverlap(intervals)

    # Precedence constraints inside the job (if more than one op)
    for job_id, job_ops in jobs_data.items():
        for op_id in range(len(job_ops) - 1):
            end_var_current = task_intervals[(job_id, op_id)][1]
            start_var_next = task_intervals[(job_id, op_id + 1)][0]
            model.Add(start_var_next >= end_var_current)

    # Define makespan variable
    makespan = model.NewIntVar(0, horizon, "makespan")

    # All operations must finish before makespan
    ends = [task_intervals[(job_id, op_id)][1]
            for job_id, job_ops in jobs_data.items()
            for op_id in range(len(job_ops))]
    model.AddMaxEquality(makespan, ends)

    # Minimize makespan
    model.Minimize(makespan)

    # Solve model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status in [cp_model.OPTIMAL, cp_model.FEASIBLE]:
        print(f"Optimal makespan: {solver.ObjectiveValue()}")
        # Optional: show start times of jobs
        for job_id, job_ops in jobs_data.items():
            for op_id in range(len(job_ops)):
                start = solver.Value(task_intervals[(job_id, op_id)][0])
                duration = task_intervals[(job_id, op_id)][3]
                print(f"Job {job_id} operation {op_id}: start at {start}, duration {duration}")
        return solver.ObjectiveValue()
    else:
        print("No solution found.")
        return None


# Exemplo de uso com seu JSON:
if __name__ == "__main__":
    json_data = {
        "jobs": {
            "job_1": [([1, 3], [], 1)],
            "job_2": [([2, 3], [], 1)],
            "job_3": [([2, 3], [], 1)],
            "job_4": [([1, 2, 3], [], 2)],
            "job_5": [([1], [], 3)],
            "job_6": [([1], [], 2)],
            "job_7": [([1], [], 4)],
            "job_8": [([1], [], 1)],
            "job_9": [([2], [], 10)],
            "job_10": [([3], [], 1)],
        },
        "machine_downtimes": {},
        "timespan": 20,  # um horizonte suficientemente grande
    }

    makespan = solve_jssp(json_data)
    print(f"Makespan mínimo calculado: {makespan}")

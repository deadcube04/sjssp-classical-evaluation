import json
from ortools.sat.python import cp_model


def solve_fjsp_with_equipment(instance_json):
    """
    Solve Flexible Job Shop Scheduling Problem (FJSP) with equipment constraints and machine downtimes.
    Each operation can be processed on alternative machines and requires specific equipment.
    Machines can have downtime periods during which they cannot process operations.
    """
    jobs_data = instance_json["jobs"]
    machine_downtimes = instance_json.get("machine_downtimes", {})

    model = cp_model.CpModel()

    # Collect all machines and equipment
    all_machines = set()
    all_equipment = set()
    for job_ops in jobs_data.values():
        for (machines, equipment, _) in job_ops:
            all_machines.update(machines)
            all_equipment.update(equipment)
    all_machines = sorted(all_machines)
    all_equipment = sorted(all_equipment)

    horizon = instance_json.get("timespan", 1000)  # fallback horizon

    # Variables to store task intervals
    task_intervals = {}
    machine_to_intervals = {m: [] for m in all_machines}
    equipment_to_intervals = {e: [] for e in all_equipment}

    # Create variables for each operation
    for job_id, job_ops in jobs_data.items():
        for op_id, (machines, equipment, duration) in enumerate(job_ops):
            suffix = f"_{job_id}_{op_id}"
            start_var = model.NewIntVar(0, horizon, "start" + suffix)
            end_var = model.NewIntVar(0, horizon, "end" + suffix)
            
            machine_interval_vars = []
            equipment_interval_vars = []

            # Create optional intervals for alternative machines
            for m in machines:
                is_present_machine = model.NewBoolVar(f"is_present_machine{suffix}_m{m}")
                interval_machine = model.NewOptionalIntervalVar(
                    start_var, duration, end_var, is_present_machine, f"interval_machine{suffix}_m{m}")
                machine_interval_vars.append((m, interval_machine, is_present_machine))
                
                # Add machine downtime constraints
                # machine_downtimes[m] is a list of time points where the machine is unavailable
                if m in machine_downtimes:
                    downtime_list = machine_downtimes[m]
                    # For each downtime point, ensure it doesn't fall within [start_var, end_var)
                    for downtime_point in downtime_list:
                        
                        # Create boolean: is downtime_point before the operation?
                        before_op = model.NewBoolVar(f"before_op{suffix}_m{m}_dt{downtime_point}")
                        
                        # If machine is selected and downtime is before: downtime_point < start_var
                        model.Add(downtime_point < start_var).OnlyEnforceIf([is_present_machine, before_op])
                        
                        # If machine is selected and downtime is not before: downtime_point >= end_var
                        model.Add(downtime_point >= end_var).OnlyEnforceIf([is_present_machine, before_op.Not()])

            # Create optional intervals for alternative equipment
            for e in equipment:
                is_present_equipment = model.NewBoolVar(f"is_present_equipment{suffix}_e{e}")
                interval_equipment = model.NewOptionalIntervalVar(
                    start_var, duration, end_var, is_present_equipment, f"interval_equipment{suffix}_e{e}")
                equipment_interval_vars.append((e, interval_equipment, is_present_equipment))

            task_intervals[(job_id, op_id)] = (
                start_var, end_var, machine_interval_vars, equipment_interval_vars, duration
            )

    # Constraints for alternative machines: exactly one machine chosen per operation
    for (job_id, op_id), (start_var, end_var, machine_interval_vars, equipment_interval_vars, duration) in task_intervals.items():
        # Each operation must be assigned to exactly one machine (if machines are available)
        if machine_interval_vars:
            model.AddExactlyOne(is_present for (_, _, is_present) in machine_interval_vars)
        
        # Each operation must be assigned to exactly one equipment (if equipment are required)
        if equipment_interval_vars:
            model.AddExactlyOne(is_present for (_, _, is_present) in equipment_interval_vars)

    # No overlap on machines
    for m in all_machines:
        intervals = []
        for (job_id, op_id), (start_var, end_var, machine_interval_vars, equipment_interval_vars, duration) in task_intervals.items():
            for (mm, interval, is_present) in machine_interval_vars:
                if mm == m:
                    intervals.append(interval)
        if intervals:
            model.AddNoOverlap(intervals)

    # No overlap on equipment
    for e in all_equipment:
        intervals = []
        for (job_id, op_id), (start_var, end_var, machine_interval_vars, equipment_interval_vars, duration) in task_intervals.items():
            for (ee, interval, is_present) in equipment_interval_vars:
                if ee == e:
                    intervals.append(interval)
        if intervals:
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
        # Show detailed solution
        for job_id, job_ops in jobs_data.items():
            print(f"\n{job_id}:")
            for op_id in range(len(job_ops)):
                start = solver.Value(task_intervals[(job_id, op_id)][0])
                duration = task_intervals[(job_id, op_id)][4]
                
                # Find which machine was selected
                machine_interval_vars = task_intervals[(job_id, op_id)][2]
                selected_machine = None
                for (m, _, is_present) in machine_interval_vars:
                    if solver.Value(is_present):
                        selected_machine = m
                        break
                
                # Find which equipment was selected
                equipment_interval_vars = task_intervals[(job_id, op_id)][3]
                selected_equipment = None
                for (e, _, is_present) in equipment_interval_vars:
                    if solver.Value(is_present):
                        selected_equipment = e
                        break
                
                machine_str = f"Machine {selected_machine}" if selected_machine else "No machine"
                equipment_str = f"Equipment {selected_equipment}" if selected_equipment else "No equipment"
                
                downtime_info = ""
                if selected_machine and selected_machine in machine_downtimes:
                    downtime_list = machine_downtimes[selected_machine]
                    downtime_info = f", Machine downtimes: {downtime_list}"
                
                print(f"  Operation {op_id}: start={start}, duration={duration}, {machine_str}, {equipment_str}{downtime_info}")
        
        return solver.ObjectiveValue()
    else:
        print("No solution found.")
        return None


# Example usage with equipment constraints:
if __name__ == "__main__":
    # Updated example with equipment constraints
    json_data =  {
    "jobs": {
        "job_1": [([1, 2, 3], [], 1)],
        "job_2": [([1, 2, 3], [], 1)],
        "job_3": [([1, 2, 3], [], 1)]
    },
    "machine_downtimes": {1: [1, 2], 2: [0, 2], 3: [0, 1]},
    "timespan": 10
}


    makespan = solve_fjsp_with_equipment(json_data)
    print(f"\n{'='*50}")
    print(f"Optimal makespan calculated: {makespan}")
    print(f"{'='*50}")

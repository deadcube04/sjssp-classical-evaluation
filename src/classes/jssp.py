import numpy as np
from classes.job import Jssp_job
from classes.operation import Operation



class jssp:
    jobs: list

    def __init__(self, data: dict):
        self.jobs = []
        self.process_data(data)

    def process_data(self, data: dict):
        jobs_data = data.get("jobs", {})
        for job_name, operations_details in jobs_data.items():
            # Passar os dados brutos das operações para Jssp_job processar
            job = Jssp_job(job_name, operations_details)
            self.jobs.append(job)
        self.machine_downtimes = data.get("machine_downtimes", {})
        self.timespan = data.get("timespan", None)

    def get_flattened_operations(self):
        operations = []
        for job in self.jobs:
            for operation in job.operations:
                op_details = operation.getOperationDetails()
                op_details["job"] = job.name  # Adicionar o nome do job
                op_details["operation_id"] = operation.id  # Adicionar o ID da operação explicitamente
                operations.append(op_details)
        return operations
    
    
    def __str__(self) -> str:
        result = []
        for job in self.jobs:
            result.append(f"Job: {job.name}")
            for idx, operation in enumerate(job.operations):
                result.append(f"  Operation {idx+1}: Machines: {operation.machines}, Equipments: {operation.equipments}, Duration: {operation.duration}")
        return "\n".join(result)

# data = import_tests_cases("test")
# jsspTest = jssp(data)
# print(jsspTest.__str__())




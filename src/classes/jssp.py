# import os
# import importlib.util
from job import Jssp_job

# def import_tests_cases(nome_dict : str) -> dict:

#     caminho_absoluto = os.path.abspath("tests/test1.py")

#     spec = importlib.util.spec_from_file_location("modulo_temp", caminho_absoluto)
    
#     if spec is None or spec.loader is None:
#         raise ImportError(f"Não foi possível carregar o módulo do arquivo: {caminho_absoluto}")
    
#     modulo = importlib.util.module_from_spec(spec)
#     spec.loader.exec_module(modulo)

    
#     return getattr(modulo, nome_dict)



class jssp:
    jobs: list

    def __init__(self, data: dict):
        self.jobs = []
        self.process_data(data)

    def process_data(self, data: dict):
       
        for job_name, details in data.get("jobs", {}).items():
            job = Jssp_job(
                name=job_name,
                usable_machines=details[0][0],
                equipments_needed=details[0][1],
                duration=details[0][2]
            )
            self.jobs.append(job)
    
    def __str__(self) -> str:
        return "\n".join([f"Job: {job.name}, Usable Machines: {job.usable_machines}, Equipments Needed: {job.equipments_needed}, Duration: {job.duration}" for job in self.jobs])

# data = import_tests_cases("test")
# jsspTest = jssp(data)
# print(jsspTest.__str__())




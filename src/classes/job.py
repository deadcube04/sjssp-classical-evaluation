from .operation import Operation

class Jssp_job:
    def __init__(self, name: str, operations_data: list):
        self.name = name
        self.operations = []
        
        # Processar cada operação e criar objetos Operation com IDs
        for i, (machines, equipments, duration) in enumerate(operations_data):
            operation_id = i + 1  # ID sequencial dentro do job (1, 2, 3...)
            operation = Operation(machines, equipments, duration, operation_id)
            self.operations.append(operation)
class Operation:
    def __init__(self, machines: list, equipments: list, duration: int, id: int):
        self.machines = machines
        self.equipments = equipments
        self.duration = duration
        self.id = id
        
    def getOperationDetails(self):
        return {
            "machines": self.machines,
            "equipments": self.equipments,
            "duration": self.duration,
            "operation_id": self.id
        }
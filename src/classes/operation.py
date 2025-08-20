class Operation:
    def __init__(self, machines: list, equipments: list, duration: int):
        self.machines = machines
        self.equipments = equipments
        self.duration = duration
        
    def getOperationDetails(self):
        return {
            "machines": self.machines,
            "equipments": self.equipments,
            "duration": self.duration
        }
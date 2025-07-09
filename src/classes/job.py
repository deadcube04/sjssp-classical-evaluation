
class Jssp_job:
    def __init__(self, name: str, usable_machines: list, equipments_needed: list, duration: int):
        self.name = name
        self.usable_machines = usable_machines
        self.equipments_needed = equipments_needed
        self.duration = duration
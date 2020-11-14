from project.software.software import Software


class LightSoftware(Software):

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super(LightSoftware, self).__init__(name, 'Light', capacity_consumption, memory_consumption)
        self.capacity_consumption = int(self.capacity_consumption * 1.5)
        self.memory_consumption = int(self.memory_consumption * 0.5)

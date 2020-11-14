from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super(HeavyHardware, self).__init__(name, 'Heavy', capacity, memory)
        self.capacity = int(self.capacity * 2)
        self.memory = int(self.memory * 0.75)

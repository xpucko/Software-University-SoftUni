from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super(PowerHardware, self).__init__(name, 'Power', capacity, memory)
        self.capacity = int(self.capacity * 0.25)
        self.memory = int(self.memory * 1.75)

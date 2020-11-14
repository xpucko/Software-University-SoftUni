from project.software.software import Software


class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        memory_used = sum([s.memory_consumption for s in self.software_components])
        capacity_used = sum([s.capacity_consumption for s in self.software_components])
        current_memory = software.memory_consumption
        current_capacity = software.capacity_consumption

        if memory_used + current_memory > self.memory or capacity_used + current_capacity > self.capacity:
            raise Exception('Software cannot be installed')

        self.software_components.append(software)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)

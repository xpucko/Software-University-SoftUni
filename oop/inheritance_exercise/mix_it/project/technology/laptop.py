from project.technology.technology import Technology


class Laptop(Technology):

    def install_software(self, software, software_memory):
        result = self.get_capacity(self.memory, self.memory_taken + software_memory)
        if result == "Capacity reached!":
            return f"You don't have enough space for {software}!"
        self.memory_taken += software_memory
        return result

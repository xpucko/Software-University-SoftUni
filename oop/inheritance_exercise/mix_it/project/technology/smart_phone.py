from project.technology.technology import Technology


class SmartPhone(Technology):

    def install_apps(self, app, app_memory):
        result = self.get_capacity(self.memory, self.memory_taken + app_memory)
        if result == "Capacity reached!":
            return f"You don't have enough space for {app}!"
        self.memory_taken += app_memory
        return result

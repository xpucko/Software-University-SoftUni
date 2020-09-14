class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        if self.is_on:
            self.is_on = False
        else:
            self.is_on = True

    def install(self, app, memory):
        result = f'Not enough memory to install {app}'
        if memory <= self.memory:
            if self.is_on:
                self.apps.append(app)
                self.memory -= memory
                result = f'Installing {app}'
            else:
                result = f'Turn on your phone to install {app}'
        return result

    def status(self):
        return f'Total apps: {len(self.apps)}. Memory left: {self.memory}'

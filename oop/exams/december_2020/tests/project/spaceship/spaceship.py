class Spaceship:
    SPACESHIP_FULL = "Spaceship is full"
    ASTRONAUT_EXISTS = "Astronaut {} Exists"
    ASTRONAUT_NOT_FOUND = "Astronaut Not Found"
    ASTRONAUT_ADD = "Added astronaut {}"
    ASTRONAUT_REMOVED = "Removed {}"
    ZERO_CAPACITY = 0

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.astronauts = []

    def add(self, astronaut_name: str) -> str:
        if len(self.astronauts) == self.capacity:
            raise ValueError(self.SPACESHIP_FULL)

        if astronaut_name in self.astronauts:
            raise ValueError(self.ASTRONAUT_EXISTS.format(astronaut_name))

        self.astronauts.append(astronaut_name)
        return self.ASTRONAUT_ADD.format(astronaut_name)

    def remove(self, astronaut_name: str) -> str:
        if astronaut_name not in self.astronauts:
            raise ValueError(self.ASTRONAUT_NOT_FOUND.format(astronaut_name))

        self.astronauts.remove(astronaut_name)
        return self.ASTRONAUT_REMOVED.format(astronaut_name)

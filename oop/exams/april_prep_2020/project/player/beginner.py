from abc import ABC

from project.player.player import Player


class Beginner(Player, ABC):
    def __init__(self, username: str):
        super().__init__(username, 50)

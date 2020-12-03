from project.player.player import Player


class BattleField:
    @staticmethod
    def fight(attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError('Player is dead!')

        if attacker.__class__.__name__ == 'Beginner':
            attacker.health += 40
            for c in attacker.card_repository.cards:
                c.damage_points += 30

        if enemy.__class__.__name__ == 'Beginner':
            enemy.health += 40
            for c in enemy.card_repository.cards:
                c.damage_points += 30

        attacker.health += sum(c.health_points for c in attacker.card_repository.cards)
        enemy.health += sum(c.health_points for c in enemy.card_repository.cards)

        attacker.health -= sum(c.damage_points for c in enemy.card_repository.cards)
        enemy.health -= sum(c.damage_points for c in attacker.card_repository.cards)

from Creatures import Creature


class Fighter(Creature):
    default_abilities = {
        "attack": 5,
        "defence": 8,
        "speed": 5
    }

    def __init__(self, name: str, hp: int = 50, abilities: dict = default_abilities):
        Creature.__init__(self, name, hp, abilities)

    def secondary_attack(self, target: Creature):
        if not target:
            return

        self.abilities["attack"] -= 3
        self.attack(target)
        self.abilities["attack"] += 3

    def auto_select(self, target_list: list):
        alive_targets = self.get_alive(target_list)

        if not alive_targets:
            return

        return max(alive_targets, key=lambda creature: creature.check_life())

    def turn(self, round_num: int, target_list: list):
        print(f"{self.get_name()} unleashes a flurry of strikes")
        target = self.auto_select(target_list)
        self.attack(target)

        for i in range(2):
            if target.check_life() == 0:
                target = self.auto_select(target_list)

            self.secondary_attack(target)

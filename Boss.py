from Orc import Orc


class Boss(Orc):
    default_abilities = {
        "attack": 5,
        "defence": 8,
        "speed": 5
    }

    def __init__(self, name, hp=200, abilities=default_abilities, rage_abilities=Orc.default_rage):
        Orc.__init__(self, name, hp, abilities, rage_abilities)

    def auto_select(self, target_list, mode):
        match mode:
            case 'Strong':
                return max(target_list, key=lambda creature: creature.check_life())
            case 'Weak':
                return min(target_list, key=lambda creature: creature.check_life())
            case 'Random':
                return Orc.auto_select(self, target_list)

    def turn(self, round_num, target_list):
        if round_num % 4 == 1:
            target = self.auto_select(target_list, "Strong")
            for _ in range(3):
                if target.check_life() == 0:
                    target = self.auto_select(target_list, "Random")
                self.attack(target)
        else:
            target = self.auto_select(target_list, "Weak")
            self.heavy_attack(target)

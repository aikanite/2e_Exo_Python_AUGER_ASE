import logging

log = logging.getLogger(__name__)


class CharacterError(Exception):
    """Base class for Character error"""


class Character:
    """To implement"""

    def __init__(self, _name : str, _life : float, _attack :float, _defense : float):
        self._name = _name
        self._life = _life
        self._attack = _attack
        self._defense = _defense
    
    def take_damages(self, damages_value : float):
        final_damage = damages_value - damages_value * self._defense
        return final_damage
    
    def attack(self,target: "Character"):
        damages = self._attack
        target.take_damages(damages)
    
    def __repr__(self):
        return f"{self._name} <{self._life}>"
    
    





class Weapon:
    """To implement"""


class Warrior:
    """To implement"""


class Magician:
    """To implement"""

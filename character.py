import logging

log = logging.getLogger(__name__)


class CharacterError(Exception):
    """Base class for Character error"""


class Character:
    """To implement"""

    name = " "
    is_dead = None
    def __init__(self, _name : str, _life : float, _attack :float, _defense : float):
        self._name = _name
        self._life = _life
        self._attack = _attack
        self._defense = _defense
        self.name = self._name
        self.is_dead = (self._life <= 0)
    
    def take_damages(self, damages_value : float):
        final_damage = damages_value - damages_value * self._defense
        self._life = self._life - final_damage
        self.is_dead = (self._life <= 0)
        return final_damage
    
    def attack(self,target: "Character"):
        damages = self._attack
        target.take_damages(damages)
    
    def __repr__(self):
        return f"{self._name} <{self._life}>"

    
#Tests 
Kevin = Character("Kevin",100,10,0.1)
Kevin2 = Character("Kevin2",100,10,0.1)
Kevin.take_damages(1000)
Kevin.attack(Kevin2)
print(Kevin)
print(Kevin2)
print(Kevin.is_dead)
print(Kevin2.is_dead)



class Weapon:
    """To implement"""


class Warrior:
    """To implement"""


class Magician:
    """To implement"""

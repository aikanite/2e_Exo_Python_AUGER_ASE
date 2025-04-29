import random
import logging

log = logging.getLogger(__name__)


#Base statistics of the characters :
default_life = 100
default_attack = 20
default_defense = 0.1


class CharacterError(Exception):
    """Base class for Character error"""


class Character:
    """A class representing a character with a name, life, attack, and defense attributes."""


    def __init__(self, _name : str, _life : float, _attack :float, _defense : float):
        self._name = _name
        self._life = _life
        self._attack = _attack
        self._defense = _defense
    
    #Sets the life of the character :
    def take_damages(self, damages_value : float):
        final_damage = damages_value - damages_value * self._defense
        self._life = self._life - final_damage
        return f"You dealt {final_damage} damages"
    
    #Sets up an attack from the character :
    def attack(self,target: "Character"):
        damages = self._attack
        target.take_damages(damages)
    

    def __repr__(self):
        return f"{self._name} <{self._life}>"
    
    #Returns the name of the character :
    @property
    def name(self):
        return self._name
    
    #Returns true is the character has 0 or bellow HP ; and False if not :
    @property
    def is_dead(self):
        return (self._life <= 0)
    
    #Creates a default character for the user :
    @classmethod
    def default(cls,new_name : str):  
        return cls(new_name, default_life, default_attack, default_defense)




class Weapon:
    """A class representing a weapon with a name and attack damage."""

    name = " "

    def __init__(self, _name : str, attack : float):
        self._name = _name
        self.attack = attack
        self.name = self._name
    

    #Creates a default weapon named 'Wood stick' with 1 attack damage :
    @classmethod
    def default(cls):  
        return cls("Wood stick", 1)
    

    
class Warrior(Character):
    """A class representing a warrior character with a name, weapon, and attributes."""

    def __init__(self,_name : str, weapon : Weapon):
        self._name = _name
        self.weapon = weapon
        self._life = 1.5 * default_life
        self.starting_life = self._life
        self._attack = default_attack
        self._defense = 1.2 * default_defense
    
    #Sets up an attack from the warrior character :
    def attack(self, target : Character):
        
        total_damage = self._attack + self.weapon.attack
        
        #If in state of rage, attack +20%
        if self.is_raging:
            total_damage *= 1.2

        target.take_damages(total_damage)

    #Returns True if the warrior is raging (life < 20% of max life).
    @property
    def is_raging(self):
        return self._life <= 0.2 * self.starting_life




class Magician(Character):
    """A class representing a magician character with a name and attributes."""

    def __init__(self,_name :str):
        self._name = _name
        self._life = 0.8 * default_life
        self.starting_life = self._life
        self._attack = 2 * default_attack
        self._defense = default_defense
        self.Attack_received_count=0
    
    #Chance of casting the shield (1/3) :
    def _activate_magical_shield(self):
        hope = random.randint(1,3)
        if hope == 1:
            return True
        else :
            return False
    
    #Sets up the damage taking of the magician character :
    def take_damages(self, damages_value : float):
        self.Attack_received_count += 1

        final_damage = damages_value - damages_value * self._defense
        self._life = self._life - final_damage
        
        #If the magician has received 3 attacks, he can counter-attack :
        if self.Attack_received_count == 3:
            self.Attack_received_count = 0

            if self._activate_magical_shield():
                return "The attack was countered"
            else :
               return f"You dealt {final_damage} damages" 
            
        else : 
            
            return f"You dealt {final_damage} damages"
        

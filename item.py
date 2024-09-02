from abc import ABC, abstractmethod
from typing import List


class Item:

    def __init__(self, name: str, item_type: str) -> None:
        self.name = name
        self.item_type = item_type

    def info(self):
        print(f"{self.name}")
        print("-----------------")
        print(f"Item Type: {self.item_type}")
        self._info_details()

    @abstractmethod
    def _info_details(self):
        pass


# Affixes and Abilities
# Base Affix class
class Affix(ABC):

    @abstractmethod
    def __str__(self):
        pass


class Damage(Affix):

    def __init__(self, damage: int, martial_increase: int) -> None:
        self.damage = damage
        self.martial_increase = martial_increase

    def __str__(self) -> str:
        return (
            f"*->Damage: {self.damage}\n"
            f"*->Martial Increase: {self.martial_increase}"
        )


# class Armor:

#     def __init__(self, armor) -> None:
#         self.armor = armor


# class MagicArmor:

#     def __init__(self, magic_armor) -> None:
#         self.magic_armor = magic_armor


# class DamageMultiplier:

#     def __init__(self, multiplier) -> None:
#         self.multiplier = multiplier


# class DefenseMultiplier:

#     def __init__(self, multiplier) -> None:
#         self.multiplier = multiplier


# item types
class Weapon(Item):

    def __init__(
        self, name: str, weapon_type: str, affixes: List[Affix]
    ) -> None:
        super().__init__(item_type="Weapon", name=name)
        self.affixes = affixes
        self.weapon_type = weapon_type

    def _info_details(self):
        print(f"Weapon Type: {self.weapon_type}")
        for affix in self.affixes:
            print(affix)


if __name__ == "__main__":
    sword = Weapon(
        name="Excalibur", weapon_type="Great Axe", affixes=[Damage(100, 55)]
    )
    sword.info()

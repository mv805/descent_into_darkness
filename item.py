from abc import ABC, abstractmethod
from typing import List


class Item:

    def __init__(self, name: str, item_type: str, rarity: str) -> None:
        self._name = name
        self._item_type = item_type
        self._rarity = rarity

    @property
    def item_info(self) -> str:
        details = f"{self._name}\n"
        details += "-----------------\n"
        details += f"Item Type: {self._item_type}\n"
        details += f"Rarity: {self._rarity}\n"
        details += self._get_affix_details()
        return details

    @abstractmethod
    def _get_affix_details(self) -> str:
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
        self, name: str, rarity: str, weapon_type: str, affixes: List[Affix]
    ) -> None:
        super().__init__(item_type="Weapon", name=name, rarity=rarity)
        self.affixes = affixes
        self.weapon_type = weapon_type

    def _get_affix_details(self) -> str:
        details = f"Weapon Type: {self.weapon_type}\n"
        for affix in self.affixes:
            details += f"{affix}\n"
        return details.strip()


if __name__ == "__main__":
    sword = Weapon(
        name="Excalibur", weapon_type="Great Axe", affixes=[Damage(100, 55)]
    )
    print(sword.item_info)

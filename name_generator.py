import json
from game_datatypes import ItemRarity, ItemType
from typing import Optional
import random


class ItemNameGenerator:

    def __init__(self) -> None:
        # Load the JSON file
        with open("item_names.json", "r") as f:
            self._word_data = json.load(f)
        self._adjectives = self._word_data["adjectives"]
        self._nouns = self._word_data["nouns"]
        self._verbs = self._word_data["verbs"]
        self._colors = self._word_data["colors"]
        self._ring_types = self._word_data["ring types"]
        self._single_word_names = self._word_data["single word names"]
        self._armor_types = self._word_data["armor types"]
        self._dragon_names = self._word_data["dragon names"]
        self._demon_names = self._word_data["demon names"]
        self._dragon_types = self._word_data["dragon types"]
        self._demon_types = self._word_data["demon types"]
        self._evil_terms = self._word_data["evil terms"]
        self._poems = self._word_data["poems"]
        self._armor_verbs = self._word_data["armor verbs"]

    def generate_item_name(
        self,
        item_type: ItemType,
        item_rarity: ItemRarity,
        weapon_type: Optional[str] = None,
    ) -> str:
        naming_formats = {
            ItemType.WEAPON: {
                ItemRarity.COMMON: (
                    f"{random.choice(self._nouns)}'s {weapon_type}"
                ),
                ItemRarity.SUPERIOR: (
                    f"{random.choice(self._adjectives)} {weapon_type}"
                ),
                ItemRarity.HEROIC: random.choice(
                    [
                        f"{weapon_type} of {random.choice(self._adjectives)} {random.choice(self._verbs)}",
                        f"The {weapon_type} of the {random.choice(self._adjectives)} {random.choice(self._nouns)}",
                    ]
                ),
                ItemRarity.DIVINE: (
                    f"{random.choice(self._single_word_names)}: The "
                    f"{random.choice(self._adjectives)} {random.choice(self._nouns)}"
                ),
                ItemRarity.TRANSCENDENT: (
                    f"{random.choice(self._verbs)} {weapon_type} of "
                    f"the {random.choice(self._dragon_types)} Dragon, "
                    f"Slayer of {random.choice(self._dragon_names)}"
                ),
            },
            ItemType.ARMOR: {
                ItemRarity.COMMON: f"{item_type.value}",
                ItemRarity.SUPERIOR: "return this",
                ItemRarity.HEROIC: "return this",
                ItemRarity.DIVINE: "return this",
                ItemRarity.TRANSCENDENT: "return this",
            },
            ItemType.MAGIC_RING: {
                ItemRarity.COMMON: f"{item_type.value}",
                ItemRarity.SUPERIOR: "return this",
                ItemRarity.HEROIC: "return this",
                ItemRarity.DIVINE: "return this",
                ItemRarity.TRANSCENDENT: "return this",
            },
        }
        return naming_formats[item_type][item_rarity]


if __name__ == "__main__":

    ITERATIONS = 50
    name_generator = ItemNameGenerator()
    word_data = None
    with open("item_names.json", "r") as f:
        word_data = json.load(f)
    weapon_names = word_data["weapon types"]
    rarities = list(ItemRarity)

    for i in range(1, ITERATIONS):
        print(
            name_generator.generate_item_name(
                ItemType.WEAPON,
                random.choice(rarities),
                random.choice(weapon_names),
            )
        )

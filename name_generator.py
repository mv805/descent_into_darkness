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
        """
        Generate a name for an item based on its type and rarity.

        Parameters:
            item_type (ItemType): The type of the item.
            item_rarity (ItemRarity): The rarity of the item.
            weapon_type (Optional[str]): The type of the weapon if applicable (default: None).

        Returns:
            str: The generated name for the item.
        """
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
                ItemRarity.HEROIC: random.choice(
                    [
                        f"{random.choice(self._colors)} Ring",
                        f"{random.choice(self._verbs)} {random.choice(self._ring_types)}",
                        f"{random.choice(self._ring_types)} of {random.choice(self._verbs)}",
                        f"The {random.choice(self._verbs)} {random.choice(self._nouns)}",
                    ]
                ),
                ItemRarity.DIVINE: (
                    f"The {random.choice(self._colors)} {random.choice(self._ring_types)} of "
                    f"the {random.choice(self._adjectives)} {random.choice(self._nouns)}"
                ),
                ItemRarity.TRANSCENDENT: (
                    f"{random.choice(self._demon_names)} {random.choice(self._ring_types)}: "
                    f"Ring of the {random.choice(self._evil_terms)} {random.choice(self._demon_types)}"
                ),
            },
        }

        # There should not be any common or superior rings
        if item_type == ItemType.MAGIC_RING and (
            item_rarity == ItemRarity.COMMON
            or item_rarity == ItemRarity.SUPERIOR
        ):
            raise (
                ValueError(
                    "Common or superior quality magic rings do not exist."
                )
            )
        else:
            return naming_formats[item_type][item_rarity]


if __name__ == "__main__":

    ITERATIONS = 50
    name_generator = ItemNameGenerator()
    word_data = None
    with open("item_names.json", "r") as f:
        word_data = json.load(f)
    weapon_names = word_data["weapon types"]
    rarities = list(ItemRarity)
    ring_rarities = [ItemRarity.HEROIC, ItemRarity.DIVINE, ItemRarity.TRANSCENDENT]

    for i in range(1, ITERATIONS):
        print(
            name_generator.generate_item_name(
                ItemType.WEAPON,
                random.choice(rarities),
                random.choice(weapon_names),
            )
        )
    print("------------------")
    for i in range(1, ITERATIONS):
        print(
            name_generator.generate_item_name(
                ItemType.MAGIC_RING,
                random.choice(ring_rarities)
            )
        )

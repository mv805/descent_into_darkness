from enum import Enum


class ItemRarity(Enum):
    COMMON = "Common"
    SUPERIOR = "Superior"
    HEROIC = "Heroic"
    DIVINE = "Divine"
    TRANSCENDENT = "Transcendent"


class ItemType(Enum):
    WEAPON = "Weapon"
    ARMOR = "Armor"
    MAGIC_RING = "Magic Ring"

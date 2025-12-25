from dataclasses import dataclass
from typing import List

@dataclass
class Product:
    name: str
    concentration: str
    skin_type: str
    key_ingredients: List[str]
    benefits: List[str]
    how_to_use: str
    side_effects: str
    price: str

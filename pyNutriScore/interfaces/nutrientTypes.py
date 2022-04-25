from enum import Enum


class NutrientTypes(Enum):
    ENERGY = "energy"
    SUGAR = "sugar"
    SAT_FATS = "saturated_fats"
    SODIUM = "sodium"
    FRUIT = "fruit_percentage"
    FIBERS = "fibers"
    PROTEINS = "proteins"


bad_nutrients = [NutrientTypes.ENERGY, NutrientTypes.SUGAR, NutrientTypes.SAT_FATS, NutrientTypes.SODIUM]
good_nutrients = [NutrientTypes.PROTEINS, NutrientTypes.FIBERS, NutrientTypes.FRUIT]
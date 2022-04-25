from enum import Enum
from pyNutriScore.interfaces.foodTypes import FoodTypes
from pyNutriScore.interfaces.nutrientTypes import NutrientTypes


class NutrientScore(Enum):
    FoodTypes.SOLID: [float, float, float]
    FoodTypes.BEVERAGE: [float, float, float]


class ScoreTable(Enum):
    NutrientTypes.ENERGY: NutrientScore
    NutrientTypes.SUGAR: NutrientScore
    NutrientTypes.SAT_FATS: NutrientScore
    NutrientTypes.SODIUM: NutrientScore
    NutrientTypes.FRUIT: NutrientScore
    NutrientTypes.FIBERS: NutrientScore
    NutrientTypes.PROTEINS: NutrientScore
    nutri_class: NutrientScore


class NutrientValues(Enum):
    NutrientTypes.ENERGY: float
    NutrientTypes.SUGAR: float
    NutrientTypes.SAT_FATS: float
    NutrientTypes.SODIUM: float
    NutrientTypes.FRUIT: float
    NutrientTypes.FIBERS: float
    NutrientTypes.PROTEINS: float

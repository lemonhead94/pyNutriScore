import json
import functools
from .interfaces.foodTypes import FoodTypes
from .interfaces.nutrientTypes import NutrientTypes, good_nutrients, bad_nutrients
from .interfaces.scoreTableInterface import NutrientValues
from importlib import resources


class NutriScore:
    # nutrient-score table for determining the nutrient-score for nutrient type
    with resources.open_binary('pyNutriScore.interfaces', 'scoreTable.json') as json_file:
        score_table = json.load(json_file)

    def nutrient_score(self, nutrient_score_ranges: [[float, float, float]], nutrient_value: float) -> float:
        return functools.reduce(
            lambda score, score_range: score_range[2] if self.in_range(nutrient_value, score_range[0],
                                                                       score_range[1]) else score,
            nutrient_score_ranges, 0)

    def nutrient_list_score(self, nutrient_list: [NutrientTypes], food_type: FoodTypes,
                            nutrient_values: NutrientValues) -> float:
        return functools.reduce(lambda score, nutrient_type: score + self.nutrient_score(
            self.score_table[nutrient_type.value][food_type if isinstance(food_type, str) else food_type.value],
            nutrient_values[nutrient_type.value]), nutrient_list, 0)

    def calculate(self, nutrient_values: NutrientValues, food_type: FoodTypes = FoodTypes.SOLID) -> float:
        bad_nutrients_score = self.nutrient_list_score(bad_nutrients, food_type, nutrient_values)
        good_nutrients_score = self.nutrient_list_score(good_nutrients, food_type, nutrient_values)

        food_key = food_type if isinstance(food_type, str) else food_type.value
        fruit_score = self.nutrient_score(self.score_table[NutrientTypes.FRUIT.value][food_key],
                                          nutrient_values[NutrientTypes.FRUIT.value])
        fibers_score = self.nutrient_score(self.score_table[NutrientTypes.FIBERS.value][food_key],
                                           nutrient_values[NutrientTypes.FIBERS.value])

        return bad_nutrients_score - fibers_score - fruit_score if bad_nutrients_score >= 11 and fruit_score < 5 else bad_nutrients_score - good_nutrients_score

    def calculate_class(self, nutrient_values: NutrientValues, food_type: FoodTypes = FoodTypes.SOLID) -> str:
        score = self.calculate(nutrient_values, food_type)
        class_number = self.nutrient_score(self.score_table["nutriClass"][food_type], score)
        return ''.join(map(chr, [64 + class_number]))

    # Checks whether a number is inside range (min, max]
    @staticmethod
    def in_range(x: float, min_value: float, max_value: float) -> bool:
        return (x - 0.000001 - min_value) * (x - max_value) <= 0

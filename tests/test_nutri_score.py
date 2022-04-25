import unittest

from pyNutriScore.nutri_score import NutriScore
from pyNutriScore.interfaces.foodTypes import FoodTypes
from pyNutriScore.interfaces.nutrientTypes import NutrientTypes


class NutriScoreTest(unittest.TestCase):

    def test_nutrient_table_score_algo(self):
        score_table_2 = [[float('-inf'), 0, 0],
                         [1, 30, 1],
                         [30, 60, 2],
                         [60, 90, 3],
                         [90, 120, 4],
                         [120, 150, 5],
                         [150, 180, 6],
                         [180, 210, 7],
                         [210, 240, 8],
                         [240, 270, 9],
                         [270, float('inf'), 10]]

        self.assertEqual(NutriScore().nutrient_score(score_table_2, -1000), 0)
        self.assertEqual(NutriScore().nutrient_score(score_table_2, 0), 0)
        self.assertEqual(NutriScore().nutrient_score(score_table_2, 1), 0)
        self.assertEqual(NutriScore().nutrient_score(score_table_2, 30), 1)
        self.assertEqual(NutriScore().nutrient_score(score_table_2, 31), 2)
        self.assertEqual(NutriScore().nutrient_score(score_table_2, 10000), 10)

    def test_in_range_method(self):
        self.assertTrue(NutriScore().in_range(5, 1, 10))
        self.assertFalse(NutriScore().in_range(11, 1, 10))
        self.assertFalse(NutriScore().in_range(0, 1, 10))
        self.assertTrue(NutriScore().in_range(-5, -15, -3))
        self.assertTrue(NutriScore().in_range(0, -1, 0))
        self.assertFalse(NutriScore().in_range(-1, -1, 0))
        self.assertTrue(NutriScore().in_range(-0.99999, -1, 0))

    def test_calculation_with_special_case(self):
        result = NutriScore().calculate(
            {
                'energy': 2000,
                'fibers': 3,
                'fruit_percentage': 42,
                'proteins': 5,
                'saturated_fats': 3,
                'sodium': 500,
                'sugar': 22,
            },
            'solid'
        )
        self.assertEqual(result, 12)

    def test_individual_nutrients(self):
        nutri_score = NutriScore()

        self.assertEqual(
            nutri_score.nutrient_score(nutri_score.score_table[NutrientTypes.FIBERS.value][FoodTypes.SOLID.value], 3),
            3)
        self.assertEqual(
            NutriScore().nutrient_score(nutri_score.score_table[NutrientTypes.PROTEINS.value][FoodTypes.SOLID.value],
                                        5), 3)
        self.assertEqual(
            NutriScore().nutrient_score(nutri_score.score_table[NutrientTypes.FRUIT.value][FoodTypes.SOLID.value], 42),
            1)

    def test_another_calculation_without_special_case(self):
        result = NutriScore().calculate(
            {
                'energy': 0,
                'fibers': 3,
                'fruit_percentage': 42,
                'proteins': 5,
                'saturated_fats': 2,
                'sodium': 500,
                'sugar': 22,
            },
            'solid'
        )
        self.assertEqual(result, 3)

    def test_different_calculation_without_special_case(self):
        result = NutriScore().calculate(
            {
                'energy': 0,
                'fibers': 4,
                'fruit_percentage': 60,
                'proteins': 2,
                'saturated_fats': 2,
                'sodium': 500,
                'sugar': 10,
            },
            'solid'
        )
        self.assertEqual(result, 2)

    def test_different_calculation_without_special_case_class(self):
        result = NutriScore().calculate_class(
            {
                'energy': 0,
                'fibers': 4,
                'fruit_percentage': 60,
                'proteins': 2,
                'saturated_fats': 2,
                'sodium': 500,
                'sugar': 10,
            },
            'solid'
        )
        self.assertEqual(result, "B")


if __name__ == '__main__':
    unittest.main()

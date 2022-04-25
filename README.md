# pyNutriScore

<p align="center">
  <img width="568" height="307" src="https://raw.githubusercontent.com/lemonhead94/pyNutriScore/main/assets/images/nutri-score-logo.png" alt="Nutri Score logo">
</p>

> The goal of the project is to provide simple package that can calculate the Nutri-Score.

## What is the Nutri-Score ?

The Nutri-Score is a nutrition label that converts the nutritional value of products into a simple code consisting of 5 letters, each with its own colour.

Each product is awarded a score based on a scientific algorithm.

This formula takes into account the nutrients to avoid (energy value and the amount of sugars, saturated fats and salt) and the positive ones (the amount of fibre, protein, fruit, vegetables and nuts).

You can therefore see at a glance which products are recommended and which should be avoided.

> Source: <https://nutriscore.colruytgroup.com/colruytgroup/en/about-nutri-score/>

Paper: <https://pdfs.semanticscholar.org/3d1c/c206bc286bb5f80452821a0d26ff9e55b387.pdf>

## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/lemonhead94/pyNutriScore

## Usage

### Import the library

```sh
pip install pyNutriScore
```

### Calculate the nutri-score:

```python
from pyNutriScore import NutriScore

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
    'solid'  # either 'solid' or 'beverage'
)

print(result)  # Output: 2
```

### Calculate the nutri-score class:

```python
from pyNutriScore import NutriScore

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
    'solid'  # either 'solid' or 'beverage'
)

print(result)  # Output: "B"
```

## License
[MIT](LICENSE)

## Contribution

Feel free to add suggestions, PRs, comments and bug reports.

## Credits
This is a re-implementation of the TypeScript package [nutri-score](https://github.com/food-nutrients/nutri-score/) by [Alex Kolarski](aleks.rk@gmail.com) in Python.

## Authors

Jorit Studer (jorit.studer@gmail.com)
from flask import Flask

app = Flask(__name__)
from json import load

with open('src/data/form1.json', 'r') as recipes_file:
    recipes = load(recipes_file)

with open('src/data/widgets.json', 'r') as ingredients_file:
    ingredients = load(ingredients_file)

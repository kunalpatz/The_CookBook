from flask import render_template
from cook import API
from src import app, recipes, ingredients

api_class = API(recipes)


@app.route('/')
def home():
    api_class.build_js(ingredients)
    api_class.build_css(ingredients)
    api_class.build_page(ingredients)
    return render_template('home.html')


if __name__ == '__main__':
    app.run(port=6262)
